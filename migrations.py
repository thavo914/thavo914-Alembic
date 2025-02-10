from sqlalchemy import create_engine
import pandas as pd
from urllib.parse import quote_plus

# Define connection details
username = "thangvo"
password = "Thang@2024"
host = "10.97.11.122"
port = 3306
database = "archive_data"

# URL encode the password
encoded_password = quote_plus(password)
# Define Source & Target Connections
# source_engine = create_engine(f"mysql+pymysql://{username}:{encoded_password}@{host}:{port}/{database}")
source_engine =  create_engine(f"mysql+pymysql://thangvo:{encoded_password}@10.101.150.110:3306/pos")
# source_engine = create_engine(f"mysql+pymysql://{username}:{encoded_password}@{host}:{port}/{database}")

target_engine = create_engine(f"mysql+pymysql://thangvo:{encoded_password}@10.101.222.10:3306/pos")

# Read Data from Source
df = pd.read_sql("SELECT * FROM AppointmentAppointmentLabel", source_engine)

# Write Data to Target
df.to_sql("AppointmentAppointmentLabel_2", target_engine, if_exists="append", index=False)