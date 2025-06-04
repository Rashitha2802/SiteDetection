from flask import Flask, render_template, request
from utils import extract_features
import joblib
import pandas as pd
import os

app = Flask(__name__)

model_path = 'model/model.pkl'
if not os.path.exists(model_path):
    raise FileNotFoundError("Model file not found! Please train the model first using model_train.py")

model = joblib.load(model_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    features = extract_features(url)

    # Handle missing domain age (-1)
    if features['domain_age'] == -1:
        features['domain_age'] = 0  # Treat unknown domain age as suspicious

    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]
    label = '✅ Benign Site' if prediction == 0 else '⚠️ Malicious/Phishing Site Detected'

    return render_template('result.html', url=url, result=label, domain_age=features['domain_age'])

if __name__ == '__main__':
    app.run(debug=True)
