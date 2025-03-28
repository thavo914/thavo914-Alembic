import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from sqlalchemy import create_engine, text
from src.config.database import DatabaseConfig

def test_mssql_connection():
    try:
        db_config = DatabaseConfig()
        engine = create_engine(db_config.get_mssql_url())
        
        with engine.connect() as connection:
            result = connection.execute(text("SELECT @@VERSION"))
            version = result.fetchone()[0]
            print("Successfully connected to MSSQL Server!")
            print(f"SQL Server Version: {version}")
            
    except Exception as e:
        print(f"Connection failed: {e}")
    finally:
        if 'engine' in locals():
            engine.dispose()
            print("Connection closed")

if __name__ == "__main__":
    test_mssql_connection()