import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine, Table, MetaData, text
from sqlalchemy.orm import sessionmaker
import pandas as pd
from src.config.database import DatabaseConfig
from src.utils.helpers import setup_logger, generate_backup_name

def migrate_table(table_name, source_engine, target_engine, logger):
    try:
        Session = sessionmaker(bind=target_engine)
        session = Session()
        logger.start_process(table_name)
        
        # Get table schema and create backup table
        metadata = MetaData()
        table_a = Table(table_name, metadata, autoload_with=target_engine)
        backup_name = generate_backup_name(table_name)
        
        # Create backup table with columns
        columns = []
        for column in table_a.columns:
            new_column = column._copy()
            new_column.name = column.name
            columns.append(new_column)
            
        table_b = Table(backup_name, metadata, *columns, extend_existing=True)
        
        with session.begin():
            session.execute(text('SET FOREIGN_KEY_CHECKS=0'))
            
            # Read source data
            df = pd.read_sql(f"SELECT * FROM {table_name}", source_engine)
            df1 = pd.read_sql(f"SELECT * FROM {table_name}", target_engine)
            
            # Convert timedelta columns
            for column in df.select_dtypes(include=['timedelta64[ns]']).columns:
                df[column] = df[column].astype(str)
                df[column] = df[column].apply(lambda x: str(x).split()[-1] if x is not None else None)
            for column in df1.select_dtypes(include=['timedelta64[ns]']).columns:
                df1[column] = df1[column].astype(str)
                df1[column] = df1[column].apply(lambda x: str(x).split()[-1] if x is not None else None)
            
            logger.log_progress(table_name, len(df))
            
            # Drop existing backup and create new one
            table_b.drop(target_engine, checkfirst=True)
            table_b.create(target_engine)
            
            # Backup existing data and migrate new data
            df1.to_sql(backup_name, target_engine, if_exists="append", index=False)
            session.execute(text(f'TRUNCATE TABLE {table_name}'))
            df.to_sql(table_name, target_engine, if_exists="append", index=False)
            
            session.execute(text('SET FOREIGN_KEY_CHECKS=1'))
            
        logger.end_process(table_name)
        
    except Exception as e:
        logger.end_process(table_name, success=False)
        session.execute(text('SET FOREIGN_KEY_CHECKS=1'))
        raise

def main():
    logger = setup_logger()
    config = DatabaseConfig()
    
    source_engine = create_engine(config.get_prod_kim_url())
    target_engine = create_engine(config.get_stag_kim_url())
    # tables = [ 'WorkSchedule']
    # tables = [ 'WorkShiftByWeekDay', 'WorkShiftByMonthDay', 'InfrequentExcludeWorkShift', 'InfrequentIncludeWorkShift']
    #, AbsenceRequest, AbsenceRequestDetail]
    # 'TimeKeeper',
    tables = 'WorkPlaceChanging','WorkSchedule',
    for table in tables:
        migrate_table(table, source_engine, target_engine, logger)

if __name__ == "__main__":
    main()