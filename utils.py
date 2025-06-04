import re
from urllib.parse import urlparse
import numpy as np
import whois
from datetime import datetime

def has_ip(url):
    return int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', url)))

def url_entropy(s):
    prob = [float(s.count(c)) / len(s) for c in dict.fromkeys(list(s))]
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

def extract_features(url):
    parsed = urlparse(url)
    domain = parsed.netloc

    features = {
        'url_length': len(url),
        'has_https': int(parsed.scheme == 'https'),
        'has_at': int('@' in url),
        'has_hyphen': int('-' in url),
        'digit_count': sum(c.isdigit() for c in url),
        'subdomain_count': count_subdomains(domain),
        'has_ip': has_ip(url),
        'domain_age': get_domain_age(domain),
        'url_entropy': url_entropy(url)
    }
    return features