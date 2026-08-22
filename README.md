🛒 E-Commerce Sales Data Analytics

An end-to-end data analytics project using **Python, SQL Server, and Power BI** to analyze e-commerce sales, profitability, customers, products, regions, and time-based performance.

📌 Project Overview

This project analyzes an e-commerce sales dataset to identify important business trends, sales patterns, customer behavior, product performance, regional performance, and profitability.

The project follows a complete analytics workflow:

**Data → Cleaning → Python Analysis → SQL Server Analysis → Power BI Dashboard → Business Insights**

🎯 Objectives

- Analyze overall sales and profit performance
- Clean and preprocess the e-commerce dataset
- Perform exploratory data analysis using Python
- Store and analyze the cleaned data using SQL Server
- Identify top-performing products and customers
- Compare sales and profit across categories and regions
- Analyze customer segments and geographical performance
- Understand monthly, quarterly, and yearly sales trends
- Build an interactive 5-page Power BI dashboard
- Translate data into meaningful business insights

🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| 🐍 Python | Data cleaning, EDA and analysis |
| 🐼 Pandas | Data manipulation and preprocessing |
| 📊 Matplotlib | Data visualization |
| 🗄️ SQL Server | Data storage and SQL analysis |
| ⚡ SQL | Business analysis and data querying |
| 📊 Power BI | Interactive dashboard and visualization |
| 📐 DAX | Measures and business calculations |
| 📁 Excel/CSV | Dataset preparation |
| 💻 VS Code | Python development |
| 🌐 GitHub | Project documentation and version control |

📂 Project Structure

```text
E-Commerce-Sales-Data-Analytics/
│
├── Dashboard/
│   └── Dashboard.pbix
│
├── data/
│   ├── superstore.csv
│   ├── superstore_clean.csv
│   └── cleaned project data
│
├── Images/
│   ├── Executive Dashboard.png
│   ├── Product Analysis.png
│   ├── Customer Analysis Dashboard.png
│   ├── Regional Analysis Dashboard.png
│   └── Time Analysis Dashboard.png
│
├── Notebooks/
│   ├── 02_data_cleaning.py
│   ├── 05_sales_chart.py
│   ├── 08_monthly_sales.py
│   ├── 10_top_customers.py
│   └── 13_correlation_analysis.py
│
├── SQL/
│   └── SQL analysis scripts
│
├── Reports/
│   └── Project documentation
│
└── README.md

🐍 Python Analysis

Python was used for data cleaning and exploratory analysis.

Analysis performed

 * Dataset loading and validation
 * Data cleaning
 * Sales analysis
 * Profit analysis
 * Category analysis
 * Monthly sales analysis
 * Customer analysis
 * Correlation analysis
 * Data visualization using Python

Key Metrics

The cleaned dataset contains 9,994 records.

| Metric        |        Value |
| ------------- | -----------: |
| Total Sales   | 2,297,200.86 |
| Total Profit  |   286,817.02 |
| Total Records |        9,994 |

🗄️ SQL Analysis

SQL Server was used to store and analyze the Superstore dataset.

 SQL concepts implemented

 * `SELECT`
 * `WHERE`
 * `ORDER BY`
 * `DISTINCT`
 * `TOP`
 * `COUNT()`
 * `SUM()`
 * `AVG()`
 * `MIN()`
 * `MAX()`
 * `GROUP BY`
 * `HAVING`
 * Window Functions
 * `ROW_NUMBER()`
 * `RANK()`
 * `DENSE_RANK()`
 * Common Table Expressions (CTEs)

Business Analysis

SQL was used to analyze:

 * Sales by category
 * Profit by category
 * Sales by region
 * Profit by region
 * Sales by customer segment
 * Sales by shipping mode
 * Top customers
 * Top products
 * Top states
 * Top cities
 * Monthly sales
 * Product rankings

📊 Power BI Dashboard

An interactive 5-page Power BI dashboard was developed.

Page 1 — 📊 Executive Dashboard

Provides an overall view of business performance.

  * 💰 Sales
  * 📈 Profit
  * 📦 Orders
  * 🛒 Quantity
  * Sales by Region
  * Sales by Category
  * Sales by Segment
  * Monthly Sales Trend

Page 2 — 📦 Product Analysis

Analyzes product and category performance.

 * Top 10 Products
 * Sales by Sub-Category
 * Profit by Sub-Category
 * Quantity by Category

Page 3 — 👥 Customer Analysis

Analyzes customer and segment performance.

 * Top Customers
 * Sales by Segment
 * Sales by State
 * Sales by City

Page 4 — 🌍 Regional Analysis

Analyzes geographical performance.

 * Sales by Region
 * Profit by Region
 * Top States by Sales
 * Sales by City

Page 5 — 📅 Time Analysis

Analyzes performance over time.

 * Monthly Sales Trend
 * Monthly Profit Trend
 * Quarterly Sales
 * Yearly Sales

🔢 DAX Measures

The Power BI report uses measures for key business metrics, including:

 * Total Sales
 * Total Profit
 * Total Quantity
 * Total Orders
 * Average Order Value
 * Profit Margin %
 * Average Profit per Order
 * Average Quantity per Order
 * Total Discount
 * Average Discount
 * Sales per Customer

🎨 Dashboard Features

 * Interactive slicers
 * KPI cards
 * Multiple analytical visuals
 * Consistent dashboard theme
 * Page navigation buttons
 * Product, customer, regional and time analysis
 * Multi-page interactive reporting

📈 Key Business Questions Answered

The project helps answer questions such as:

1. Which category generates the highest sales?
2. Which region performs best?
3. Which products generate the most sales?
4. Which customers contribute the most revenue?
5. Which states generate the highest sales?
6. Which regions generate the highest profit?
7. How do sales change over time?
8. Which customer segment contributes the most sales?
9. Which sub-categories are most profitable?
10. Which products and customers should receive greater business attention?

💡 Key Learning Outcomes

Through this project, I gained practical experience in:

* Data cleaning and preprocessing
* Exploratory Data Analysis
* SQL querying and business analysis
* Data aggregation and grouping
* Window functions and CTEs
* DAX measures
* Interactive dashboard development
* Data visualization
* Translating data into business insights

🚀 Future Improvements

Potential future enhancements include:

* Adding more advanced DAX calculations
* Adding sales growth and year-over-year analysis
* Connecting Power BI directly to SQL Server
* Adding automated data refresh
* Adding predictive sales analysis
* Deploying the dashboard through Power BI Service

👨‍💻 Author
Bhuvanesh S
B.Tech — Artificial Intelligence & Data Science


⭐ If you find this project useful, feel free to explore the repository and connect with me.
