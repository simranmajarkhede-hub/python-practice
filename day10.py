import pandas as pd

sales = {
    "Order_ID": [1001,1002,1003,1004,1005,1006],
    "Product": ["Laptop","Mobile","Tablet","Laptop","Mobile","Tablet"],
    "City": ["Nagpur","Pune","Mumbai","Nagpur","Pune","Mumbai"],
    "Quantity": [2,5,3,1,4,2],
    "Price": [60000,25000,30000,62000,24000,31000]
}

df = pd.DataFrame(sales)

# Total Amount
df["Total"] = df["Quantity"] * df["Price"]

print("Sales Data")
print(df)

print("\nTotal Revenue")
print(df["Total"].sum())

print("\nAverage Price")
print(df["Price"].mean())

print("\nCity-wise Revenue")
print(df.groupby("City")["Total"].sum())

print("\nBest Selling Product")
print(df.groupby("Product")["Quantity"].sum().idxmax())

print("\nHighest Order")
print(df.loc[df["Total"].idxmax()])

print("\nLowest Order")
print(df.loc[df["Total"].idxmin()])

df.to_csv("sales_analysis_report.csv", index=False)

print("\nProject Completed Successfully!")