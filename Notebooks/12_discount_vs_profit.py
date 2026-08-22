import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Data/superstore.csv")

plt.figure(figsize=(10,6))
plt.scatter(
    df["Discount"],
    df["Profit"],
    alpha=0.5,
    color="Red"
)

plt.title("Discount vs Profit",fontsize=16)
plt.xlabel("Discount")
plt.ylabel("Profit ($)")
plt.grid(True)
plt.show()