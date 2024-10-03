#PURPOSE: Automating reading CSV file scripts from a given directory and uploading them to a PostgreSQL database using SQL Alchemy 

import pandas as pd
from sqlalchemy import create_engine
import glob
import os

# Database connection parameters
username = 'postgres'  # PostgreSQL username
password =  # PostgreSQL password [This is purposely hidden for security reasons]
database = 'PokemonPowerScale'
host = 'localhost'

# Create the connection string
connection_string = f'postgresql+psycopg2://{username}:{password}@{host}/{database}'

# Create an SQLAlchemy engine
engine = create_engine(connection_string)

# Path to your CSV files
csv_files = glob.glob(r'C:\Users\ianki\Desktop\PkmnPowerScaling\pokeapi\data\v2\csv\*.csv')

for csv_file in csv_files:
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Get the table name from the filename (remove the path and .csv extension)
    table_name = os.path.basename(csv_file).replace('.csv', '')

    # Insert the DataFrame into the PostgreSQL table
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Data from {csv_file} uploaded to {table_name}.")
