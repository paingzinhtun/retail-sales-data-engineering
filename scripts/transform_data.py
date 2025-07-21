import sqlite3
import pandas as pd

conn = sqlite3.connect("data/retail.db")

query = """SELECT date, ROUND(SUM(quantity * price), 2) AS total_revenue FROM sales GROUP BY date;"""
df = pd.read_sql_query(query, conn)

print("Daily Revenue:")
print(df)

conn.close()
