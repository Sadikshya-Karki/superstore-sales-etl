# 📊 Superstore Sales ETL Pipeline

## 📌 Project Overview
This project is an end-to-end ETL (Extract, Transform, Load) pipeline built using Python. It processes raw retail sales data from a CSV file, cleans and transforms it, loads it into a SQLite database, and runs SQL-based analysis to generate business insights.

It demonstrates a modular data engineering workflow with validation, logging, and structured analytics.

---

## 🏗️ Project Structure

```
superstore-sales-etl/
├── data/
│   └── superstore.csv
│
├── sql/
│   └── analysis.sql
│
├── logs/
│   └── etl.log
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── validation.py
│   ├── logger.py
│   └── run_sql.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack
- Python
- Pandas
- SQLite
- SQL
- Logging

---

## 🔄 ETL Pipeline Flow

### 1. Extract
Reads `superstore.csv`, cleans column names, and loads data into a DataFrame.

### 2. Transform
- Removes duplicates  
- Handles missing values  
- Converts date columns (Order Date, Ship Date)  
- Feature engineering:
  - Order Year
  - Order Month
  - Order Day
  - Shipping Days
  - Sales Category (Low / Medium / High)
  - High Value Order flag

### 3. Validation
- Checks required columns exist:
  - Order Date
  - Ship Date
  - Sales
- Ensures data quality before processing

### 4. Load
- Loads cleaned data into SQLite database
- Database: `superstore.db`
- Table name: `sales`

### 5. SQL Analysis Layer
Business insights generated using SQL:
- Total sales
- Total orders
- Sales by category, sub-category, and region
- Top 10 products by sales
- Monthly and yearly sales trends
- Average shipping days
- High-value order count

---

## 📊 Key Business Insights
- Technology is the highest revenue category
- West region performs best in sales
- Phones and Chairs are top sub-categories
- Strong seasonal spikes in sales (Q4 highest)
- Average shipping time ~4 days
- 1000+ high-value orders identified

---

## 🚀 How to Run

### Install dependencies
pip install -r requirements.txt

### Run ETL pipeline
python main.py

### Run SQL analysis
python src/run_sql.py

---

## 📁 Database Details
- Database: `superstore.db`
- Table: `sales`
- Auto-created during ETL load step

---

## 📜 Logging
Logs are stored in:
logs/etl.log

Tracks:
- Extraction process
- Transformation steps
- Validation results
- Load status
- Pipeline execution flow

---

## 🧠 Skills Demonstrated
- ETL pipeline design
- Data cleaning & preprocessing
- Feature engineering
- Data validation
- SQL analytics
- Logging system
- Modular Python architecture

---

## 👨‍💻 Author
**Sadikshya Karki**

