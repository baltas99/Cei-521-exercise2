import streamlit as st
import requests
import weather
from Currency import convert_currency

weather.get_weather('Limassol')
weather.get_weather_for_city()

convert_currency()
