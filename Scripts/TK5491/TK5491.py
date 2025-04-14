import pandas as pd
import os
import sys

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from sqlalchemy import create_engine, text
from src.config.database import DatabaseConfig

def read_mapping_file(mapping_path):
    try:
        mapping_df = pd.read_excel(mapping_path)
        # print(mapping_df)
        
        return {
            row['COLUMN_NAME_VI']: {
                'name': row['COLUMN_NAME'],
                'type': row['COLUMN_TYPE']
            }
            for _, row in mapping_df.iterrows()
        }
    except Exception as e:
        print(f"Error reading mapping file: {e}")
        return {}

def convert_sql_to_pandas_type(sql_type):
    type_mapping = {
        'varchar': 'str',
        'char': 'str',
        'text': 'str',
        'date': 'datetime64[ns]',
        'datetime': 'datetime64[ns]',
        'timestamp': 'datetime64[ns]',
        'int': 'int32',
        'bigint': 'int64',
        'tinyint': 'int8',
        'smallint': 'int16',
        'mediumint': 'int32',
        'decimal': 'float64',
        'float': 'float32',
        'double': 'float64',
        'bool': 'bool',
        'boolean': 'bool'
    }
    for sql, pd_type in type_mapping.items():
        if sql in sql_type.lower():
            return pd_type
    return 'str'  # default type

def read_excel_file(file_path, mapping_path=None, sheet_name=0):
    try:
        # Load the Excel file
        xls = pd.ExcelFile(file_path)
        # Read the Excel file with specified sheet
        df = pd.read_excel(xls, sheet_name=sheet_name)




        # Print column names and data types
        print("\nColumn Names and Data Types:")
        for column in df.columns:
            print(f"{column}: {df[column].dtype}")
        # Convert data types directly
        for column in df.columns:
            try:
                if df[column].dtype == 'object':
                    df[column] = df[column].fillna('').astype(str).str.strip()
            except Exception as e:
                print(f"Warning: Could not convert column {column}: {e}")
        
        # Replace NaN values with None
        df = df.replace({pd.NA: None, pd.NaT: None})
        df = df.where(pd.notnull(df), None)
        
        return df
        
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error reading Excel file: {e}")

def update_inactive_services(df):
    try:
        db_config = DatabaseConfig()
        engine = create_engine(db_config.get_dev_kim_url('pos'))
        
        # Drop and Create table statements separated
        drop_table_query = "DROP TABLE IF EXISTS pos.TestInactiveService;"
        create_table_query = """
        CREATE TABLE IF NOT EXISTS pos.TestInactiveService (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            ServiceCode VARCHAR(50),
            CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        with engine.connect() as connection:
            connection.execute(text(drop_table_query))
            connection.execute(text(create_table_query))
            connection.commit()
            
        # Insert data
        df.to_sql(
            name='TestInactiveService',
            con=engine,
            if_exists='replace',
            index=False
        )
        
        print(f"Successfully inserted {len(df)} records")
        
        # Update Service state based on TestInactiveService
        # update_service_query = """
        # UPDATE pos.Service s
        # INNER JOIN pos.TestInactiveService tis ON s.ServiceCode = tis.ServiceCode
        # SET s.State = 0
        # WHERE s.State = 1;
        # """
        
        # with engine.connect() as connection:
        #     connection.execute(text(update_service_query))
        #     connection.execute(text(drop_table_query))
        #     connection.commit()
        #     print("Successfully updated Service states")

    except Exception as e:
        print(f"Error while inserting data: {e}")
    finally:
        engine.dispose()
        print("Database connection closed")

def update_service_name(df):
    try:
        db_config = DatabaseConfig()
        engine = create_engine(db_config.get_dev_kim_url('pos'))
        
        # Drop and Create table statements separated
        drop_table_query = "DROP TABLE IF EXISTS pos.TestRenameService;"
        create_table_query = """
        CREATE TABLE IF NOT EXISTS pos.TestRenameService (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            ServiceCode VARCHAR(50),
            DMKT VARCHAR(50),
            CurrentServiceName VARCHAR(255),
            NewServiceName VARCHAR(255),
            CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        with engine.connect() as connection:
            connection.execute(text(drop_table_query))
            connection.execute(text(create_table_query))
            connection.commit()
            
        # Insert data
        df.to_sql(
            name='TestRenameService',
            con=engine,
            if_exists='append',
            index=False
        )
        
        print(f"Successfully inserted {len(df)} records")
        
        # Update Service state based on TestInactiveService
        # update_service_query = """
        # UPDATE pos.Service s
        # INNER JOIN pos.TestRenameService tis ON s.ServiceCode = tis.ServiceCode
        # SET s.Name = tis.NewServiceName
        # WHERE s.State = 1;
        # """
        
        # with engine.connect() as connection:
        #     connection.execute(text(update_service_query))
        #     connection.execute(text(drop_table_query))
        #     connection.commit()
        #     print("Successfully updated Service states")

    except Exception as e:
        print(f"Error while inserting data: {e}")
    finally:
        engine.dispose()
        print("Database connection closed")



if __name__ == "__main__":
    excel_path_QT = os.path.join(project_root, "data", "inactive_doi-ten-dich-vu_hdyk_14-04-2025_confirm.xlsx")

    # Read specific sheet (0 = first sheet)
    df = read_excel_file(excel_path_QT, None, sheet_name='Inactive')
    # Rename columns
    column_mapping = {
        'Nhóm DMKT': 'DMKT',
        'Tên hiện tại': 'CurrentServiceName',
        'Tên mới': 'NewServiceName'
    }
    df = df.rename(columns=column_mapping)
    update_inactive_services(df)  # Uncomment if you want to insert filtered data

    df1 = read_excel_file(excel_path_QT, None, sheet_name='Đổitên')
    column_mapping_2 = {
        'Nhóm DMKT': 'DMKT',
        'Tên hiện tại': 'CurrentServiceName',
        'Tên mới': 'NewServiceName'
    }
    df1 = df1.rename(columns=column_mapping_2)
    update_service_name(df1)  # Uncomment if you want to insert filtered data

