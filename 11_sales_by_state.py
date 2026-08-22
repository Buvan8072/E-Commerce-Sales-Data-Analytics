import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/superstore.csv")
state_sales = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(state_sales)
plt.figure(figsize=(10,6))

state_sales.plot(
    kind="barh",
    color="royalblue"
)

plt.title("Top 10 States by Sales", fontsize=16)
plt.xlabel("Sales ($)")
plt.ylabel("State")
plt.gca().invert_yaxis()
plt.grid(axis="x", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()