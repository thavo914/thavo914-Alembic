from sqlalchemy import create_engine, Table, MetaData, text
from sqlalchemy.orm import sessionmaker
import pandas as pd
from urllib.parse import quote_plus

# Define connection details
username = "thangvo"
password = "Thang@2024"
password_DEV = "WoKfeGkjICCvil6"

host = "10.97.11.122"
port = 3306
database = "archive_data"

# URL encode the password
encoded_password = quote_plus(password)
encoded_password_DEV = quote_plus(password_DEV)

# Define Source & Target Connections
# source_engine = create_engine(f"mysql+pymysql://{username}:{encoded_password}@{host}:{port}/{database}")
source_engine =  create_engine(f"mysql+pymysql://thangvo:{encoded_password}@10.101.150.110:3306/in")
# source_engine =  create_engine(f"mysql+pymysql://thangvo:{encoded_password}@10.101.222.10:3306/in") #STAGING

# source_engine = create_engine(f"mysql+pymysql://{username}:{encoded_password}@{host}:{port}/{database}")

target_engine = create_engine(f"mysql+pymysql://thangvo:{encoded_password_DEV}@10.97.11.122:3306/in")

metadata = MetaData()

# SELECT * FROM `in`.Staff;
# SELECT * FROM `in`.WorkPlaceChanging;
# SELECT * FROM `in`.WorkProfile;
# SELECT * FROM `in`.WorkContract;
# SELECT * FROM `in`.WorkContractAnnex;
# SELECT * FROM `in`.Org;
# SELECT * FROM `in`.OrgWorkProfile;
# SELECT * FROM `in`.StaffPhone;
# SELECT * FROM `in`.SalaryAllowances;
# SELECT * FROM `in`.AllowanceStaff;
# SELECT * FROM `in`.User;
# 'Staff', 'WorkPlaceChanging', 'WorkProfile', 'WorkContract', 'WorkContractAnnex', 'Org', 'OrgWorkProfile'


tables_to_migrate = [
    'User'
    # Add other table names here
]

for table_name in tables_to_migrate:
    try:
        print(f"Starting migration for table: {table_name}")

        table_a = Table(table_name, metadata, autoload_with=target_engine)
        backup_table_name = f"{table_name}_BK20250214"
        table_b = Table(backup_table_name, metadata, *[column.copy() for column in table_a.columns])

    # Read Data from Source
        df = pd.read_sql(f"SELECT * FROM {table_name}", source_engine)
        df1 = pd.read_sql(f"SELECT * FROM {table_name}", target_engine)
        print(f"Data read from source and target for {table_name}")
    # Write Data to Target

    # Create a session
        Session = sessionmaker(bind=target_engine)
        session = Session()

# Truncate table using raw SQL
        try:
            session.execute(text(f'SET FOREIGN_KEY_CHECKS=0'))
            session.execute(text(f'DROP TABLE IF EXISTS {backup_table_name}'))
            table_b.create(target_engine, checkfirst=True)
            df1.to_sql(backup_table_name, target_engine, if_exists="append", index=False)
            session.execute(text(f'TRUNCATE TABLE {table_name}'))
            df.to_sql(table_name, target_engine, if_exists="append", index=False)

            session.execute(text('SET FOREIGN_KEY_CHECKS=1'))

            session.commit()
            print(f"Migration completed successfully for table: {table_name}")
        except Exception as e:
            session.rollback()
            print(f"An error occurred while migrating {table_name}: {e}")
        finally:
            session.close()
    except Exception as e:
        print(f"Failed to process table {table_name}: {e}")

print("All table migrations completed!")

