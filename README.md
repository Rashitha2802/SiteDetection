Fake Site Detector
Author: Rashitha Ashraf Project Type: Web-based Phishing & Malicious URL Detection using Machine Learning
Technologies: Python, Flask, scikit-learn, pandas, whois, HTML, CSS
Status: Completed – Ready for demonstration and deployment

📌 Project Overview
Fake Site Detector is a Flask-based web application that classifies any given URL as:

✅ Benign (safe)
⚠️ Malicious/Phishing (potential threat)
It uses machine learning with a Random Forest classifier trained on URLs enriched with real-time WHOIS-based domain data and other structural features.

Features
Domain Age Analysis: Uses WHOIS lookup to calculate the domain age in days.
Feature Extraction: Uses:
URL length
Presence of HTTPS
Use of "@" symbol
Use of hyphens
Number of digits
Subdomain count
Presence of IP address
URL entropy
Domain age
ML Classifier: Trained Random Forest model with 90%+ accuracy.
User-friendly UI: Clean interface to enter URLs and view detection results.
Clear Output:
✅ Benign Site
⚠️ Malicious/Phishing Site Detected
Flow of Execution
User inputs a URL via the homepage.
utils.py extracts features from the URL.
WHOIS lookup determines domain age.
Features are passed into the trained ML model (model.pkl).
Prediction is made.
Result is displayed along with domain age.
Project Structure
image

Create Virtual Environment bash python -m venv venv source venv/bin/activate

Install Requirements bash pip install -r requirements.txt

Generate Dataset bash python generate_url_dataset.py

Train the Model bash python model_train.py

Run the Flask App bash python app.py

Open in Browser

Dependencies Flask

pandas

numpy

scikit-learn

python-whois

joblib

urllib3

Notes
Domain age lookup via WHOIS can be slow or blocked for private domains.

The model classifies URLs into only two classes: benign and malicious.

Future Enhancements
Multi-class classification (e.g., suspicious, phishing, malware)

Deep learning-based models

URL screenshot and content analysis

Real-time threat intelligence APIs

User login system to track URL history
