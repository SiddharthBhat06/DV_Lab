import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
cricket_data=pd.read_csv("deliveries.csv")
sns.boxplot(data=cricket_data,x="over",y="total_runs")
plt.show()
top=cricket_data.groupby("batter")["total_runs"].sum().reset_index().sort_values(by="total_runs",ascending=False).head(10)
sns.barplot(data=top,x="total_runs",y="batter")
plt.show()

sns.countplot(data=cricket_data,x="extras_type")
plt.show()

dismissal_counts=cricket_data["dismissal_kind"].value_counts()
plt.pie(dismissal_counts)
plt.show()
