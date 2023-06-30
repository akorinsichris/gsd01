import streamlit as st
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/akorinsichris/gsd01/main/employe.csv")

st.title("GSD Dashboard")

st.sidebar.header("Time Period")
st.sidebar.write("Year")
st.sidebar.write("Quarter")
st.sidebar.write("Month")
st.sidebar.header("Client/Department")
