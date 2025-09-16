
from pathlib import Path
import pandas as pd


DATA  = Path("DATA")
OUT_T = Path("OUTPUT") / "tables"
OUT_F = Path("OUTPUT") / "figures"
OUT_T.mkdir(parents=True, exist_ok=True)
OUT_F.mkdir(parents=True, exist_ok=True)

def load_data():
    customers   = pd.read_csv(DATA / "customers.csv",   parse_dates=["join_date"])
    daily_sales = pd.read_csv(DATA / "daily_sales.csv", parse_dates=["date"])
    orders      = pd.read_csv(DATA / "orders.csv",      parse_dates=["order_date"])
    stores      = pd.read_csv(DATA / "stores.csv")
    return customers, daily_sales, orders, stores

def save_table(df: pd.DataFrame, name: str):
    (OUT_T / f"{name}.csv").parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_T / f"{name}.csv", index=False)
