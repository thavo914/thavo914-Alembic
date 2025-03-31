from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),  # Changed from days_ago
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'rpt_TimeSalaryCalculation_NEW',
    default_args=default_args,
    description='Salary calculation report using Spark',
    schedule_interval='0 1 * * *',  # Run at 1 AM daily
    catchup=False
)

# Initialize database connections and temp tables
def init_database(**context):
    # Add your MySQL connection initialization here
    print("Initializing database connections...")

init_task = PythonOperator(
    task_id='init_database',
    python_callable=init_database,
    provide_context=True,
    dag=dag
)

# Spark job to process the data
spark_process = SparkSubmitOperator(
    task_id='spark_salary_calculation',
    application='/opt/spark/scripts/salary_calculation.py',
    name='TimeSalaryCalculation',
    conn_id='spark_default',
    conf={
        "spark.driver.memory": "2g",
        "spark.executor.memory": "2g",
        "spark.executor.cores": "2",
        "spark.driver.host": "spark-master",
        "spark.driver.bindAddress": "0.0.0.0",
    },
    dag=dag
)

# Define task sequence
init_task >> spark_process
