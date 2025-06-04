Fake Site Detector
Author: Rashitha Ashraf 
Project Type: Web-based Phishing & Malicious URL Detection using Machine Learning
Technologies: Python, Flask, scikit-learn, pandas, whois, HTML, CSS

Project Overview
Fake Site Detector is a Flask web application that identifies whether a given URL is benign (safe) or malicious/phishing. It leverages machine learning classification trained on a dataset of URLs characterized by domain age, URL features, and entropy.

The system extracts multiple URL features, such as:

URL length

Presence of HTTPS

Use of "@" symbol

Use of hyphens

Count of digits

Number of subdomains

Presence of IP address instead of domain name

Domain age (in days, from WHOIS data)

URL entropy (randomness of characters)

These features are used by a trained Random Forest model to predict the URL category.

Features
Domain Age Analysis: Uses WHOIS to compute the domain age in days. Unknown or unregistered domains are flagged as suspicious.

Comprehensive Feature Extraction: Multiple URL attributes and statistical measures are extracted to improve classification accuracy.

Machine Learning Model: Random Forest classifier trained on a dataset of over 500 URLs (benign and phishing) with real domain ages.

User-friendly Web Interface: Input any URL, get immediate results classifying it as benign or malicious.

Clear Classification Labels:

"Unrecognized URL" for invalid or unresolvable URLs

"Benign Site" for safe URLs

"Malicious/Phishing Site Detected" for suspicious URLs

Open Source: Entire codebase uses publicly available Python libraries without any API keys or external dependencies.

How It Works (Flow)
User inputs a URL in the web form on the homepage.

The backend extracts URL features using utils.py.

Domain age is fetched from WHOIS data; if unavailable, domain age is set to 0 (suspicious).

The feature vector is fed into a pre-trained Random Forest model (model.pkl).

The model predicts the URL class (benign or phishing).

The result is displayed along with domain age.

If URL is invalid/unrecognized, the user is prompted accordingly.

Project Structure
php
Copy
Edit
Fake-Site-Detector/
├── app.py                  # Flask app for routing and prediction
├── model_train.py          # Script to train the ML model and save it
├── generate_url_dataset.py # Script to generate and save dataset CSV with real domain ages
├── utils.py                # Feature extraction functions
├── model/                  # Folder containing model.pkl and url_dataset_final.csv
│   ├── model.pkl
│   └── url_dataset_final.csv
├── templates/
│   ├── index.html          # Home page with URL input form
│   └── result.html         # Results display page
├── static/
│   └── style.css           # CSS styling for web pages
├── README.md               # This file
└── requirements.txt        # Required Python packages
Installation & Setup
Clone the repository

bash
cd fake-site-detector
Create and activate a Python virtual environment (optional but recommended)

bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Generate dataset

This script builds the dataset model/url_dataset_final.csv combining benign and phishing URLs with domain ages.

bash
python generate_url_dataset.py
Train the model

This trains a Random Forest classifier and saves it as model/model.pkl.

bash
python model_train.py
Run the Flask app

bash
python app.py
Open your browser and visit
http://127.0.0.1:5000/

Dependencies
Flask

pandas

numpy

scikit-learn

python-whois

urllib3

joblib


Notes
The domain age feature depends on WHOIS server responses, which may sometimes be slow or unavailable, especially for new or private domains.

The model currently classifies only two classes: benign and malicious/phishing.

Dataset is synthetically generated with some real domain ages to improve model robustness.

Future Improvements
Support multi-class classification (e.g., phishing, malware, suspicious, benign)

Add URL screenshot or content analysis

Integrate real-time blacklists or external reputation APIs (with API keys)

Enhance feature extraction with NLP techniques on URL paths and parameters

Add user authentication for personalized tracking/history
