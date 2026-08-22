import pandas as pd
df=pd.read_csv("Data/superstore.csv")
numeric_data=df[["Sales", "Profit", "Discount", "Quantity"]]
correlation=numeric_data.corr()

print(correlation)