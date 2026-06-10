-- ====================================================
-- SUPERSTORE SALES ANALYSIS SQL LAYER
-- Table: sales (from SQLite database)
-- Source: superstore.csv (processed via ETL pipeline)
-- ====================================================

-- 1. TOTAL SALES (BUSINESS KPI)
SELECT SUM(Sales) AS total_sales
FROM sales;


-- 2. TOTAL NUMBER OF ORDERS
SELECT COUNT(*) AS total_orders
FROM sales;


-- 3. SALES BY CATEGORY
SELECT Category, SUM(Sales) AS total_sales
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;


-- 4. SALES BY SUB-CATEGORY
SELECT "Sub-Category", SUM(Sales) AS total_sales
FROM sales
GROUP BY "Sub-Category"
ORDER BY total_sales DESC;


-- 5. SALES BY REGION
SELECT Region, SUM(Sales) AS total_sales
FROM sales
GROUP BY Region
ORDER BY total_sales DESC;


-- 6. TOP 10 PRODUCTS BY SALES
SELECT "Product Name", SUM(Sales) AS total_sales
FROM sales
GROUP BY "Product Name"
ORDER BY total_sales DESC
LIMIT 10;


-- 7. MONTHLY SALES TREND
SELECT "Order Month", SUM(Sales) AS monthly_sales
FROM sales
GROUP BY "Order Month"
ORDER BY "Order Month";


-- 8. YEARLY SALES TREND
SELECT "Order Year", SUM(Sales) AS yearly_sales
FROM sales
GROUP BY "Order Year"
ORDER BY "Order Year";


-- 9. AVERAGE SHIPPING TIME (OPERATIONAL METRIC)
SELECT AVG("Shipping Days") AS avg_shipping_days
FROM sales;


-- 10. HIGH VALUE ORDERS COUNT
SELECT COUNT(*) AS high_value_orders
FROM sales
WHERE "High Value Order" = 'Yes';


-- 11. SALES CATEGORY DISTRIBUTION
SELECT "Sales Category", COUNT(*) AS order_count
FROM sales
GROUP BY "Sales Category";


-- 12. ESTIMATED PROFIT (SINCE NO PROFIT COLUMN)
SELECT SUM(Sales * 0.2) AS estimated_profit
FROM sales;