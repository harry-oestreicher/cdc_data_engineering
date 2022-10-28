# -*- coding: utf-8 -*-
import sys
import logging
import streamlit as st
from pathlib import Path

# sys.path.append("..")
from src.dataio import get_data

# import streamlit.components.v1 as components
# from sqlalchemy import inspect, create_engine

st.set_page_config(layout="wide")

def main():
    #Header information 
    st.title("System Administration", anchor=None)
    st.markdown("description coming soon.")
    st.markdown("---")
    query_str="SELECT * FROM DISTRICT WHERE `sitecode` = 'CH' LIMIT 10;"
    # df = get_data(query_str)

    # st.write("Query: `SELECT * FROM DISTRICT WHERE 'sitecode' = 'CH' LIMIT 100;`")
    # st.dataframe(df)

if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL)
    main()
