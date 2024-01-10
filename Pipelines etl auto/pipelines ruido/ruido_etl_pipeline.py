from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from etl import descargar_datos_si_necesario, transformar_datos, cargar_datos

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('ruido_etl_pipeline',
          default_args=default_args,
          description='ETL para datos de ruido',
          schedule_interval=timedelta(days=1))

descargar_datos = PythonOperator(
    task_id='descargar_datos',
    python_callable=descargar_datos_si_necesario,
    dag=dag,
)

transformar_datos = PythonOperator(
    task_id='transformar_datos',
    python_callable=transformar_datos,
    op_kwargs={'bucket_name': 'us-west4-eduardopc-bcaeda57-bucket', 'origen_blob': 'datos_descargados.csv'},
    dag=dag,
)

cargar_datos = PythonOperator(
    task_id='cargar_datos',
    python_callable=cargar_datos,
    op_kwargs={'nombre_archivo': 'ruido.csv', 'bucket_name': 'us-west4-eduardopc-bcaeda57-bucket'},
    dag=dag,
)

descargar_datos >> transformar_datos >> cargar_datos
