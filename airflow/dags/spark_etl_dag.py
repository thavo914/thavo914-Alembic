from airflow.decorators import dag, task
from datetime import datetime, timedelta  # Add timedelta import
from pyspark.sql import SparkSession
from pyspark import SparkContext
import time
import socket

def is_port_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

@dag(
    schedule_interval="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    dag_id='spark_etl_pipeline'
)
def spark_etl():
    @task(retries=3, retry_delay=timedelta(seconds=10))  # Use timedelta directly
    def extract():
        # Try to create Spark session with retries
        max_retries = 3
        retry_count = 0
        while retry_count < max_retries:
            try:
                spark = SparkSession.builder \
                    .appName('ExtractTask') \
                    .master('spark://spark-master:7077') \
                    .config('spark.network.timeout', '120s') \
                    .config('spark.executor.heartbeatInterval', '60s') \
                    .getOrCreate()
                return
            except Exception as e:
                retry_count += 1
                if retry_count == max_retries:
                    raise e
                print(f"Failed to connect to Spark. Retrying in 10 seconds... (Attempt {retry_count}/{max_retries})")
                time.sleep(10)

    raw_data = extract()

dag = spark_etl()