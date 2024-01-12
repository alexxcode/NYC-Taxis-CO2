from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def run_main_taxi_zones():
    import main_taxi_zones
    main_taxi_zones.main()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dag_taxi_zones',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    description='DAG para procesar datos de taxi zones'
)

task = PythonOperator(
    task_id='run_main_taxi_zones',
    python_callable=run_main_taxi_zones,
    dag=dag,
)
