# Retail Analytics Project

This project is a simple data pipeline for analyzing retail sales.  
It uses **Python, Pandas, and Matplotlib** to clean data, generate KPIs, and create visualizations.

---

## Project Structure
retail-analytics/
│── data/ # Sample input CSVs
│── outputs/
│ ├── tables/ # Generated KPI tables
│ └── figures/ # Charts (e.g., revenue by region/quarter)
│── src/ # Python scripts
│ ├── main.py
│ ├── transform.py
│ ├── kpis.py
│ └── io_utils.py
│── requirements.txt
│── README.md


---

## Features
- Cleans raw orders and customer data  
- Handles missing values and discounts  
- Creates regional KPI tables (quarterly revenue, discounts)  
- Exports results as CSV files  
- Generates Matplotlib charts (e.g., **Revenue by Region and Quarter**)  

---
## Installation
```bash
git clone https://github.com/your-username/retail-analytics.git
cd retail-analytics
pip install -r requirements.txt
python src/main.py
