import streamlit as st
import requests

def get_weather(city):
    if 'button_clicked' not in st.session_state:
        st.session_state.button_clicked = False

    if st.button(f"Get Weather for {city}") or not st.session_state.button_clicked:
        st.session_state.button_clicked = True
        
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


def get_weather_for_city():
    # Text input for city inside the function
    city = st.text_input("Enter a town name:")

    if st.button("Search") or not st.session_state.button_clicked:
        st.session_state.button_clicked = True

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









