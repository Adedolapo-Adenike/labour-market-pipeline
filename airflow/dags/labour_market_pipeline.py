from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Default settings for all tasks
default_args = {
    'owner': 'adedolapo',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Define the DAG
dag = DAG(
    'labour_market_pipeline',
    default_args=default_args,
    description='Fetches Nigeria and UK economic data weekly',
    schedule_interval='@weekly',
    start_date=datetime(2026, 1, 1),
    catchup=False
)

# Task 1 - Fetch data from World Bank API
fetch_data = BashOperator(
    task_id='fetch_world_bank_data',
    bash_command='cd /opt/airflow/dags && py ingest.py',
    dag=dag
)

# Task 2 - Upload to AWS S3
upload_to_s3 = BashOperator(
    task_id='upload_to_s3',
    bash_command='cd /opt/airflow/dags && py upload_to_s3.py',
    dag=dag
)

# Task 3 - Run dbt transformations
run_dbt = BashOperator(
    task_id='run_dbt_models',
    bash_command='cd /opt/airflow/dags && dbt run --project-dir labour_market_dbt',
    dag=dag
)

# Define the order of tasks
fetch_data >> upload_to_s3 >> run_dbt