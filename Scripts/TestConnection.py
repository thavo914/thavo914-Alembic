from sqlalchemy import create_engine, Table, MetaData, text
from sqlalchemy.orm import sessionmaker
import pandas as pd
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

# Load environment variables with absolute path
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(env_path, override=True)  # Add override=True to ensure values are updated

# Get connection details from .env
STAG_KIM_HOST = os.getenv('STAG_KIM_HOST')
STAG_KIM_USER = os.getenv('STAG_KIM_USER')
STAG_KIM_PASSWORD = os.getenv('STAG_KIM_PASSWORD')

DEV_KIM_HOST = os.getenv('DEV_KIM_HOST')
DEV_KIM_USER = os.getenv('DEV_KIM_USER')
DEV_KIM_PASSWORD = os.getenv('DEV_KIM_PASSWORD')

# URL encode the passwords
encoded_stag_password = quote_plus(STAG_KIM_PASSWORD)
encoded_dev_password = quote_plus(DEV_KIM_PASSWORD)

# Define Source & Target Connections
source_engine = create_engine(f"mysql+pymysql://{STAG_KIM_USER}:{encoded_stag_password}@{STAG_KIM_HOST}:3306/in")
target_engine = create_engine(f"mysql+pymysql://{DEV_KIM_USER}:{encoded_dev_password}@{DEV_KIM_HOST}:3306/in")

try:
    # Read Staff data from source (STAG)
    stag_staff = pd.read_sql("SELECT * FROM Staff", source_engine)
    # print("\nSTAG Staff Count:", len(stag_staff))
    # print("\nSTAG Staff Sample:")
    # print(stag_staff.head())

    # Read Staff data from target (DEV)
    dev_staff = pd.read_sql("SELECT * FROM Staff", target_engine)
    # print("\nDEV Staff Count:", len(dev_staff))
    # print("\nDEV Staff Sample:")
    # print(dev_staff.head())

except Exception as e:
    print(f"Error reading Staff table: {e}")
finally:
    source_engine.dispose()
    target_engine.dispose()