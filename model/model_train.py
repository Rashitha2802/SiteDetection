import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

dataset_path = 'model/url_dataset_final.csv'
if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"{dataset_path} not found! Run generate_url_dataset.py first.")

# Load dataset
df = pd.read_csv(dataset_path)

# Remove rows with invalid domain_age
df = df[df['domain_age'] >= 0].reset_index(drop=True)

# Split features and target
X = df.drop(columns=['url', 'type'])
y = df['type'].apply(lambda x: 0 if x == 'benign' else 1)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train model
model = RandomForestClassifier(n_estimators=200, max_depth=20, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save model
os.makedirs('model', exist_ok=True)
joblib.dump(model, 'model/model.pkl')
print("✅ Model saved as model/model.pkl")
