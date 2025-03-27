from pyspark.sql import SparkSession
import requests
import json

# Create a SparkSession without logging configuration
spark = SparkSession.builder \
    .appName('SimpleApp') \
    .master('spark://spark-master:7077') \
    .config('spark.executor.instances', '2') \
    .config('spark.executor.memory', '2g') \
    .getOrCreate()

# Set log level
spark.sparkContext.setLogLevel("INFO")

# Read JSON from URL
json_url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(json_url)
json_data = response.json()
# Convert JSON to Spark DataFrame
users_df = spark.createDataFrame(json_data)
# Show the DataFrame
print("Users data from API:")
users_df.show(truncate=False)

# Show schema
print("\nDataFrame Schema:")
users_df.printSchema()

spark.stop()