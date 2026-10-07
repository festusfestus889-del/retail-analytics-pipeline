import requests, pandas as pd, os
from datetime import datetime

os.makedirs("data/raw", exist_ok=True)

# 1. Extract products
print("Extracting products...")
r = requests.get("https://fakestoreapi.com/products")
df = pd.DataFrame(r.json())
df.to_csv("data/raw/products.csv", index=False)

# 2. Extract exchange rates USD -> NGN
print("Extracting exchange rates...")
r2 = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
rates = r2.json()['rates']
pd.DataFrame([rates]).to_csv("data/raw/exchange_rates.csv", index=False)

print(f"Done! Saved {len(df)} products at {datetime.now()}")
