from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from datetime import datetime, timedelta
import sys
sys.path.append('/opt/spark/config')
from database import MYSQL_CONFIG, DEV_KIM_CONFIG, get_mysql_jdbc_url, get_kim_jdbc_url

def create_spark_session():
    return SparkSession.builder \
        .appName("TimeSalaryCalculation") \
        .config("spark.sql.sources.partitionOverwriteMode", "dynamic") \
        .getOrCreate()

def process_salary_calculation(spark, from_date, to_date):
    # Create temporary views for all required tables
    timekeeper_df = spark.read.format("jdbc") \
        .option("url", get_kim_jdbc_url('dev')) \
        .option("dbtable", "TimeKeeper") \
        .option("user", DEV_KIM_CONFIG['user']) \
        .option("password", DEV_KIM_CONFIG['password']) \
        .load()
    
    # Similar JDBC reads for other tables
    workprofile_df = spark.read.format("jdbc") \
        .option("url", get_kim_jdbc_url('dev')) \
        .option("dbtable", "WorkProfile") \
        .option("user", DEV_KIM_CONFIG['user']) \
        .option("password", DEV_KIM_CONFIG['password']) \
        .load()
    
    timekeeper_df.createOrReplaceTempView("TimeKeeper")
    
    # Similar JDBC reads for other tables (WorkProfile, WorkContract, etc.)
    workprofile_df = spark.read.format("jdbc") \
        .option("url", get_kim_jdbc_url('prod')) \
        .option("dbtable", "WorkProfile") \
        .option("user", PROD_KIM_CONFIG['user']) \
        .option("password", PROD_KIM_CONFIG['password']) \
        .load()
    
    workprofile_df.createOrReplaceTempView("WorkProfile")
    
    # Convert the original SQL logic to Spark SQL
    result_df = spark.sql("""
        WITH tempData_ListTimeKeeper AS (
            -- Convert the original temp table logic to Spark SQL
            SELECT 
                t.StaffId,
                t.WorkProfileId,
                t.Date,
                -- ... other columns
            FROM TimeKeeper t
            JOIN WorkProfile wp ON t.WorkProfileId = wp.WorkProfileId
            WHERE t.Day BETWEEN '{from_date}' AND '{to_date}'
        )
        -- Continue converting the rest of the SQL logic
        SELECT 
            s.StaffId AS 'ID Nhân viên',
            s.StaffCode AS 'Mã nhân viên',
            s.FullName AS 'Họ tên nhân viên',
            -- ... other columns and calculations
        FROM tempData_ListTimeKeeper t
        JOIN Staff s ON t.StaffId = s.StaffId
        -- ... rest of the joins and conditions
    """.format(from_date=from_date, to_date=to_date))
    
    # Write results back to MySQL using local configuration
    result_df.write \
        .format("jdbc") \
        .option("url", get_mysql_jdbc_url()) \
        .option("dbtable", "SalaryCalculationResults") \
        .option("user", MYSQL_CONFIG['user']) \
        .option("password", MYSQL_CONFIG['password']) \
        .mode("overwrite") \
        .save()

if __name__ == "__main__":
    spark = create_spark_session()
    
    # Get dates from Airflow (you'll need to pass these as arguments)
    from_date = "2024-01-01"
    to_date = "2024-01-31"
    
    process_salary_calculation(spark, from_date, to_date)
    spark.stop()