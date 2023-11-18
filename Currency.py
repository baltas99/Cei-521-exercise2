import streamlit as st
import requests

def check_button_state(key):
    if key not in st.session_state:
        st.session_state[key] = False

def convert_EUR():
    check_button_state("eur_button_clicked")  # Ensure the session state key is initialized

    api_key = "847c5bfac8-916b284d26-s4bl4o"
    amount = 1  # Set amount as 1 for exchange rate retrieval
    target_currencies = ["USD", "JPY", "GBP"]

    st.session_state["eur_button_clicked"] = True  # Set the button state as pressed

    base_url = "https://api.fastforex.io/convert"

    for target_currency in target_currencies:
        params = {
            "api_key": api_key,
            "from": "EUR",
            "to": target_currency,
            "amount": amount,
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            converted_amount = data["result"]
            st.success(f"1 EUR is approximately {converted_amount} {target_currency}")
        else:
            st.error(f"Error while fetching data for {target_currency}.")

def main():
    convert_EUR()  # Calling the function inside main

if __name__ == "__main__":
    main()
