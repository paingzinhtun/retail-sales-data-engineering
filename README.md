# 🛒 Retail Sales Data Pipeline & Dashboard

**A beginner-friendly Data Engineering project** built with Python, Pandas, SQLite, and Plotly Dash.  
This project demonstrates how to clean, transform, store, and visualize retail sales data end-to-end — without using any cloud tools.

---

## 📌 Project Overview

This project simulates a small-scale retail data pipeline from CSV files to a structured database and interactive dashboard. It's perfect for learning the foundational workflow of a Data Engineer:

- 🧹 Data Cleaning with Pandas  
- 🗃️ Database Loading using SQLite  
- 📊 Dashboard Visualization with Plotly Dash  

---

## 🛠 Tech Stack

| Tool         | Role                          |
|--------------|-------------------------------|
| Python       | Core scripting                |
| Pandas       | Data cleaning & transformation|
| SQLite3      | Lightweight relational DB     |
| Plotly Dash  | Web-based dashboard           |
| VS Code      | IDE for development           |

---

## 🔁 Project Workflow

### 1. 📥 Data Ingestion

- Input files: `sales.csv`, `products.csv`, `stores.csv`
- Initial inspection for nulls, duplicates, and inconsistent formats

### 2. 🧼 Data Cleaning

- Removed rows with missing or invalid data
- Converted price columns to float
- Standardized `date` fields to `YYYY-MM-DD` format
- Output: `*_cleaned.csv` files

### 3. 🗃️ SQLite Database

- Created SQLite DB: `retail.db`
- Tables:
  - `sales`
  - `products`
  - `stores`
- Inserted cleaned data into respective tables using Python’s `sqlite3` module

### 4. 📊 Dashboard (Optional but Powerful)

- Built an interactive dashboard using Plotly Dash:
  - Total sales by product
  - Sales trends over time
  - Sales by store
- Launch it by running `dashboard.py`

---

## 📁 Project Structure

retail-data-engineering/
│
├── data/
│   ├── sales.csv
│   ├── products.csv
│   ├── stores.csv
│   ├── sales_cleaned.csv
│   └── ...
│
├── db/
│   └── retail.db
│
├── scripts/
│   ├── clean_data.py
│   ├── load_to_sqlite.py
│   └── dashboard.py
│
├── README.md
└── requirements.txt


---

## 💡 What I Learned

- Building an end-to-end data pipeline
- Data cleaning techniques using Pandas
- Creating and inserting tables in SQLite
- Querying structured data with SQL
- Creating simple interactive dashboards

---

## 🚀 Next Steps

- Add logging and error handling
- Load data from API instead of CSVs
- Upgrade from SQLite to PostgreSQL
- Deploy dashboard using Streamlit Cloud or Render
- Schedule the pipeline with Airflow (advanced)

---