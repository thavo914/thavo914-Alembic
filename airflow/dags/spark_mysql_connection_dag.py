from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.providers.telegram.operators.telegram import TelegramOperator
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
    'mysql_connection_test',
    default_args=default_args,
    description='Test MySQL connection with notifications',
    schedule_interval=None,
    catchup=False
)

spark_job = SparkSubmitOperator(
    task_id='spark_mysql_job',
    application='/opt/spark/scripts/test_mysql_connection.py',
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

notify_success = TelegramOperator(
    task_id='notify_success',
    telegram_conn_id='telegram_default',
    chat_id='1977848679',
    text='✅ Spark MySQL job completed successfully!',
    dag=dag
)

notify_failure = TelegramOperator(
    task_id='notify_failure',
    telegram_conn_id='telegram_default',
    chat_id='1977848679',
    text='❌ Spark MySQL job failed!',
    trigger_rule='one_failed',
    dag=dag
)

spark_job >> [notify_success, notify_failure]