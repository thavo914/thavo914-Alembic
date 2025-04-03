from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def test_spark_connection():
    from pyspark.sql import SparkSession
    from pyspark.sql.types import StructType, StructField, StringType, IntegerType
    from pyspark.sql import Row
    
    try:
        print("Testing Spark master connection...")
        spark = SparkSession.builder \
            .appName("TestConnection") \
            .config("spark.master", "spark://spark-master:7077") \
            .config("spark.driver.bindAddress", "0.0.0.0") \
            .config("spark.driver.host", "airflow-webserver") \
            .getOrCreate()
        
        # Test if we can execute a simple Spark operation
        test_data = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
        count = test_data.count()
        print(f"Successfully connected to Spark master!")
        print(f"Test data count: {count}")
        print(f"Spark master URL: {spark.sparkContext.master}")
        print(f"Available executors: {len(spark.sparkContext._jsc.sc().statusTracker().getExecutorInfos())}")
        
        return True
    except Exception as e:
        print(f"Error connecting to Spark master: {str(e)}")
        raise e
    finally:
        if 'spark' in locals():
            spark.stop()

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

# Updated Spark configuration
spark_job = SparkSubmitOperator(
    task_id='run_spark_rdd',
    application='/opt/spark/scripts/RDD.py',
    conn_id='spark_default',
    conf={
        'spark.master': 'spark://spark-master:7077',
        'spark.executor.memory': '1g',
        'spark.driver.memory': '1g',
        'spark.executor.cores': '2',
        'spark.driver.cores': '1',
        'spark.python.version': '3.8',
        'spark.submit.deployMode': 'client',
        'spark.driver.bindAddress': '0.0.0.0'  # Add this line
    },
    verbose=True,
    dag=dag
)

test_connection = PythonOperator(
    task_id='test_spark_connection',
    python_callable=test_spark_connection,
    dag=dag
)

test_connection >> spark_job
