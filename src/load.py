import sqlite3, pandas as pd
conn = sqlite3.connect("data/processed/retail_warehouse.db")

for table in ['dim_product', 'fact_sales']:
    df = pd.read_csv(f"data/processed/{table}.csv")
    df.to_sql(table, conn, if_exists='replace', index=False)
    print(f"Loaded {table}: {len(df)} rows")

conn.close()
print("Warehouse ready!")
