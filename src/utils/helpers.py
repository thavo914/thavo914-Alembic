import logging
from datetime import datetime
import os
import time
from typing import Dict

class ProcessLogger:
    def __init__(self):
        self.log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs')
        os.makedirs(self.log_dir, exist_ok=True)
        
        # Setup file handler
        file_handler = logging.FileHandler(os.path.join(self.log_dir, 'migration.log'))
        console_handler = logging.StreamHandler()
        
        # Setup formatters
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_formatter = logging.Formatter('%(message)s')
        
        file_handler.setFormatter(file_formatter)
        console_handler.setFormatter(console_formatter)
        
        # Setup logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
        # Process metrics
        self.start_time = None
        self.metrics: Dict[str, dict] = {}

    def start_process(self, table_name: str):
        self.start_time = time.time()
        self.metrics[table_name] = {
            'start_time': datetime.now(),
            'rows_processed': 0,
            'status': 'Started'
        }
        self.logger.info(f"\nStarting migration for table: {table_name}")

    def log_progress(self, table_name: str, rows_processed: int):
        self.metrics[table_name]['rows_processed'] = rows_processed
        self.logger.info(f"Processed {rows_processed} rows from {table_name}")

    def end_process(self, table_name: str, success: bool = True):
        end_time = time.time()
        duration = end_time - self.start_time
        status = 'Completed' if success else 'Failed'
        self.metrics[table_name]['status'] = status
        self.metrics[table_name]['duration'] = duration

        self.logger.info(
            f"\nMigration Summary for {table_name}:"
            f"\n{'='*50}"
            f"\nStatus: {status}"
            f"\nRows Processed: {self.metrics[table_name]['rows_processed']}"
            f"\nDuration: {duration:.2f} seconds"
            f"\n{'='*50}\n"
        )

def setup_logger():
    return ProcessLogger()

def generate_backup_name(table_name):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"{table_name}_BK_{timestamp}"