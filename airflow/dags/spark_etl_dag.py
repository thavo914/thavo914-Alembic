from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.models import Connection
from airflow.utils.session import provide_session
from datetime import datetime, timedelta
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'spark_etl_pipeline',
    default_args=default_args,
    description='A simple Spark ETL pipeline',
    schedule_interval=timedelta(days=1),
    catchup=False
)

spark_job = SparkSubmitOperator(
    task_id='run_spark_job',
    application='/opt/spark/scripts/RDD.py',
    name='user_data_etl',
    conn_id='spark_default',
    executor_memory='2g',
    num_executors='2',
    dag=dag
)

spark_job