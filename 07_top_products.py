import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Data/superstore.csv")
top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(top_products)
plt.figure(figsize=(12,6))

top_products.plot(kind="bar")


plt.title("Top 10 Products by Sales", fontsize=16)
plt.xlabel("Product Name")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()
