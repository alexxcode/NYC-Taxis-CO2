from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def run_main_light_duty_vehicles():
    from main_light_duty_vehicles import main
    main()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dag_light_duty_vehicles',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    description='DAG para procesamiento y carga de datos de vehículos ligeros'
)

task = PythonOperator(
    task_id='run_main_light_duty_vehicles',
    python_callable=run_main_light_duty_vehicles,
    dag=dag,
)
