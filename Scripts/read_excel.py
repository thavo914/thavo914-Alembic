import pandas as pd
import os
import sys

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
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

def read_excel_file(file_path, mapping_path=None):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        if mapping_path:
            # Get column mappings from Mapping.xlsx
            column_config = read_mapping_file(mapping_path)
            # print(column_config)
            # Rename columns
            column_mappings = {k: v['name'] for k, v in column_config.items()}
            # Drop columns that are not in mapping
            columns_to_keep = list(column_mappings.keys())
            df = df[columns_to_keep]
            # Rename columns
            df = df.rename(columns=column_mappings)
            # print("\nMapped Columns and Types:")
            # for column in df.columns:
            #     print(f"{column}: {df[column].dtype}")

            # Convert data types
            for old_col, config in column_config.items():
                if config['name'] in df.columns:
                    new_col = config['name']
                    pandas_type = convert_sql_to_pandas_type(config['type'])
                    if pandas_type == 'str':
                        df[new_col] = df[new_col].fillna('').astype(str).str.strip()
                    else:
                        df[new_col] = df[new_col].astype(pandas_type)
            
            # Replace NaN values with None for non-string columns
            df = df.replace({pd.NA: None, pd.NaT: None})
            df = df.where(pd.notnull(df), None)
            
            print(df)
        
        return df
        
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error reading Excel file: {e}")

def insert_into_mysql(df):
    try:
        # Get database configuration
        db_config = DatabaseConfig()
        engine = create_engine(db_config.get_dev_kim_url())
        
        # Add Year column with default value 2024
        df['Year'] = 2025

        # Sort by StaffCode descending and limit to 5 records
        # df_limited = df.sort_values('StaffCode', ascending=False).head(5)
        # First insert the data
        df.to_sql(
            name='StaffSalaryTaxSettlement',
            con=engine,
            if_exists='append',
            index=False
        )
        
        # Update StaffId using JOIN
        with engine.connect() as connection:
            update_query = text("""
                UPDATE StaffSalaryTaxSettlement sst
                INNER JOIN Staff s ON sst.StaffCode = s.StaffCode COLLATE utf8mb4_unicode_ci
                SET sst.StaffId = s.StaffId
                WHERE sst.Year = 2025
            """)
            connection.execute(update_query)
            connection.commit()
            
        print(f"Successfully inserted and updated {len(df)} records")
            
    except Exception as e:
        print(f"Error while inserting data: {e}")
    finally:
        engine.dispose()
        print("Database connection closed")

if __name__ == "__main__":
    excel_path_QT = os.path.join(os.path.dirname(__file__), "..", "data", "PhieuQT2024_upHIS_uplai26.3.xlsx")
    excel_path_DT = os.path.join(os.path.dirname(__file__), "..", "data", "Mapping.xlsx")

    df = read_excel_file(excel_path_QT, excel_path_DT)
    insert_into_mysql(df)