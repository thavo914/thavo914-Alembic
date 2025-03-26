from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'spark_user_etl',
    default_args=default_args,
    schedule_interval='@daily'
)

spark_job = SparkSubmitOperator(
    task_id='process_users',
    application='/opt/spark/scripts/RDD.py',
    conn_id='spark_default',
    # master='spark://spark-master:7077',
    dag=dag
)

