import pandas as pd
df=pd.read_csv("Data/superstore.csv")
sales_by_category = df.groupby("Category")["Sales"].sum()
print("===== Sales by Category =====")
print(sales_by_category)