from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 4, 5),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'test_spark_permissions',
    default_args=default_args,
    description='Test file permissions in Spark container',
    schedule_interval=None,
    catchup=False
)

test_permissions = SparkSubmitOperator(
    task_id='test_permissions',
    application='/opt/spark/scripts/test_permissions.py',
    conn_id='spark_default',
    conf={
        'spark.master': 'spark://spark-master:7077',
        'spark.executor.memory': '512m',
        'spark.driver.memory': '512m',
        'spark.executor.cores': '1',
        'spark.driver.cores': '1'
    },
    verbose=True,
    dag=dag
)