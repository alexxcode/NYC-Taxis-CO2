from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def run_main_charging_stations():
    import main_charging_stations
    main_charging_stations.main()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dag_charging_stations',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    description='DAG para procesar datos de estaciones de carga de combustible alternativo'
)

task = PythonOperator(
    task_id='run_main_charging_stations',
    python_callable=run_main_charging_stations,
    dag=dag,
)
