from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def run_main_electric_cars():
    import main_electric_cars
    main_electric_cars.main()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dag_electric_cars',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    description='DAG para procesar datos de autos eléctricos'
)

task = PythonOperator(
    task_id='run_main_electric_cars',
    python_callable=run_main_electric_cars,
    dag=dag,
)
