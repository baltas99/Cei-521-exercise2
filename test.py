import streamlit as st
import requests
import weather
from Currency import convert_EUR

#functions
st.header("Limassol Weather")
weather.get_weather('Limassol')

st.header("Euro Forex Exchange")
convert_EUR()
