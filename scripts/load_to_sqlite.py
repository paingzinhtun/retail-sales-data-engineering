import pandas as pd
import sqlite3

# Connect to SQLite (or create a new database)
conn = sqlite3.connect("data/ratail.db") # DB will be create if it doesn't exist
cursor = conn.cursor()

# Drop tables if they exist (clean load)
cursor.execute("DROP TABLE IF EXISTS sales")
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS stores")

# Create tables
cursor.execute("""
CREATE TABLE products(
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT
)
""")

cursor.execute("""
CREATE TABLE stores(
    store_id INTEGER PRIMARY KEY,
    location TEXT
)
""")

cursor.execute("""
CREATE TABLE sales(
    sale_id INTEGER PRIMARY KEY,
    date TEXT,
    product_id INTEGER,
    quantity INTEGER,
    price REAL,
    store_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
)
""")

# load cleaned data
sales_df = pd.read_csv("data/cleaned_sales.csv")
products_df = pd.read_csv("data/cleaned_products.csv")
stores_df = pd.read_csv("data/cleaned_stores.csv")

#Write to database
products_df.to_sql("products", conn, if_exists="append", index=False)
stores_df.to_sql("stores", conn, if_exists="append", index=False)
sales_df.to_sql("sales", conn, if_exists="append", index=False)

# Confirm success
print("✅ Data loaded into retail.db successfully.")

# Close connection
conn.commit()
conn.close()