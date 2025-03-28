import psycopg2
from psycopg2 import OperationalError

def test_postgres_connection():
    try:
        connection = psycopg2.connect(
            database="airflow",
            user="airflow",
            password="airflow",
            host="localhost",
            port="5432"
        )
        print("Successfully connected to PostgreSQL database!")
        
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"PostgreSQL database version: {db_version[0]}")
        
        cursor.close()
        connection.close()
        print("Database connection closed.")
        
    except OperationalError as e:
        print(f"Error connecting to PostgreSQL database: {e}")

if __name__ == "__main__":
    test_postgres_connection()