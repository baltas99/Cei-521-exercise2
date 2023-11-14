# currency.py
import streamlit as st
import requests

# Function to check or initialize the button click state
def check_button_state(key):
    if key not in st.session_state:
        st.session_state[key] = False

def convert_currency():
    api_key = "83754dc3d2-6c852bf831-s3rryq"

    amount = st.number_input("Enter the amount to convert:", min_value=0.01, step=0.01, format="%.2f")

    source_currency = st.selectbox("Select the source currency:", ["EUR", "USD", "JPY", "GBP"])

    target_currency = st.selectbox("Select the target currency:", ["USD", "JPY", "EUR", "GBP"])

    if st.button("Convert"):
        if source_currency == target_currency:
            st.warning("Source and target currencies are the same. No conversion needed.")
        else:
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
                st.error("Error while fetching data.")

def convert_EUR():
    api_key = "83754dc3d2-6c852bf831-s3rryq"
    amount = st.number_input("Enter the amount to convert:", min_value=0.01, step=0.01, format="%.2f")
    target_currency = st.selectbox("Select the target currency:", ["USD", "JPY", "GBP"])

    if st.button("Convert"):
        base_url = "https://api.fastforex.io/convert"
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
            st.success(f"{amount} EUR is approximately {converted_amount} {target_currency}")
        else:
            st.error("Error while fetching data.")

def Currency():
    st.title("Currency Converter")

    option = st.selectbox("Select Conversion Method:", ["Convert Any Currency", "Convert from EUR"])

    if option == "Convert Any Currency":
        convert_currency()
    elif option == "Convert from EUR":
        convert_EUR()

if __name__ == "__main__":
    Currency()
