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
    dist = st.radio('District:', ('NYC', 'CH', 'SF', 'ALL'))
    btn =  st.button(f"Initialize dataset with {dist} District results")
    if btn:
        # re-initialize the database
        df = init_data(dist)
        # st.write(f"Shape: {df.shape}")
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


def plot_question(data, question, demog):
    label = "16 & Older Males - Sad or Hopeless?"
    data.rename(columns={question: label}, inplace=True)
    plt = "foo" #sns.histplot(y=demog, data=data, fill=True).set_ylabel(survey_labels_dict[demog], labelpad=2)
    return plt


if df is None:
    st.write("Select a District in the left sidebar.")

if df is not None:
    # st.dataframe(df[:5])
    demog_df = enumerate_df(enumerate_df(enumerate_df(df, "age", age_dict), "sex", sex_dict), "race7", race7_dict).copy()
    results_df = enumerate_df(enumerate_df(enumerate_df(enumerate_df(enumerate_df(demog_df, "q25", q25_dict), "q26", q26_dict), "q27", q27_dict), "q28", q28_dict), "q29", q29_dict).copy()
    new_df = results_df[["year", "sitecode", "age", "sex", "race7", "q25", "q26", "q27", "q28", "q29"]].copy()
    # Decided to remove these responses since the `Did not attempt suicide` responses are not used in this dataset
    new_df.drop(new_df.loc[new_df['q29'] == "Did not attempt suicide"].index, inplace=True)
    st.write(f"Shape: {new_df.shape}")
    st.dataframe(new_df)
    # Plot the question
    # plot_question(new_df, "q25","race7")






def main():

    return None

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
