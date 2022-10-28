# -*- coding: utf-8 -*-
import sys
import logging
import streamlit as st
import pandas as pd
import numpy as np

from src.dataio import get_data

# # Hacky css stuff
# st.write(
#     """
#     <style>
#     [data-testid="stJson"] div {
#         display: none;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

st.set_page_config(layout="wide")

st.markdown("# YRBS Data Analysis")
st.markdown("**Youth Risk Behavior Survey**")

with st.sidebar:
    st.subheader('Demographic Filter')
    
    gender = st.radio(
        'Gender',
        ('Female', 'Male', 'Lizard'))

    if gender == 'Lizard':
        st.write('hi mark :/')
    else:
        st.write("Ahh a human! FINALLY!")
        
    options = st.multiselect(
        'What are your favorite colors?',
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'])
    
    st.write('You selected:', options)
    
# st.markdown('### Choose or modify features:')
# col1, col2 = st.columns(2)
# with col1:
#     profit_margin = selected_row.iloc[0]['ProfitMargin(%)']
#     predicted_profit_margin = st.slider('Profit Margin (%)', 1, 99, int(profit_margin))
#     # outstanding_shares = selected_row.iloc[0]['OutstandingShares']
#     # predicted_outstanding_shares = st.number_input('Outstanding Shares', 0, 10000000000000, int(outstanding_shares),)
#     recent_price = selected_row.iloc[0]['RecentPrice']
#     predicted_recent_price = st.number_input('RecentPrice', 0, 1000, int(recent_price),)


# with col2:
#     total_cash = selected_row.iloc[0]['TotalCash']
#     predicted_total_cash = st.number_input('Total Cash', -10000000000000, 10000000000000, int(total_cash))
#     total_debt = selected_row.iloc[0]['TotalDebt']
#     predicted_total_debt = st.number_input('Total Debt', -10000000000000, 10000000000000, int(total_debt))


def main():
    # init_df = init_data()
    return None

if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL)
    main()