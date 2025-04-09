from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Local MySQL Configuration
MYSQL_CONFIG = {
    'host': os.getenv('LOCAL_MYSQL_HOST'),
    'port': int(os.getenv('LOCAL_MYSQL_PORT')),
    'database': os.getenv('LOCAL_MYSQL_DATABASE'),
    'user': os.getenv('LOCAL_MYSQL_USER'),
    'password': os.getenv('LOCAL_MYSQL_PASSWORD')
}

# SAAS Configurations
DEV_SAAS_CONFIG = {
    'host': os.getenv('DEV_SAAS_HOST'),
    'user': os.getenv('DEV_SAAS_USER'),
    'password': os.getenv('DEV_SAAS_PASSWORD')
}

STAG_SAAS_CONFIG = {
    'host': os.getenv('STAG_SAAS_HOST'),
    'user': os.getenv('STAG_SAAS_USER'),
    'password': os.getenv('STAG_SAAS_PASSWORD')
}

# KIM Configurations
DEV_KIM_CONFIG = {
    'host': os.getenv('DEV_KIM_HOST'),
    'user': os.getenv('DEV_KIM_USER'),
    'password': os.getenv('DEV_KIM_PASSWORD')
}

STAG_KIM_CONFIG = {
    'host': os.getenv('STAG_KIM_HOST'),
    'user': os.getenv('STAG_KIM_USER'),
    'password': os.getenv('STAG_KIM_PASSWORD')
}

PROD_KIM_CONFIG = {
    'host': os.getenv('PROD_KIM_HOST'),
    'user': os.getenv('PROD_KIM_USER'),
    'password': os.getenv('PROD_KIM_PASSWORD')
}

# MSSQL Configuration
MSSQL_CONFIG = {
    'host': os.getenv('MSSQL_HOST'),
    'port': int(os.getenv('MSSQL_PORT')),
    'database': os.getenv('MSSQL_DATABASE'),
    'username': os.getenv('MSSQL_USERNAME'),
    'password': os.getenv('MSSQL_PASSWORD'),
    'driver': os.getenv('MSSQL_DRIVER')
}

# Add Remote MySQL Configuration
REMOTE_MYSQL_CONFIG = {
    'host': os.getenv('REMOTE_MYSQL_HOST'),
    'port': os.getenv('REMOTE_MYSQL_PORT'),
    'database': os.getenv('REMOTE_MYSQL_DATABASE'),
    'user': os.getenv('REMOTE_MYSQL_USER'),
    'password': os.getenv('REMOTE_MYSQL_PASSWORD')
}

def get_mysql_jdbc_url():
    return f"jdbc:mysql://{MYSQL_CONFIG['host']}:{MYSQL_CONFIG['port']}/{MYSQL_CONFIG['database']}"

def get_remote_mysql_jdbc_url():
    return f"jdbc:mysql://{REMOTE_MYSQL_CONFIG['host']}:{REMOTE_MYSQL_CONFIG['port']}/{REMOTE_MYSQL_CONFIG['database']}"

def get_mssql_jdbc_url():
    return f"jdbc:sqlserver://{MSSQL_CONFIG['host']}:{MSSQL_CONFIG['port']};database={MSSQL_CONFIG['database']};trustServerCertificate=true"

def get_kim_jdbc_url(env='dev'):
    configs = {
        'dev': DEV_KIM_CONFIG,
        'stag': STAG_KIM_CONFIG,
        'prod': PROD_KIM_CONFIG
    }
    config = configs.get(env.lower())
    return f"jdbc:mysql://{config['host']}:3306" if config else None

def get_saas_jdbc_url(env='dev'):
    configs = {
        'dev': DEV_SAAS_CONFIG,
        'stag': STAG_SAAS_CONFIG
    }
    config = configs.get(env.lower())
    return f"jdbc:mysql://{config['host']}:3306" if config else None