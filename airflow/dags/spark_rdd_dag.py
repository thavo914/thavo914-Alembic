from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

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

spark_job = SparkSubmitOperator(
    task_id='run_spark_rdd',
    application='/opt/spark/scripts/rdd.py',  # Path mounted in docker-compose
    conn_id='spark_default',
    conf={
        'spark.master': 'spark://spark-master:7077',
        'spark.executor.instances': '2',
        'spark.executor.memory': '2g'
    },
    dag=dag
)