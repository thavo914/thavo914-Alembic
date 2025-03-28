import pandas as pd
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from sqlalchemy import create_engine, text, DATE, DECIMAL, FLOAT, BIGINT, INTEGER, DATETIME, NVARCHAR
from src.config.database import DatabaseConfig

def extract_from_mysql(start_date, end_date, batch_size=1000):
    try:
        db_config = DatabaseConfig()
        mysql_engine = create_engine(db_config.get_prod_kim_url())
        
        # Execute stored procedure
        query = text("CALL pos.usp_DoctorActMaster_getDataForMSSQL(:start_date, :end_date)")
        chunks = []
        
        with mysql_engine.connect() as connection:
            result = connection.execute(
                query, 
                {"start_date": start_date, "end_date": end_date}
            )
            df = pd.DataFrame(result.fetchall())
            if not df.empty:
                df.columns = result.keys()
            
            # Convert datetime columns
            for column in df.columns:
                if df[column].dtype == 'datetime64[ns]':
                    df[column] = df[column].astype(str)
            
            print(f"Successfully extracted {len(df)} records from MySQL stored procedure")
            return df
            
    except Exception as e:
        print(f"Error during MySQL extraction: {e}")
        return None
    finally:
        mysql_engine.dispose()
        print("MySQL connection closed")

def transfer_to_mssql(df, table_name, batch_size=1000):
    try:
        db_config = DatabaseConfig()
        mssql_engine = create_engine(db_config.get_mssql_url())
        
        # Convert DataFrame data types
        df = df.astype({
            'Date': 'datetime64[ns]',
            'BranchId': 'int32',
            'OrgCode': 'str',
            'Doctor': 'int32',
            'Consult': 'int32',
            'Treatment': 'int32',
            'CVR': 'float64',
            'CVRT': 'float64',
            'CVRP': 'float64',
            'CVRI': 'float64',
            'CVRC': 'float64'
        })
        
        # Sort DataFrame by Date in ascending order
        df = df.sort_values(by='Date', ascending=True)
        
        # SQL data types
        dtypes = {col: DECIMAL(5,1) if 'CVR' in col else 
                 DATE if col == 'Date' else
                 NVARCHAR(20) if col == 'OrgCode' else
                 INTEGER for col in df.columns}
        
        print("\nColumns and their data types:")
        for col in df.columns:
            print(f"{col}: {df[col].dtype}")
        print("\nTotal columns:", len(df.columns))
        print("Total rows:", len(df))
        print("-" * 50)
        total_rows = len(df)
        for i in range(0, total_rows, batch_size):
            chunk_df = df[i:i + batch_size]
            chunk_df.to_sql(
                name=table_name,
                con=mssql_engine,
                if_exists='append',
                index=False,
                schema='dbo',
                dtype=dtypes
            )
            print(f"Transferred batch of {len(chunk_df)} records to MSSQL")
            
        print(f"Successfully transferred all {total_rows} records to MSSQL")
            
    except Exception as e:
        print(f"Error during MSSQL transfer: {e}")
    finally:
        mssql_engine.dispose()
        print("MSSQL connection closed")

if __name__ == "__main__":
    from datetime import datetime, timedelta
    
    start = datetime(2022, 1, 1)
    end = datetime.now() - timedelta(days=1)
    chunk_days = 100
    
    current = start
    while current < end:
        chunk_end = min(current + timedelta(days=chunk_days), end)
        
        print(f"\nProcessing date range: {current.date()} to {chunk_end.date()}")
        df = extract_from_mysql(
            start_date=current.strftime('%Y-%m-%d'),
            end_date=chunk_end.strftime('%Y-%m-%d')
        )
        
        if df is not None and not df.empty:
            transfer_to_mssql(df, 'DoctorActMaster')
        
        current = chunk_end + timedelta(days=1)