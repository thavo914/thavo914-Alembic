from airflow.decorators import dag, task
from datetime import datetime
from pyspark.sql import SparkSession

@dag(
    schedule_interval="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    dag_id='spark_etl_pipeline'
)
def spark_etl():
    @task()
    def extract():
        spark = SparkSession.builder \
            .appName('ExtractTask') \
            .master('spark://spark-master:7077') \
            .getOrCreate()
            
        # json_url = "https://jsonplaceholder.typicode.com/users"
        # df = spark.read.json(json_url)
        # return df.toPandas().to_dict()
    
    # @task()
    # def transform(data):
    #     spark = SparkSession.builder \
    #         .appName('TransformTask') \
    #         .master('spark://spark-master:7077') \
    #         .getOrCreate()
            
    #     df = spark.createDataFrame(data)
    #     transformed_df = df.select("id", "name", "email")
    #     return transformed_df.toPandas().to_dict()

    # @task()
    # def load(data):
    #     spark = SparkSession.builder \
    #         .appName('LoadTask') \
    #         .master('spark://spark-master:7077') \
    #         .getOrCreate()
            
    #     df = spark.createDataFrame(data)
    #     print("Final Data:")
    #     df.show()
    
    raw_data = extract()
    # clean_data = transform(raw_data)
    # load(clean_data)

dag = spark_etl()