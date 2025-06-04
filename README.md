# 🛡️ Fake Site Detector

**Author:** Rashitha Ashraf M  
**Project Type:** Web-based Phishing & Malicious URL Detection using Machine Learning  
**Technologies:** Python, Flask, scikit-learn, pandas, whois, HTML, CSS  
**Status:**  Completed – Ready for demonstration and deployment

---

## 📌 Project Overview

**Fake Site Detector** is a Flask-based web application that classifies any given URL as:

- ✅ **Benign** (safe)  
- ⚠️ **Malicious/Phishing** (potential threat)

It uses **machine learning** with a `Random Forest` classifier trained on URLs enriched with real-time WHOIS-based domain data and other structural features.

---

##  Features

- **Domain Age Analysis:** Uses WHOIS lookup to calculate the domain age in days.
- **Feature Extraction:** Uses:
  - URL length  
  - Presence of HTTPS  
  - Use of "@" symbol  
  - Use of hyphens  
  - Number of digits  
  - Subdomain count  
  - Presence of IP address  
  - URL entropy  
  - Domain age
- **ML Classifier:** Trained Random Forest model with 90%+ accuracy.
- **User-friendly UI:** Clean interface to enter URLs and view detection results.
- **Clear Output:**
  - ✅ Benign Site
  - ⚠️ Malicious/Phishing Site Detected

---

## Flow of Execution

1. User inputs a URL via the homepage.
2. `utils.py` extracts features from the URL.
3. WHOIS lookup determines domain age.
4. Features are passed into the trained ML model (`model.pkl`).
5. Prediction is made.
6. Result is displayed along with domain age.

---

## Project Structure

Fake-Site-Detector/
├── app.py # Flask app for routing and prediction
├── model_train.py # Script to train the ML model and save it
├── generate_url_dataset.py # Generates dataset with WHOIS-based domain age
├── utils.py # Extracts URL-based features
├── model/
│ ├── model.pkl # Saved Random Forest model
│ └── url_dataset_final.csv # Generated dataset
├── templates/
│ ├── index.html # Input form
│ └── result.html # Result display page
├── static/
│ └── style.css # CSS styling
├── requirements.txt # Dependencies list
└── README.md # You are here

Create Virtual Environment
bash
python -m venv venv
source venv/bin/activate  

Install Requirements
bash
pip install -r requirements.txt

Generate Dataset
bash
python generate_url_dataset.py

Train the Model
bash
python model_train.py

Run the Flask App
bash
python app.py

Open in Browser

Dependencies
Flask

pandas

numpy

scikit-learn

python-whois

joblib

urllib3
