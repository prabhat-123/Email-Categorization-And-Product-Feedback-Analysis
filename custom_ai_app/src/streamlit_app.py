import json
import requests
import pandas as pd
import streamlit as st

# Set Streamlit page configuration
st.set_page_config(layout="wide")

# Render the Streamlit UI
if __name__ == "__main__":
    st.write("# Product Sentiment Analyzer")  # Updated title
    user_query = st.text_area("Enter your query", height=200)  # Updated variable name for user input
    if st.button("Predict"):
        response = requests.post("http://127.0.0.1:8000/analyze_product_sentiment", data={"query": user_query})  # Updated route path
        if response.status_code == 200:
            prediction_result = response.json()
            st.write(prediction_result)
        else:
            st.write("Error: Failed to fetch results")
