# currency.py
import streamlit as st
import requests

# Function to check or initialize the button click state
def check_button_state(key):
    if key not in st.session_state:
        st.session_state[key] = False

def convert_currency():
    # API Key from FastForex
    api_key = "83754dc3d2-6c852bf831-s3rryq"

    # Create a text input widget for the amount to convert
    amount = st.number_input("Enter the amount to convert:", min_value=0.00, step=0.01, format="%.2f")

    # Create a selectbox for the source currency with Euro (EUR) as the default
    source_currency = st.selectbox("Select the source currency:", ["EUR", "USD", "JPY", "GBP"])

    # Create a selectbox for the target currency
    target_currency = st.selectbox("Select the target currency:", ["USD", "JPY", "EUR", "GBP"])

    # Initialize conversion click state
    check_button_state('conversion_clicked')

    # Create a button to trigger the currency conversion
    if st.button("Convert"):
        st.session_state['conversion_clicked'] = True

    if st.session_state['conversion_clicked']:
        if source_currency == target_currency:
            st.warning("Source and target currencies are the same. No conversion needed.")
        else:
            # Make a request to the FastForex API
            base_url = "https://api.fastforex.io/convert"
            params = {
                "api_key": api_key,
                "from": source_currency,
                "to": target_currency,
                "amount": amount,
            }

            response = requests.get(base_url, params=params)

            if response.status_code == 200:
                data = response.json()
                converted_amount = data["result"]
                st.success(f"{amount} {source_currency} is approximately {converted_amount} {target_currency}")
            else:
                st.error("Error while fetching data. Please check your API key and try again.")
