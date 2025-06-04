import os
import pandas as pd
import numpy as np
import re
from urllib.parse import urlparse
import random
import string
import whois
from datetime import datetime

# Ensure model folder exists
os.makedirs('model', exist_ok=True)

def has_ip(url):
    return int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', url)))

def url_entropy(s):
    prob = [float(s.count(c))/len(s) for c in dict.fromkeys(list(s))]
    entropy = -sum([p * np.log2(p) for p in prob])
    return entropy

def count_subdomains(domain):
    parts = domain.split('.')
    return max(len(parts) - 2, 0)

def get_domain_age(domain):
    try:
        w = whois.whois(domain)
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if creation_date:
            return (datetime.now() - creation_date).days
    except:
        return -1
    return -1

def generate_features(url, label):
    parsed = urlparse(url)
    domain = parsed.netloc
    return {
        'url': url,
        'url_length': len(url),
        'has_https': int(parsed.scheme == 'https'),
        'has_at': int('@' in url),
        'has_hyphen': int('-' in url),
        'digit_count': sum(c.isdigit() for c in url),
        'subdomain_count': count_subdomains(domain),
        'has_ip': has_ip(url),
        'domain_age': get_domain_age(domain),
        'url_entropy': url_entropy(url),
        'type': label
    }

benign_urls = [
    'https://www.google.com',
    'https://www.facebook.com',
    'https://www.amazon.com',
    'https://www.wikipedia.org',
    'https://www.youtube.com',
    'https://www.linkedin.com',
    'https://www.twitter.com',
    'https://www.microsoft.com',
    'https://www.apple.com',
    'https://www.netflix.com'
]

def generate_phishing_url():
    protocol = random.choice(['http', 'https'])
    subdomains = ['login', 'secure', 'account', 'update', 'web', 'service']
    domain = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(5, 10)))
    subdomain = random.choice(subdomains)
    tld = random.choice(['com', 'net', 'org', 'info', 'biz'])
    url = f"{protocol}://{subdomain}.{domain}.{tld}/"
    if random.random() > 0.7:
        url = url.replace("://", "://user@")
    if random.random() > 0.6:
        url = url.replace(domain, domain + '-secure')
    return url

data = []

for _ in range(200):
    base_url = random.choice(benign_urls)
    if random.random() > 0.5:
        base_url += "/path" + str(random.randint(1, 100))
    if random.random() > 0.7:
        base_url += "?id=" + str(random.randint(1000, 9999))
    data.append((base_url, 'benign'))

for _ in range(300):
    data.append((generate_phishing_url(), 'phishing'))

print("⏳ Generating dataset with real domain ages...")

df = pd.DataFrame([generate_features(url, label) for url, label in data])

# ✅ Save as new name
df.to_csv("model/url_dataset_final.csv", index=False)
print("✅ Dataset saved at model/url_dataset_final.csv with shape:", df.shape)
