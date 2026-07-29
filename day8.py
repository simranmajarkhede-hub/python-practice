import pandas as pd

sales = {
    "Date": ["2026-07-25", "2026-07-26", "2026-07-27", "2026-07-28", "2026-07-29"],
    "Sales": [25000, 30000, 28000, 35000, 40000]
}

df = pd.DataFrame(sales)

df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Day_Name"] = df["Date"].dt.day_name()

print("Sales Report")
print(df)

print("\nSales After 26 July")
print(df[df["Date"] > "2026-07-26"])

print("\nAverage Sales")
print(df["Sales"].mean())

df.to_csv("daily_sales_report.csv", index=False)

print("\nReport Saved Successfully!")