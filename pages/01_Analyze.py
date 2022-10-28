# -*- coding: utf-8 -*-
from calendar import c
import logging
import streamlit as st
import pandas as pd
from src.dataio import init_data, enumerate_df
from src.dictionaries import *
from src.labels import survey_labels_dict



st.set_page_config(layout="wide")
st.markdown("# Youth Risk Behavior Survey (YRBS) Data Analysis")

df = None
with st.sidebar:
    # st.header('Where Sleep?')
    # st.subheader('Filter:')
    # gender = st.radio('Gender', ('Female', 'Male', 'Both'))
    # age = st.radio('Age', ("12 years old or younger", "13 years old", "14 years old", "15 years old", "16 years old", "17 years old", "18 years old or older"))

    cols = survey_labels_dict
    dist = st.radio('District:', ('NYC', 'CH', 'SF'))
    btn =  st.button(f"Initialize dataset with {dist} District results")
    if btn:
        # re-initialize the database
        df = init_data(dist)
        st.write(f"Shape: {df.shape}")
        # st.write(f"Info: {df.info}")

    # options = st.multiselect(
    #     'Which questions to focus on?',
    #     ['q30', 'q31', 'q32', 'q33', 'q34'],
    #     ['q30', 'q31'])
    
    # st.write('You selected:', options)

    # btn =  st.button("View selected dataset")
    
    # if btn:
    # selected_gender = gender
    # query_str = f"SELECT * FROM DISTRICT WHERE `age` = '{age}';"
    
    # df = get_data(query_str)
    # data = enumerate_df(enumerate_df(df, "sex", sex_dict), "age", age_dict).copy()

    # column = st.selectbox("Describe Column", list(df.columns), format_func=cols.get)
    # st.write(df[column].describe())

def main():
    
    if df is None:
        st.write("Select a District in the left sidebar.")

    if df is not None:
        st.write("Dataset head:")
        # st.dataframe(df[:5])
        demog_df = enumerate_df(enumerate_df(enumerate_df(df, "age", age_dict), "sex", sex_dict), "race7", race7_dict).copy()
        results_df = enumerate_df(enumerate_df(enumerate_df(enumerate_df(enumerate_df(demog_df, "q25", q25_dict), "q26", q26_dict), "q27", q27_dict), "q28", q28_dict), "q29", q29_dict).copy()
        #  "q16", q16_dict), "q17", q17_dict), "q18", q18_dict), "q19", q19_dict), "q20", q20_dict), "q21", q21_dict), "q22", q22_dict), "q23", q23_dict), "q24", q24_dict), "q25", q25_dict), "q26", q26_dict), "q27", q27_dict), "q28", q28_dict), "q29", q29_dict).copy()
        # selected_df = selected_df.loc["year", "age", "sex", "race7", "stweight", "stheight", "q16", "q17", "q18", "q19", "q20", "q21", "q22", "q23", "q24", "q25", "q26", "q27", "q28", "q29" ].copy()

        # enumerated_df = results_df.iloc[]

        st.dataframe(results_df)


if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL)
    main()

    # "q16": "Threatened at school",
    # "q17": "Physical fighting",
    # "q18": "Physical fighting at school",
    # "q19": "Forced sexual intercourse",

    # "q20": "Sexual violence",
    # "q21": "Sexual dating violence",
    # "q22": "Physical dating violence",
    # "q23": "Bullying at school",
    # "q24": "Electronic bullying",

    # "q25": "Sad or hopeless",
    # "q26": "Considered suicide",
    # "q27": "Made a suicide plan",
    # "q28": "Attempted suicide",
    # "q29": "Injurious suicide attempt",
