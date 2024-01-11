# dag_vehiculos.py

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def run_main_vehiculos():
    from main_vehiculos import main
    main()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dag_vehiculos',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    description='DAG para procesamiento y carga de datos de vehículos'
)

tarea_vehiculos = PythonOperator(
    task_id='run_main_vehiculos',
    python_callable=run_main_vehiculos,
    dag=dag,
)
