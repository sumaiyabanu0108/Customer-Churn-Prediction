
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("churn_model.pkl")

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Churn Prediction")
st.write("Predict whether a customer is likely to leave the service.")

st.header("Enter Customer Details")

gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (Months)", 0, 72, 12)

PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox(
    "Multiple Lines", ["Yes", "No", "No phone service"]
)
InternetService = st.selectbox(
    "Internet Service", ["DSL", "Fiber optic", "No"]
)
OnlineSecurity = st.selectbox(
    "Online Security", ["Yes", "No", "No internet service"]
)
OnlineBackup = st.selectbox(
    "Online Backup", ["Yes", "No", "No internet service"]
)
DeviceProtection = st.selectbox(
    "Device Protection", ["Yes", "No", "No internet service"]
)
TechSupport = st.selectbox(
    "Tech Support", ["Yes", "No", "No internet service"]
)
StreamingTV = st.selectbox(
    "Streaming TV", ["Yes", "No", "No internet service"]
)
StreamingMovies = st.selectbox(
    "Streaming Movies", ["Yes", "No", "No internet service"]
)
Contract = st.selectbox(
    "Contract", ["Month-to-month", "One year", "Two year"]
)
PaperlessBilling = st.selectbox(
    "Paperless Billing", ["Yes", "No"]
)
PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

MonthlyCharges = st.number_input(
    "Monthly Charges", min_value=0.0, value=70.0
)
TotalCharges = st.number_input(
    "Total Charges", min_value=0.0, value=840.0
)

if st.button("Predict Churn"):

    customer = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }])

    prediction = model.predict(customer)[0]
    probability = model.predict_proba(customer)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Customer is likely to leave!")
    else:
        st.success("✅ Customer is likely to stay!")

    st.metric(
        "Churn Probability",
        f"{probability * 100:.2f}%"
    )
