# 💳 Credit Card Fraud Detection App

This is a **web-based application** that detects **credit card fraud** using two types of models:
- A **Deep Learning (DL)** classifier
- An **Unsupervised DBSCAN** clustering model

Built with **Streamlit**, this app allows users to input transaction data and receive instant predictions on whether a transaction is **fraudulent** or **legitimate**.

---

## 🚀 Features

- Interactive form with 30+ transaction feature inputs
- Choice of prediction model:
  - ✅ Deep Learning (Supervised)
  - ✅ DBSCAN (Unsupervised anomaly detection)
- Real-time prediction with confidence
- Easy-to-use web interface

---

## 📁 File Structure
📦 project-root/
├── app.py # Streamlit application code
├── credit_card_fraud.ipynb # Data preprocessing and model training notebook
├── dbscan_model.pkl # Trained DBSCAN model
├── fraud_dl_model.keras # Trained Deep Learning model (Keras)
├── scaler.pkl # Scaler used for DL model
├── scaler_dbscan.pkl # Scaler used for DBSCAN


---

## ⚙️ Installation

1. **Clone the repository**
bash
git clone https://github.com/your-username/credit-card-fraud-detection.git
cd credit-card-fraud-detection

2. ## Install dependencies

bash
>>>pip install -r requirements.txt

Run the app

bash
>>>streamlit run app.py

✅ Requirements
Here are the major libraries used:

1. streamlit

2. numpy

3. tensorflow

4. joblib

5. scikit-learn

📊 Model Details
1. Deep Learning Classifier
Input: Scaled features (Time, V1 to V28, Amount)

Output: Probability of fraud

Model: Fully connected layers (from fraud_dl_model.keras)

2. DBSCAN (Unsupervised)
Detects outliers using density-based clustering

Transactions labeled -1 are flagged as fraud


🔐 Disclaimer
This app is for educational and demo purposes only. Real-world fraud detection systems require robust data governance, continual monitoring, and compliance with data protection regulations.

🧠 Author
Pratham Verma

Feel free to connect or suggest improvements!
