import streamlit as st
import numpy as np
import joblib
import tensorflow as tf

# Load model
dbscan = joblib.load("dbscan_model.pkl")
dl_model = tf.keras.models.load_model("fraud_dl_model.keras")

# Load scalers
scaler_dl = joblib.load("scaler.pkl")
scaler_dbscan = joblib.load("scaler_dbscan.pkl")

# Define input fields
st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details below to classify it as *fraudulent* or *legitimate*.")
# ✅ Fixed feature list with 30 features
features = ['Time'] + [f'V{i}' for i in range(1,29)] + ['Amount']

user_input = []

with st.form("fraud_form"):
    for feat in features:
        val = st.number_input(feat, value=0.0)
        user_input.append(val)
    model_choice = st.selectbox(
        "Choose model for prediction:",
        (
            "Deep Learning",
            "DBSCAN (Unsupervised)"
        )
    )
    submitted = st.form_submit_button("Predict")

if submitted:
    input_array = np.array(user_input).reshape(1, -1)

    if model_choice == "Deep Learning":
        scaled_input = scaler_dl.transform(input_array)
        prediction = dl_model.predict(scaled_input)
        label = "🚨 Fraud" if np.round(prediction[0][0]) == 1 else "✅ Legitimate"

    elif model_choice == "DBSCAN (Unsupervised)":
        scaled_input = scaler_dbscan.transform(input_array)
        prediction = dbscan.fit_predict(scaled_input)[0]
        label = "🚨 Fraud" if prediction == -1 else "✅ Legitimate"

        st.success(f"Prediction Result: *{label}*")
