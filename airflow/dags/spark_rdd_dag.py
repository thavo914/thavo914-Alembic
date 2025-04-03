from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def test_spark_connection():
    from pyspark.sql import SparkSession
    from pyspark.sql.types import StructType, StructField, StringType, IntegerType
    from pyspark.sql import Row
    
    try:
        print("Initializing Spark connection...")
        spark = SparkSession.builder \
            .appName("TestConnection") \
            .config("spark.master", "spark://spark-master:7077") \
            .config("spark.driver.host", "airflow-webserver") \
            .config("spark.driver.memory", "1g") \
            .config("spark.executor.memory", "1g") \
            .config("spark.python.worker.memory", "1g") \
            .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
            .config("spark.python.use.daemon", "false") \
            .config("spark.rdd.compress", "true") \
            .getOrCreate()
        
        print("Creating test DataFrame...")
        # Create Row object
        # TestRow = Row("col1", "col2")
        # data = [TestRow("Test", 1)]
        
        # df = spark.createDataFrame(data)
        print("\nSpark Connection Test Results:")
        print(f"Spark Version: {spark.version}")
        print(f"Spark Master: {spark.sparkContext.master}")
        print("\nTest DataFrame:")
        # df.show()
        
        return True
    except Exception as e:
        print(f"Error in Spark connection test: {str(e)}")
        raise e
    finally:
        if 'spark' in locals():
            print("Closing Spark session...")
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
    application='/opt/spark/scripts/RDD.py',  # Updated path
    conn_id='spark_default',
    conf={
        'spark.master': 'spark://spark-master:7077',
        'spark.executor.memory': '1g',
        'spark.driver.memory': '1g',
        'spark.executor.cores': '2',
        'spark.driver.cores': '1',
        'spark.python.version': '3.8',
        'spark.submit.deployMode': 'client'
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
