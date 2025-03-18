import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
import pandas as pd
from src.config.database import DatabaseConfig
from src.utils.helpers import setup_logger, generate_backup_name

def migrate_table(table_name, source_engine, target_engine, logger):
    try:
        logger.start_process(table_name)
        
        # Read source data
        df = pd.read_sql(f"SELECT * FROM {table_name}", source_engine)
        logger.log_progress(table_name, len(df))
        
        # Create backup
        backup_name = generate_backup_name(table_name)
        df.to_sql(backup_name, target_engine, if_exists="replace", index=False)
        
        # Migrate data
        df.to_sql(table_name, target_engine, if_exists="replace", index=False)
        logger.end_process(table_name)
        
    except Exception as e:
        logger.end_process(table_name, success=False)
        raise

def main():
    logger = setup_logger()
    config = DatabaseConfig()
    
    source_engine = create_engine(config.get_stag_kim_url())
    target_engine = create_engine(config.get_local_url())
    
    tables = ['TimeKeeper']
    
    for table in tables:
        migrate_table(table, source_engine, target_engine, logger)

if __name__ == "__main__":
    main()