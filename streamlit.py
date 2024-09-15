# app.py
import streamlit as st
import joblib
import pandas as pd

st.title("Churn Prediction App")

# Load the trained model
model = joblib.load('churn_prediction_with_logistic_reg.joblib')

# Function to make predictions
def predict_churn(data):
    features = pd.DataFrame(data, index=[0])
    prediction = model.predict(features)
    return prediction[0]

# Function to map numeric prediction to labels
def map_prediction(prediction):
    return 'Churn' if prediction == 1 else 'Not Churn'

# Streamlit app layout
st.write("Enter customer information:")

# Input fields for the features with labels
gender_label = st.selectbox("Gender", ['Female', 'Male'])
senior_citizen_label = st.selectbox("Senior Citizen", ['No', 'Yes'])
partner_label = st.selectbox("Partner", ['No', 'Yes'])
dependents_label = st.selectbox("Dependents", ['No', 'Yes'])
tenure = st.slider("Tenure (months)", 0, 72, 12)
phone_service_label = st.selectbox("Phone Service", ['No', 'Yes'])
multiple_lines_label = st.selectbox("Multiple Lines", ['No', 'Yes'])
online_security_label = st.selectbox("Online Security", ['No', 'Yes'])
online_backup_label = st.selectbox("Online Backup", ['No', 'Yes'])
device_protection_label = st.selectbox("Device Protection", ['No', 'Yes'])
tech_support_label = st.selectbox("Tech Support", ['No', 'Yes'])
streaming_tv_label = st.selectbox("Streaming TV", ['No', 'Yes'])
streaming_movies_label = st.selectbox("Streaming Movies", ['No', 'Yes'])
paperless_billing_label = st.selectbox("Paperless Billing", ['No', 'Yes'])
monthly_charges = st.slider("Monthly Charges", 0.0, 150.0, 50.0)
total_charges = st.slider("Total Charges", 0.0, 8000.0, 2000.0)

# Categorical features with boolean values
internet_service_label = st.radio("Internet Service", ['DSL', 'Fiber optic', 'No'])
contract_label = st.radio("Contract", ['Month-to-month', 'One year', 'Two year'])
payment_method_label = st.radio("Payment Method", ['Bank transfer', 'Credit card', 'Electronic check', 'Mailed check'])

# Mapping for encoding
gender_mapping = {'Female': 0, 'Male': 1}
senior_citizen_mapping = {'No': 0, 'Yes': 1}
partner_mapping = {'No': 0, 'Yes': 1}
dependents_mapping = {'No': 0, 'Yes': 1}
phone_service_mapping = {'No': 0, 'Yes': 1}
multiple_lines_mapping = {'No': 0, 'Yes': 1}
online_security_mapping = {'No': 0, 'Yes': 1}
online_backup_mapping = {'No': 0, 'Yes': 1}
device_protection_mapping = {'No': 0, 'Yes': 1}
tech_support_mapping = {'No': 0, 'Yes': 1}
streaming_tv_mapping = {'No': 0, 'Yes': 1}
streaming_movies_mapping = {'No': 0, 'Yes': 1}
paperless_billing_mapping = {'No': 0, 'Yes': 1}
internet_service_mapping = {'DSL': 0, 'Fiber optic': 1, 'No': 0}
contract_mapping = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
payment_method_mapping = {'Bank transfer': 0, 'Credit card': 1, 'Electronic check': 2, 'Mailed check': 3}

# Convert labels to encoded values
gender = gender_mapping[gender_label]
senior_citizen = senior_citizen_mapping[senior_citizen_label]
partner = partner_mapping[partner_label]
dependents = dependents_mapping[dependents_label]
phone_service = phone_service_mapping[phone_service_label]
multiple_lines = multiple_lines_mapping[multiple_lines_label]
online_security = online_security_mapping[online_security_label]
online_backup = online_backup_mapping[online_backup_label]
device_protection = device_protection_mapping[device_protection_label]
tech_support = tech_support_mapping[tech_support_label]
streaming_tv = streaming_tv_mapping[streaming_tv_label]
streaming_movies = streaming_movies_mapping[streaming_movies_label]
paperless_billing = paperless_billing_mapping[paperless_billing_label]
internet_service = internet_service_mapping[internet_service_label]
contract = contract_mapping[contract_label]
payment_method = payment_method_mapping[payment_method_label]

# here 
# Make a prediction
features = {
    'gender': gender,
    'SeniorCitizen': senior_citizen,
    'Partner': partner,
    'Dependents': dependents,
    'tenure': tenure,
    'PhoneService': phone_service,
    'MultipleLines': multiple_lines,
    'OnlineSecurity': online_security,
    'OnlineBackup': online_backup,
    'DeviceProtection': device_protection,
    'TechSupport': tech_support,
    'StreamingTV': streaming_tv,
    'StreamingMovies': streaming_movies,
    'PaperlessBilling': paperless_billing,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges,
    'InternetService_DSL': internet_service,
    'InternetService_Fiber optic': 1 if internet_service_label == 'Fiber optic' else 0,
    'InternetService_No': 1 if internet_service_label == 'No' else 0,
    'Contract_Month-to-month': 1 if contract_label == 'Month-to-month' else 0,
    'Contract_One year': 1 if contract_label == 'One year' else 0,
    'Contract_Two year': 1 if contract_label == 'Two year' else 0,
    'PaymentMethod_Bank transfer (automatic)': 1 if payment_method == 'Bank transfer' else 0,
    'PaymentMethod_Credit card (automatic)': 1 if payment_method == 'Credit card' else 0,
    'PaymentMethod_Electronic check': 1 if payment_method == 'Electronic check' else 0,
    'PaymentMethod_Mailed check': 1 if payment_method == 'Mailed check' else 0
}

if st.button("Predict"):
    prediction = predict_churn(features)
    mapped_prediction = map_prediction(prediction)
    st.success(f"The predicted churn status is: {mapped_prediction}")