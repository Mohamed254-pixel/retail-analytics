import pandas as pd

def regional_quarter_kpis(daily_sales):
    reg_qtr = (daily_sales.groupby(["region","quarter"], as_index=False)
               .agg(revenue=("amount","sum"), avg_discount=("discount","mean")).round(2))
    pivot = reg_qtr.pivot_table(values="revenue", index="region", columns="quarter", aggfunc="sum").fillna(0)
    reg_tot = daily_sales.groupby("region", as_index=False).agg(revenue=("amount","sum"))
    total = reg_tot["revenue"].sum()
    reg_tot["revenue_pct"] = (reg_tot["revenue"]/total*100).round(2)
    return reg_qtr, pivot, reg_tot

def top_stores(daily_sales, n=10):
    return (daily_sales.groupby(["store_id","region"], as_index=False)
            .agg(revenue=("amount","sum"), avg_discount=("discount","mean"))
            .sort_values("revenue", ascending=False).head(n))
