from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def run_main_contaminacion_historico():
    from main_contaminacion_historico import main
    main()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dag_contaminacion_historico',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    description='DAG para procesamiento y carga de datos de contaminacion historico'
)

task_contaminacion_historico = PythonOperator(
    task_id='run_main_contaminacion_historico',
    python_callable=run_main_contaminacion_historico,
    dag=dag,
)
