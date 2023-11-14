#Euro
import streamlit as st
import requests

def check_button_state(key):
    if key not in st.session_state:
        st.session_state[key] = False

def convert_EUR():
    check_button_state("eur_button_clicked")  # Ensure the session state key is initialized

    api_key = "83754dc3d2-6c852bf831-s3rryq"
    amount = st.number_input("Enter the amount to convert:", min_value=0.01, step=0.01, format="%.2f")
    target_currency = st.selectbox("Select the target currency:", ["USD", "JPY", "GBP"])

    if st.button("Convert EUR"):
        st.session_state["eur_button_clicked"] = True  # Update session state on button click

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

def main():
    convert_EUR()  # Calling the function inside main

if __name__ == "__main__":
    main()
