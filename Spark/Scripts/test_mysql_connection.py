import mysql.connector
from mysql.connector import Error

hostname = "i-ixc.h.filess.io"
database = "ThangVo_realizeper"
port = "61002"
username = "ThangVo_realizeper"
password = "ce1c6ad5c8924898d9014db8b9afd31e77682834"

try:
    connection = mysql.connector.connect(
        host=hostname,
        database=database,
        user=username,
        password=password,
        port=port
    )
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
    raise e  # Re-raise the error so Airflow can catch it
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")