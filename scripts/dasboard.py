import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("data/ratail.db")

# Example: Line chart for daily revenue
query = """
SELECT date, ROUND(SUM(quantity * price), 2) AS total_revenue
FROM sales
GROUP BY date
ORDER BY date;
"""

df = pd.read_sql_query(query, conn)
conn.close()

# Plot
plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['total_revenue'], marker='o')
plt.title("Daily Revenue")
plt.xlabel("Date")
plt.ylabel("Total Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()
