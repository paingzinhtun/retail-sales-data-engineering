import pandas as pd

# Load data
sales_df = pd.read_csv("data/sales.csv")
products_df = pd.read_csv("data/products.csv")
stores_df = pd.read_csv("data/stores.csv")

# 1. Convert date column
sales_df['date'] = pd.to_datetime(sales_df["date"])

#2. Handle missing price
sales_df = sales_df.dropna(subset=["price"]) # or fillna() if logic exists

#3. Remove invalid foreign keys
valid_products = set(products_df["product_id"])
valid_stores = set(stores_df["store_id"])

sales_df = sales_df[sales_df['product_id'].isin(valid_products)]
sales_df = sales_df[sales_df['store_id'].isin(valid_stores)]

# 4. Drop duplicated
sales_df = sales_df.drop_duplicates()
products_df = products_df.drop_duplicates()
stores_df = stores_df.drop_duplicates()

# 5. Fix types
sales_df['quantity'] = sales_df['quantity'].astype(int)
sales_df['price'] = sales_df['price'].astype(float)

# Optional: Clean text
products_df['name'] = products_df['name'].str.strip()
products_df['category'] = products_df['category'].str.strip()

# ✅ Save cleaned files (optional)
sales_df.to_csv("data/cleaned_sales.csv", index=False)
products_df.to_csv("data/cleaned_products.csv", index=False)
stores_df.to_csv("data/cleaned_stores.csv", index=False)


print("✅ Data cleaning complete.")