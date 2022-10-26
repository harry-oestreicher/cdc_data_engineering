# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pathlib import Path
from csv import writer
from sqlalchemy import inspect, create_engine

# Connect to the SQL database
connection_string = 'sqlite:///data/yrbss_data.db'
engine = create_engine(connection_string)
insp = inspect(engine)
# print(insp.get_table_names())

def init_data():
    """
    Purpose:
        Initialize system data from local CSV files for reproducability
    Input:
        None
    Output (pd.DataFrame):
        Produces pandas DataFrames and corresponding SQL tables in SQLlite db file.
    
    """
    # df = pd.read_csv(data_file, delimiter=",") #.rename(columns={"Unnamed: 0":"Ticker"})
    # df.to_sql('df', engine, if_exists='replace')
    # df.drop(columns=["sitetype", "sitetypenum", "survyear", "record"], inplace=True)
    
    # df.to_sql('df', engine, index_label="Ticker", index=False, if_exists='replace')
    # df.set_index("Ticker", inplace=True)

    return None

def get_data(query):
    """
    Purpose:
        To return a dataframe to be used on the caller's page.
    Input (Str):
        Any SQL query string to perform on db
    Returns (pd.DataFrame):
        Pandas dataframe object

    """
    df = pd.read_sql_query(query, con=engine)
    return df
