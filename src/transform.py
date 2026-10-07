import pandas as pd, os
os.makedirs("data/processed", exist_ok=True)

products = pd.read_csv("data/raw/products.csv")
# Create Star Schema

# Dimension: Products
dim_product = products[['id','title','category']].rename(columns={'id':'product_id'})
dim_product.to_csv("data/processed/dim_product.csv", index=False)

# Fact: Simulate sales (hard part - we generate sales)
import numpy as np
np.random.seed(42)
sales = pd.DataFrame({
    'order_id': range(1, 1001),
    'product_id': np.random.choice(dim_product['product_id'], 1000),
    'quantity': np.random.randint(1,5, 1000),
    'price': np.random.uniform(10, 500, 1000).round(2),
    'order_date': pd.date_range("2024-01-01", periods=1000).strftime("%Y-%m-%d")
})
sales['total_amount'] = sales['quantity'] * sales['price']
sales.to_csv("data/processed/fact_sales.csv", index=False)

print(f"Transformed: {len(sales)} sales, {len(dim_product)} products")
print("Data quality check: No nulls?", sales.isnull().sum().sum() == 0)
