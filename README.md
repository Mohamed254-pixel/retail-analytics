# Retail Analytics — Sales KPIs & Insights

Pipeline to clean and analyze retail sales across customers, orders, and stores.  
Generates KPI tables and visualizations to understand revenue, discounts, and top stores.  

---

## Results (Plain English)

- **Revenue by Region & Quarter** → Which regions contribute most each quarter.  
- **Regional Totals** → Share of total revenue per region (%).  
- **Top 10 Stores** → Highest-revenue stores with average discounts.  
- **Customer Region Revenue** → Revenue grouped by customer’s home region (with unknowns flagged).  

📂 **Outputs**  
- `outputs/tables/` → CSVs with KPIs  
- `outputs/figures/` → charts (Revenue by Region/Quarter, Top 10 Stores)  

---

## What this project shows

- Cleaning and joining multiple datasets (customers, orders, stores, daily sales)  
- KPI reporting (regional revenue %, discounts, top stores)  
- Matplotlib charts for management-level insights  
- Reproducible with one Python script  

---

## Tech Stack

- **Python** (Pandas, Matplotlib, Pathlib)  
- **CSV/Excel** for data in/out  

---

## Repo Structure
retail-analytics/
├─ data/
│ ├─ customers.csv
│ ├─ daily_sales.csv
│ ├─ orders.csv
│ └─ stores.csv
├─ outputs/
│ ├─ tables/
│ │ ├─ regional_quarter_kpis.csv
│ │ ├─ regional_totals.csv
│ │ ├─ top_stores.csv
│ │ └─ revenue_by_customer_region.csv
│ └─ figures/
│ ├─ revenue_by_region_quarter.png
│ └─ top10_stores_revenue.png
├─ src/
│ └─ main.py
├─ requirements.txt
└─ README.md

## Quick Start

```bash
# 1) Clone
git clone https://github.com/Mohamed254-pixel/retail-analytics.git
cd retail-analytics
# 2) Create env + install
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# 3) Run pipeline
python src/main.py
Input: CSVs in data/ (customers.csv, daily_sales.csv, orders.csv, stores.csv)
Outputs: KPI CSVs in outputs/tables/, charts in outputs/figures/

How it Works
Load data: customers, daily sales, orders, stores (CSV).
Clean: fill missing discounts, drop invalid orders, extract year/quarter.

KPIs:
Regional quarterly revenue & avg discounts
Regional totals + revenue share %

Top 10 stores by revenue
Revenue grouped by customer region (with unknowns flagged)

Visuals:
Bar chart → Revenue by Region & Quarter
Horizontal bar chart → Top 10 Stores

FAQ
Can I swap in my own data? Yes — replace the CSVs in data/.
Do I need SQL? Not required; all joins/calcs are in Pandas.
Can I extend this? Yes — add more KPIs in main.py.
License? MIT recommended.
