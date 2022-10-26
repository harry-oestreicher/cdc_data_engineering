# -*- coding: utf-8 -*-
import logging
import streamlit as st
from src.dataio import get_data, init_data
# import streamlit.components.v1 as components
 
# Begin Streamlit calls
st.set_page_config(layout="wide")

def main():
    #Header information 
    st.title("System Settings and Data", anchor=None)
    st.markdown("Manage database, users, etc.")
    st.markdown("---")

    btn =  st.button("View top 10 DISTRICT records")
    if btn:
        # re-initialize the database
        query_str="SELECT * FROM DISTRICT WHERE `sitecode` = 'CH' LIMIT 10;"
        df = get_data(query_str)
        
        # Display the tables
        st.write("Top 10 from Chicago Results")
        st.dataframe(df)

if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL)
    main()
