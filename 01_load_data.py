import pandas as pd
df = pd.read_csv("Data/superstore.csv")

print("===== First 5 Rows =====")
print(df.head())

print("\n===== Last 5 Rows =====")
print(df.tail())

print("\n===== Shape =====")
print(df.shape)

print("\n===== Columns =====")
print(df.columns)