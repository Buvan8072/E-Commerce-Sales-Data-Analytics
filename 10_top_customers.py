import pandas as pd
import matplotlib.pyplot as plt

print("Program Started")

# Load dataset
df = pd.read_csv("Data/superstore.csv")

print("Dataset Loaded Successfully")

# Top 10 customers by sales
top_customers = (
    df.groupby("Customer Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(top_customers)

plt.figure(figsize=(10,6))

top_customers.plot(
    kind="barh",
    color="darkgreen"
)

plt.title("Top 10 Customers by Sales")
plt.xlabel("Sales ($)")
plt.ylabel("Customer")

plt.gca().invert_yaxis()

plt.grid(axis="x", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.show()