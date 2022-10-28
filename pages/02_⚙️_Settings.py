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
    dist = st.radio('District:', ('NYC', 'CH', 'SF'))
    btn =  st.button(f"Initialize dataset with {dist} District results")
    if btn:
        # re-initialize the database
        df = init_data(dist)
        st.dataframe(df)

if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL)
    main()
