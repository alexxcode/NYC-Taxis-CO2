from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Función para ejecutar el script principal
def run_main_contaminacion():
    from main_contaminacion import api_key, zones_names, start_date, end_date, bucket_name, raw_folder, curated_folder
    from etl_contaminacion import extract_data, transform_data, aggregate_monthly_with_boroughs, upload_to_bucket
    from datetime import datetime

    # Extracción
    df_raw = extract_data(api_key, zones_names, start_date, end_date)

    # Carga de los datos en bruto
    upload_to_bucket(df_raw, bucket_name, raw_folder, 'datos_contaminacion_raw.csv')

    # Transformación y agregación
    df_transformed = transform_data(df_raw)
    df_monthly = aggregate_monthly_with_boroughs(df_transformed)

    # Carga de los datos transformados
    upload_to_bucket(df_monthly, bucket_name, curated_folder, 'datos_contaminacion_curados.csv')

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dag_contaminacion',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    description='DAG para procesamiento y carga de datos de contaminacion'
)

tarea_contaminacion = PythonOperator(
    task_id='run_main_contaminacion',
    python_callable=run_main_contaminacion,
    dag=dag,
)
