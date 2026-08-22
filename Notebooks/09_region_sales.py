import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Data/superstore.csv")

region_sales = (
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print(region_sales)
plt.figure(figsize=(8,5))

region_sales.plot(
    kind="barh",
    color="purple"
)

plt.title("Total Sales by Region", fontsize=16)
plt.xlabel("Sales ($)")
plt.ylabel("Region")
plt.gca().invert_yaxis()

plt.grid(axis="x", linestyle="--", alpha=0.5)

plt.show()