import streamlit as st
import requests
import weather
from Currency import convert_EUR

weather.get_weather('Limassol')
convert_EUR()
