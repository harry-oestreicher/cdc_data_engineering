# -*- coding: utf-8 -*-
import sys
import logging
import streamlit as st
import pandas as pd
import numpy as np


# import streamlit.components.v1 as components

# from pickle import load
from src.dataio import get_data

# from sklearn.preprocessing import StandardScaler
# from sklearn.ensemble import RandomForestRegressor

# SQL query to pull data from local source
# query_str = "SELECT * FROM DISTRICT WHERE `sitecode` = 'CH';"
# df = get_data(query_str)

# Streamlit options
st.set_page_config(layout="wide")

# # Split the data per-ticker-selection
# def splitit(col):
#     y = df[col]
#     X = df.drop(columns=col)
#     return y, X

# # Initialize these when page loads to populate objects & screen components
# ticker = 'A'
# split_by = 'MarketCap'
# y, X = splitit(split_by)
# feature_list = X.loc[X['Ticker'] == ticker].values.flatten().tolist()

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


st.markdown("# Youth Risk Behavior Survey (YRBS) Data Analysis")

with st.sidebar:
    st.subheader('Demographic Filter')
    
    gender = st.radio(
        'Gender',
        ('Female', 'Male', 'Lizard'))

    if gender == 'Lizard':
        st.write('I\'m sorry')
    else:
        st.write("Ahh a human! FINALLY!")
        
    options = st.multiselect(
        'What are your favorite colors?',
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'])
    
    st.write('You selected:', options)
    
    
#     ticker = st.selectbox('Select a ticker', df['Ticker'])

#     # Use the selected item to get the entire row
#     selected_row = df.loc[df["Ticker"] == ticker]

#     # Get the actual mcap
#     mcap = selected_row.iloc[0]['MarketCap'].astype(np.int64)

#     # Create a dictionary (for display)
#     features = X.loc[X["Ticker"] == ticker].to_dict()

#     # ...and a list for the ML UI
#     feature_list = X.loc[X["Ticker"] == ticker].values.flatten().tolist()

#     st.write(features)

# st.markdown('#### Quarterly metrics for selected ticker:')
# st.dataframe(X.loc[X["Ticker"] == ticker])

# st.markdown('#### Choose or modify Metrics')
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

# feature_list.pop(0)

# model = load(open('model/RFR_model_1.1.2.pkl', 'rb'))

# if st.button('Predict'):
#     feature_list[1] = predicted_recent_price
#     feature_list[5] = predicted_profit_margin
#     feature_list[6] = predicted_total_cash
#     feature_list[7] = predicted_total_debt
#     # feature_list[8] = predicted_outstanding_shares

#     predict_list_scaled = feature_list

#     scaler = load(open('model/RFR_scaler_1.1.2.pkl', 'rb'))
#     predict_list_scaled = scaler.transform([feature_list])
#     # st.write(predict_list_scaled)

#     prediction = model.predict(predict_list_scaled)
#     prediction = prediction[0]
#     prediction = '`$ {:,.2f}`'.format(prediction.astype(np.int64))

#     st.markdown("#### Predicted:")
#     st.write(f'{ticker} Market Cap: {prediction}')

#     st.markdown("#### Actual:")
#     st.write(f'{ticker} Market Cap: '+'`$ {:,.2f}`'.format(mcap))

st.write(gender)

def main():
    # init_df = init_data()
    return None

if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL)
    main()