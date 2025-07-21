import pandas as pd

# load CSVs
sales_df = pd.read_csv("data/sales.csv")
products_df = pd.read_csv("data/products.csv")
stores_df = pd.read_csv("data/stores.csv")

# Preview Data
print("Sales Data:")
print(sales_df.head())
print(sales_df.info())

print("\nProducts Data:")
print(products_df.head())
print(products_df.info())

print("\nStores Data:")
print(stores_df.head())
print(stores_df.info())

# Check for nulls
print("\nMissing values in Sales:")
print(sales_df.isnull().sum())

# Check for unknown product_id or store_id
print("\nUnknown Product IDs in sales:")
print(set(sales_df["product_id"]) - set(products_df['product_id']))

# Check for unknown product_id pr store_id
print("\nUnknown Store IDs in sales:")
print(set(sales_df["store_id"]) - set(stores_df['store_id']))