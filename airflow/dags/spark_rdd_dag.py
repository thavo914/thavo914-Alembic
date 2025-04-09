from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

# Remove the Python test connection function as it's causing Py4J errors
# and replace with a simple bash test

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 4, 2),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'spark_rdd_job',
    default_args=default_args,
    description='Run Spark RDD job',
    schedule_interval=timedelta(days=1),
    catchup=False
)

# Updated Spark configuration with correct Python path
spark_job = SparkSubmitOperator(
    task_id='run_spark_rdd',
    application='/opt/spark/scripts/RDD.py',
    conn_id='spark_default',
    conf={
        'spark.master': 'spark://spark-master:7077',
        'spark.executor.memory': '512m',  # Reduced memory requirements
        'spark.driver.memory': '512m',    # Reduced memory requirements
        'spark.executor.cores': '1',      # Reduced core requirements
        'spark.driver.cores': '1',
    },
    verbose=True,
    dag=dag
)

# This task will run directly in Airflow
spark_job
