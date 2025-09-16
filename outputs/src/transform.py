def basic_clean(customers, daily_sales, orders, stores):
    customers["cust_id"] = customers["cust_id"].astype("int64")
    stores["store_id"]   = stores["store_id"].astype("int64")
    orders["store_id"]   = orders["store_id"].astype("int64")
    orders["cust_id"]    = orders["cust_id"].astype("int64")
    orders["discount"]   = orders["discount"].fillna(0)
    orders_clean = orders.dropna(subset=["amount"]).copy()
    daily_sales["year"]    = daily_sales["date"].dt.year
    daily_sales["quarter"] = daily_sales["date"].dt.to_period("Q").astype(str)
    orders_clean["year"]    = orders_clean["order_date"].dt.year
    orders_clean["quarter"] = orders_clean["order_date"].dt.to_period("Q").astype(str)
    customers["join_month"] = customers["join_date"].dt.to_period("M").astype(str)
    return customers, daily_sales, orders_clean, stores


