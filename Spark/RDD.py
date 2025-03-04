import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

# Create schema for the DataFrame
schema = StructType([StructField("numbers", IntegerType(), True)])

# Set environment variables
if not os.environ.get('JAVA_OPTS'):
    os.environ['JAVA_OPTS'] = '-Djava.security.manager=allow'
os.environ['HADOOP_HOME'] = 'C:\\hadoop'
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession \
    .builder \
    .appName("Python Spark create RDD example") \
    .master("local[*]") \
    .config("spark.driver.memory", "2g") \
    .config("spark.driver.extraJavaOptions", "-Djava.security.manager=allow") \
    .config("spark.executor.extraJavaOptions", "-Djava.security.manager=allow") \
    .config("spark.python.worker.memory", "512m") \
    .config("spark.python.worker.reuse", "true") \
    .config("spark.python.worker.python", sys.executable) \
    .config("spark.hadoop.io.native.lib.available", "true") \
    .config("spark.ui.port", "4040") \
    .getOrCreate()

try:
    # Create DataFrame with proper schema
    from pyspark.sql.types import StructType, StructField, IntegerType, StringType
    import time
    schema = StructType([
        StructField("col1", IntegerType(), True),
        StructField("col2", IntegerType(), True),
        StructField("col3", IntegerType(), True),
        StructField("col4", StringType(), True)
    ])

    data = [(1, 2, 3, 'a b c'),
            (4, 5, 6, 'd e f'),
            (7, 8, 9, 'g h i')]
            
    spark.createDataFrame(data, schema).show()
    print("DataFrame created successfully")

    # Keep the session alive for UI access
    print("Session will remain active for 60 seconds...")
    time.sleep(600)
except Exception as e:
    print(f"Error: {str(e)}")
    print(f"Error type: {type(e).__name__}")
finally:
    if 'spark' in locals():
        spark.stop()
        print("Spark session stopped successfully")