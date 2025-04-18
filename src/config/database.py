from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

class DatabaseConfig:
    def __init__(self):
        load_dotenv()
        
        # STAG Environment
        self.stag_kim_host = os.getenv('STAG_KIM_HOST')
        self.stag_kim_user = os.getenv('STAG_KIM_USER')
        self.stag_kim_password = quote_plus(os.getenv('STAG_KIM_PASSWORD'))
        
        self.stag_saas_host = os.getenv('STAG_SAAS_HOST')
        self.stag_saas_user = os.getenv('STAG_SAAS_USER')
        self.stag_saas_password = quote_plus(os.getenv('STAG_SAAS_PASSWORD'))
        
        # DEV Environment
        self.dev_kim_host = os.getenv('DEV_KIM_HOST')
        self.dev_kim_user = os.getenv('DEV_KIM_USER')
        self.dev_kim_password = quote_plus(os.getenv('DEV_KIM_PASSWORD'))
        
        self.dev_saas_host = os.getenv('DEV_SAAS_HOST')
        self.dev_saas_user = os.getenv('DEV_SAAS_USER')
        self.dev_saas_password = quote_plus(os.getenv('DEV_SAAS_PASSWORD'))
        
        # Local Environment
        self.local_host = os.getenv('LOCAL_MYSQL_HOST')
        self.local_port = os.getenv('LOCAL_MYSQL_PORT')
        self.local_user = os.getenv('LOCAL_MYSQL_USER')
        self.local_password = quote_plus(os.getenv('LOCAL_MYSQL_PASSWORD'))
        self.local_database = os.getenv('LOCAL_MYSQL_DATABASE')

        # PROD Environment
        self.prod_kim_host = os.getenv('PROD_KIM_HOST')
        self.prod_kim_user = os.getenv('PROD_KIM_USER')
        self.prod_kim_password = quote_plus(os.getenv('PROD_KIM_PASSWORD'))
        
        # MSSQL Configuration
        self.mssql_host = os.getenv('MSSQL_HOST')
        self.mssql_port = os.getenv('MSSQL_PORT')
        self.mssql_database = os.getenv('MSSQL_DATABASE')
        self.mssql_username = os.getenv('MSSQL_USERNAME')
        self.mssql_password = quote_plus(os.getenv('MSSQL_PASSWORD'))
        self.mssql_driver = quote_plus(os.getenv('MSSQL_DRIVER'))

    def get_stag_kim_url(self, database='in'):
        return f"mysql+pymysql://{self.stag_kim_user}:{self.stag_kim_password}@{self.stag_kim_host}:3306/{database}"
    
    def get_stag_saas_url(self, database='in'):
        return f"mysql+pymysql://{self.stag_saas_user}:{self.stag_saas_password}@{self.stag_saas_host}:3306/{database}"
    
    def get_dev_kim_url(self, database='in'):
        return f"mysql+pymysql://{self.dev_kim_user}:{self.dev_kim_password}@{self.dev_kim_host}:3306/{database}"
    
    def get_dev_saas_url(self, database='in'):
        return f"mysql+pymysql://{self.dev_saas_user}:{self.dev_saas_password}@{self.dev_saas_host}:3306/{database}"
    
    def get_local_url(self, database=None):
        db = database if database else self.local_database
        return f"mysql+pymysql://{self.local_user}:{self.local_password}@{self.local_host}:{self.local_port}/{db}"
        
    def get_prod_kim_url(self, database='in'):
        return f"mysql+pymysql://{self.prod_kim_user}:{self.prod_kim_password}@{self.prod_kim_host}:3306/{database}"
    
    def get_mssql_url(self):
        return f"mssql+pyodbc://{self.mssql_username}:{self.mssql_password}@{self.mssql_host}:{self.mssql_port}/{self.mssql_database}?driver={self.mssql_driver}"