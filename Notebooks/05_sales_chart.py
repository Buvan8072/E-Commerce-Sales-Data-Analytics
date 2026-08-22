import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/superstore.csv")
sales_by_category = df.groupby("Category")["Sales"].sum()
plt.figure(figsize=(8,5))
sales_by_category.plot(
    kind="bar",
    color=["skyblue", "orange", "green"]
)

plt.title("Total Sales by Category", fontsize=16)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()