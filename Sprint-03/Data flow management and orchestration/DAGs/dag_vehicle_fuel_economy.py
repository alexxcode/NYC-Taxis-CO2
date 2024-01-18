from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def run_main_vehicle_fuel_economy():
    import main_vehicle_fuel_economy
    main_vehicle_fuel_economy.main()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 16),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dag_vehicle_fuel_economy',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    description='DAG para procesar datos de economía de combustible de vehículos'
)

task = PythonOperator(
    task_id='run_main_vehicle_fuel_economy',
    python_callable=run_main_vehicle_fuel_economy,
    dag=dag,
)
