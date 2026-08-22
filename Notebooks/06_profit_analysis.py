import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Data/superstore.csv")
profit_by_category = df.groupby("Category")["Profit"].sum()
print(profit_by_category)
plt.figure(figsize=(8,5))

profit_by_category.plot(
    kind="bar",
    color=["skyblue", "orange", "green"]
)

plt.title("Total Profit by Category", fontsize=16)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Profit ($)", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()