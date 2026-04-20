import streamlit as st
import pandas as pd
import plotly.express as px #Dynamic Data Visualization tool

st.title("Cricket Info App")

def load_data(file_path):
    df=pd.read_csv(file_path)
    return df

data_path="./cricinfo.csv"

df=load_data(data_path)

st.dataframe(df)

matches=df.groupby("Country")["Matches"].sum().sort_values().reset_index()

country_match2 = df.groupby("country")["Matches"].sum().sort_values().reset_index()
st.sidebar.header("Filters")

country = st.sidebar.multiselect("Select Country", options=df["Country"].unique())
filtered_df=df[
    (df["Country"].isin(country))
]

#Metric Key Perfromance Indicator

total_runs=filtered_df["Runs"].sum()
total_matches=filtered_df["Matches"].sum()
total_hundreds=filtered_df["100"].sum()
total_sixes=filtered_df["6s"].sum()
total_player=filtered_df["Player"].nunique()

st.metric(label="Total Runs", value=total_runs)
st.metric(label="Total Matches", value=total_matches)
st.metric(label="Total Hundreds", value=total_hundreds)
st.metric(label="Total Sixes", value=total_sixes)
st.metric(label="Total Players", value=total_player)