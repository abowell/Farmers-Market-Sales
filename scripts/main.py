import pandas as pd
df = pd.read_csv("../data/sales_data.csv")

print("Accuracy Checks")
df["date"] = pd.to_datetime(df["date"])
negative_prices = (df["price"] < 0).sum()
current_date = pd.Timestamp.now()
future_date_count = (df["date"] > current_date).sum()
print(f"Negative prices: {negative_prices}")
print(f"Future dates: {future_date_count}")

print("Consistency Checks")
unique_products = df["product"].unique()
print("Unique products:", unique_products)
unique_count = df["product"].nunique()
print("Count of unique products:", unique_count)


print("Completeness Checks")
missing_values = df.isnull().sum()
completeness_rate = df.notnull().mean().mean() * 100
print(missing_values)
print(f"Overall completeness rate: {completeness_rate: .1f}%")

assert (df["price"] >= 0).all(), "Found negative prices"