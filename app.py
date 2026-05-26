import pickle

import numpy as np
import streamlit as st


@st.cache_resource
def load_model():
    with open("build.pkl", "wb") as model_file:
        return pickle.load(model_file)


model = load_model()

st.set_page_config(page_title="Bank Loan Prediction", layout="centered")

st.title("Bank Loan Prediction")

with st.form("loan_prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Customer Age", min_value=18, max_value=100, value=30, step=1)
        dependents = st.number_input("Dependents", min_value=0, max_value=20, value=0, step=1)
        income = st.number_input("Applicant Income", min_value=0, value=5000, step=500)
        loan_amount = st.number_input("Loan Amount", min_value=0, value=100000, step=10000)
        cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900, value=700, step=1)
        tenure = st.number_input("Tenure", min_value=0, value=12, step=1)

    with col2:
        gender = st.selectbox("Gender", options=["Male", "Female"])
        married = st.selectbox("Married", options=["Yes", "No"])
        education = st.selectbox("Education", options=["Yes", "No"])
        self_employed = st.selectbox("Self Employed", options=["Yes", "No"])
        previous_loan = st.selectbox("Previous Loan Taken", options=["Yes", "No"])
        property_area = st.selectbox(
            "Property Area",
            options=["Rural", "Semiurban", "Urban"],
        )
        customer_bandwidth = st.selectbox(
            "Customer Bandwidth",
            options=["Bad", "Good", "Medium"],
        )

    submitted = st.form_submit_button("Predict Loan Status")

if submitted:
    gender_map = {"Male": 1, "Female": 0}
    yes_no_map = {"Yes": 1, "No": 0}
    property_area_map = {"Rural": 0, "Semiurban": 1, "Urban": 2}
    customer_bandwidth_map = {"Bad": 0, "Good": 1, "Medium": 2}

    features = np.array(
        [
            [
                age,
                dependents,
                income,
                loan_amount,
                cibil_score,
                tenure,
                gender_map[gender],
                yes_no_map[married],
                yes_no_map[education],
                yes_no_map[self_employed],
                yes_no_map[previous_loan],
                property_area_map[property_area],
                customer_bandwidth_map[customer_bandwidth],
            ]
        ]
    )

    prediction = model.predict(features)[0]

    if prediction == 0:
        st.error("Loan is Rejected")
    else:
        st.success("Loan is Approved")
