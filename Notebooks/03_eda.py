import pandas as pd
df = pd.read_csv("Data/superstore.csv")
print("Total Sales:",df["Sales"].sum())
print("Total Profit:",df["Profit"].sum())
print("Total Orders:",df["Order ID"].nunique())
print("Average Sales:",df["Sales"].mean())
