import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Data/superstore.csv")
numeric_data = df[["Sales", "Profit", "Discount", "Quantity"]]
correlation=numeric_data.corr()

plt.figure(figsize=(8,6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.show()