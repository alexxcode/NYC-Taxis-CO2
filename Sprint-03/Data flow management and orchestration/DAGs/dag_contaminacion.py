from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Función para ejecutar el script principal

def run_main_contaminacion():
    from main_contaminacion import main
    main()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 17),
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
