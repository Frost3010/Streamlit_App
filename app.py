import streamlit as st
import pandas as pd
import requests
import json

st.title('Loan Default Prediction App')

# Create input fields
age = st.slider('Age', min_value=20, max_value=100, value=30)
income = st.slider('Income', min_value=8000, max_value=1000000, value=50000)
emp_exp = st.slider('Employment Experience (years)', min_value=0, max_value=70, value=5)
loan_amount = st.slider('Loan Amount', min_value=500, max_value=500000, value=10000)
interest_rate = st.slider('Interest Rate', min_value=5.42, max_value=25.0, value=10.0)
percent_income = st.slider('Percent Income', min_value=0.0, max_value=0.66, value=0.1)
cred_hist_length = st.slider('Credit History Length (years)', min_value=2.0, max_value=50.0, value=5.0)
credit_score = st.slider('Credit Score', min_value=390, max_value=850, value=650)

gender = st.selectbox('Gender', options=['male', 'female'])
education = st.selectbox('Education', options=['High School', 'Bachelor', 'Master', 'Associate', 'Doctorate'])
home_ownership = st.selectbox('Home Ownership', options=['RENT', 'OWN', 'MORTGAGE', 'OTHER'])
loan_intent = st.selectbox('Loan Intent', options=['PERSONAL', 'EDUCATION', 'MEDICAL', 'VENTURE', 'HOMEIMPROVEMENT', 'DEBTCONSOLIDATION'])
previous_defaults = st.selectbox('Previous Defaults', options=['No', 'Yes'])

if st.button('Predict'):
    # Prepare the input data
    input_data = {
        "age": age,
        "income": income,
        "emp_exp": emp_exp,
        "loan_amount": loan_amount,
        "interest_rate": interest_rate,
        "percent_income": percent_income,
        "cred_hist_length": cred_hist_length,
        "credit_score": credit_score,
        "gender": gender,
        "education": education,
        "home_ownership": home_ownership,
        "loan_intent": loan_intent,
        "previous_defaults": previous_defaults
    }

    # Make a POST request to the FastAPI endpoint
    response = requests.post("http://165.22.43.24:8000/predict", json=input_data)
    
    if response.status_code == 200:
        result = response.json()
        prediction = "Approved" if result['prediction'] == 1 else "Denied"
        st.success(f"Loan Application Status: {prediction}")
    else:
        st.error("An error occurred while processing your request.")

st.write("Note: This app assumes that your FastAPI server is running on localhost:8000. Adjust the URL if needed.")
