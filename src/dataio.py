# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import streamlit as st
from src.dictionaries import *
# from csv import writer
from sqlalchemy import inspect, create_engine

# Connect to the SQL database
connection_string = 'sqlite:///data/yrbss_data.db'
engine = create_engine(connection_string)
insp = inspect(engine)
# print(insp.get_table_names())

def enumerate_df(data, col, dic):
    data=data.replace({f"{col}": dic})
    data.drop(data.loc[data[col]==0].index, inplace=True)
    data.drop(data.loc[data[col]==''].index, inplace=True)
    return data

@st.cache
def init_data(dist):
    """
    Purpose:
        Initialize system data from local CSV files for reproducability
    Input:
        None
    Output (pd.DataFrame):
        Produces pandas DataFrames and corresponding SQL tables in SQLlite db file.
    
    """
    # Re-initialize the database
    query_str = f"SELECT * FROM DISTRICT WHERE `sitecode` = '{dist}';"
    df = get_data(query_str)
    df.drop(columns=["sitetype", "sitecode", "sitename", "sitetypenum", "survyear", "record"], inplace=True)

    demographic_df = df.iloc[:,0:23].copy().dropna().reset_index(drop=True)
    responses_df = df.iloc[:,23:199].copy().dropna().reset_index(drop=True)
    df = pd.concat([demographic_df, responses_df], axis=1).dropna().reset_index(drop=True)
    df[['year', 'stratum', 'PSU', 'age', 'sex', 'grade', 'race4', 'race7', 
    'qnobese', 'qnowt', 'q66', 'q65', 'sexid', 'sexid2', 'sexpart', 'sexpart2' ]] = df[['year', 'stratum', 'PSU', 'age', 'sex', 'grade', 'race4', 'race7', 
                                                                                        'qnobese', 'qnowt', 'q66', 'q65', 'sexid', 'sexid2', 'sexpart', 'sexpart2']].astype('int64')
    # Display the tables
    # st.write("Results")
    # st.dataframe(df)
    df = enumerate_df(enumerate_df(df, "sex", sex_dict), "age", age_dict).copy()
    return df

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
