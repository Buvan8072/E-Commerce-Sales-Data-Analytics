import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Data/superstore.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month_Number"] = df["Order Date"].dt.month
df["Month_Name"] = df["Order Date"].dt.month_name()

monthly_sales = (
    df.groupby(["Month_Number", "Month_Name"])["Sales"]
    .sum()
    .reset_index()
)

print(monthly_sales)

plt.figure(figsize=(10,5))

plt.plot(
    monthly_sales["Month_Name"],
    monthly_sales["Sales"],
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Trend", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True)

plt.show()