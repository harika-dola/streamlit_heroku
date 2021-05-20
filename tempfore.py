import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.dates as mdates
import matplotlib.dates as dates
from datetime import datetime,timedelta
st.title("TEMPERATURE FORECASTING")
st.sidebar.title("Temperature Forecasting")

st.markdown("Streamlit App to analyse the temperature readings ☔️☀️")
st.sidebar.markdown("Streamlit App to analyse the temperature readings ☔️☀️")

DATA_URL = ("/Users/harika.dola/Desktop/New folder/IOT-temp.csv")

@st.cache(persist=True)
def load_data():
    data = pd.read_csv(DATA_URL,parse_dates=['noted_date'])
    data['temp'] = pd.to_datetime(data['temp'])
    return data

data = load_data()
st.write(data)
st.sidebar.markdown("### IN/OUT Temperature analysis ")
select = st.sidebar.selectbox( 'Visualizaton type', ['Histogram', 'Pie chart'], key='1')
sentiment_count = data['out/in'].value_counts()
sentiment_count = pd.DataFrame({'out/in':sentiment_count.index, 'temp':sentiment_count.values})

if not st.sidebar.checkbox("Hide", True):
    st.markdown("### IN/OUT Temperature analysis")
    if select == "Histogram":
        fig = px.bar(sentiment_count, x='out/in', y='temp', color='temp', height=580)
        st.plotly_chart(fig)

    else:
        fig = px.pie(sentiment_count, values ='temp', names='out/in')
        st.plotly_chart(fig)

st.sidebar.subheader("Monthly-wise temperature analysis")
month = st.sidebar.slider("month of year", 1, 12)

modified_data = data[data['noted_date'].dt.month == month]

if not st.sidebar.checkbox("Close", True, key='1'):
    st.markdown ("### Temperature recordings based on  time of the day")
    st.markdown("%i temperature recordings between %i:00 and %i:00" % (len (modified_data), month,month))
    if st.sidebar.checkbox("Show raw data", False):
        st.write(modified_data)
st.sidebar.subheader ("Monthly-wise with date-wise temperature analysis")
choice = st. sidebar.multiselect('Pick Month', ('J', 'A', 'S','O','N','D'))
if len(choice) > 0:
    choice_data = data[data.month.isin(choice)]
    fig_choice1=px.histogram(choice_data, x='out/in', y='temp', histfunc='count',   height=600, width=800)
    st.plotly_chart(fig_choice1)
    fig_choice=px.histogram(choice_data, x='out/in', y='temp', histfunc='count', color='temp',   height=600, width=800)
    st.plotly_chart(fig_choice)
