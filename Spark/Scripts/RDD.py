from pyspark.sql import SparkSession
import requests
import json
# Create a SparkSession
spark = SparkSession.builder.appName('SimpleApp').getOrCreate()


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