import streamlit as st
import requests
import os

# Function to check or initialize the button click state
def check_button_state():
    if 'button_clicked' not in st.session_state:
        st.session_state['button_clicked'] = False

def get_weather(city):
    check_button_state()
    if st.button(f"Get Weather for {city}"):
        st.session_state['button_clicked'] = True
        # Your existing API call logic
        api_key = "31061e71138b8a05356fba63f13034f8"
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": api_key, "units": "metric"}

        response = requests.get(url, params=params)

        if response.status_code == 200:
            weather_data = response.json()
            st.write(f"Town: {city}")
            st.write(f"Temperature: {weather_data['main']['temp']}°C")
            st.write(f"Description: {weather_data['weather'][0]['description']}")
            st.write(f"Humidity: {weather_data['main']['humidity']}%")
        else:
            st.warning(f"Failed to retrieve weather data for {city}.")
