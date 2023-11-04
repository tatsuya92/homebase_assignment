from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from dags_function.iris_plant import transfer_data


default_args = {
    'owner': 'user',
    'start_date': datetime(2023, 11, 4),
    'depends_on_past': False,
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'postgresql_to_cliclhouse',
    default_args=default_args,
    schedule_interval=timedelta(hours=1),
    catchup=False
)

data_transfer = PythonOperator(
    task_id = 'transfer_postgresql_to_clickhouse',
    python_callable=transfer_data,
    provide_context=True,
    dag=dag
)
