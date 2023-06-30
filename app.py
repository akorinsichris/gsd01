import calendar
from datetime import datetime

import streamlit as st
import pandas as pd

#------- Settings ------#
page_title = "GSD Dashboard"
layout = "wide"
#------------------

#---Drop down values -----#
years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])

@st.cache(allow_output_mutation=True)
def load_data():
  df = pd.read_csv("https://raw.githubusercontent.com/akorinsichris/gsd01/main/employe.csv")
  return df

st.set_page_config(page_title=page_title, layout=layout)
st.title(page_title)

df = load_data()
df.filter(['firstname','lastname','department','accountid'])
st.write(df)

st.sidebar.header("Time Period")
col1,col2 = st.sidebar.columns(2)
col1.selectbox("Year", years, key="year")
col2.selectbox("Month", months, key="month")
  
st.sidebar.write("Year")
st.sidebar.write("Quarter")
st.sidebar.write("Month")
st.sidebar.header("Client/Department")


