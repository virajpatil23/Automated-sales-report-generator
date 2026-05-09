import pandas as pd

df = pd.read_csv("sales_data.csv")
print(df.head())

import matplotlib.pyplot as plt
import seaborn as sns

region_sales = df.groupby("Region")["Revenue"].sum().sort_values()

plt.figure(figsize=(8,5))
sns.barplot(x=region_sales.values, y=region_sales.index)

plt.title("Revenue by Region")
plt.xlabel("Revenue")
plt.ylabel("Region")

plt.show()

product_sales = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=product_sales.values, y=product_sales.index)

plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")

plt.show()

orders = df["Product"].value_counts().head(5)

plt.figure(figsize=(6,6))
plt.pie(orders.values, labels=orders.index, autopct="%1.1f%%")

plt.title("Top Products Share")
plt.show()