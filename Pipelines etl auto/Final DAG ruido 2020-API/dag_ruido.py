from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def run_main_ruido():
    from main_ruido import main
    main()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dag_ruido',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    description='DAG para procesamiento y carga de datos de ruido'
)

tarea_ruido = PythonOperator(
    task_id='run_main_ruido',
    python_callable=run_main_ruido,
    dag=dag,
)
