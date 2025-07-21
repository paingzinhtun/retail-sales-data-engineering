-- SQLite
SELECT * FROM sales LIMIT 5;

-- 🔹 1. Daily Total Sales (Revenue)
SELECT 
  date, 
  ROUND(SUM(quantity * price), 2) AS total_revenue
FROM sales
GROUP BY date
ORDER BY date;

-- 🔹 2. Total Revenue by Store
SELECT 
  s.store_id, 
  st.location, 
  ROUND(SUM(s.quantity * s.price), 2) AS store_revenue
FROM sales s
JOIN stores st ON s.store_id = st.store_id
GROUP BY s.store_id
ORDER BY store_revenue DESC;

--🔹 3. Top 5 Selling Products by Revenue
SELECT 
  p.name, 
  ROUND(SUM(s.quantity * s.price), 2) AS product_revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.name
ORDER BY product_revenue DESC
LIMIT 5;

-- 🔹 4. Category-Wise Total Sales
SELECT 
  p.category, 
  SUM(s.quantity) AS total_units_sold
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY total_units_sold DESC;

-- 🔹 5. Average Order Value Per Day
SELECT 
  date,
  ROUND(SUM(quantity * price) / COUNT(DISTINCT sale_id), 2) AS avg_order_value
FROM sales
GROUP BY date
ORDER BY date;
