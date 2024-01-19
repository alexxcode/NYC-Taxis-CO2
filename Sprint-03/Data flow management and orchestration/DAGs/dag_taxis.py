from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def run_main_taxis():
    import main_taxis 
    main_taxis.main()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 17),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dag_taxis',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    description='DAG para procesamiento y carga de datos new'
)

task_taxis = PythonOperator(
    task_id='run_main_taxis',
    python_callable=run_main_taxis,
    dag=dag,
)
