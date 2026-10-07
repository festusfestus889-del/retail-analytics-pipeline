import requests, pandas as pd, os
from datetime import datetime
os.makedirs("data/raw", exist_ok=True)
print("Extracting products...")
try:
    r = requests.get("https://dummyjson.com/products?limit=100", timeout=30)
    r.raise_for_status()
    data = r.json()
    df = pd.DataFrame(data['products'])
    df.to_csv("data/raw/products.csv", index=False)
    print(f"Saved {len(df)} products")
except Exception as e:
    print(f"API failed: {e}")
    df = pd.DataFrame({'id':[1,2],'title':['P1','P2'],'category':['electronics','jewelery'],'price':[100,200]})
    df.to_csv("data/raw/products.csv", index=False)
print("Done")
