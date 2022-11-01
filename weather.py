import pandas as pd
import streamlit as st

st.image("cloud.png")
st.title("Weather Analysis")
weather_data = pd.read_csv("weather.csv")
st.dataframe(weather_data, height=200)
st.map(weather_data)
