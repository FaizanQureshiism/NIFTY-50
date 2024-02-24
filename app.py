import streamlit as st
import pandas as pd
import numpy as np

def calculate_volatility(df):
    # Calculating Daily Returns
    df['Previous Close'] = df['Close '].shift(1)
    df['Daily Returns'] = (df['Close '] / df['Previous Close']) - 1

    # Calculating Daily Volatility
    daily_volatility = np.std(df['Daily Returns'])

    # Calculating Annualized Volatility
    length_of_data = len(df)
    annualized_volatility = daily_volatility * np.sqrt(length_of_data)

    return df['Daily Returns'], daily_volatility, annualized_volatility

def main():
    st.title("Volatility Calculator")

    # File Upload
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        # Read the data from the uploaded file
        try:
            df = pd.read_excel(uploaded_file)  # Update to 'pd.read_csv' if CSV file
        except Exception as e:
            st.error(f"Error reading the file: {e}")
            return

        # Display the raw data
        st.subheader("Raw Data")
        st.dataframe(df)

        # Calculate Volatility
        daily_returns, daily_volatility, annualized_volatility = calculate_volatility(df)

        # Display Calculations
        st.subheader("Daily Returns")
        st.write(daily_returns)

        st.subheader("Daily Volatility")
        st.write(daily_volatility)

        st.subheader("Annualized Volatility")
        st.write(annualized_volatility)

if __name__ == "__main__":
    main()
