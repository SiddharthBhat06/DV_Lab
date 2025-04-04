import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("cereal.csv")
nut={"calories","protein",'fat'}
for i in nut:
    sns.boxplot(x=i,y="name",data=data,color='skyblue')
    plt.show()
for i in nut:
    sns.histplot(x=i,y="name",data=data,color="skyblue")
    plt.show()

sns.barplot(data=data.sort_values(by="rating"),x="rating",y="name")
plt.show()
sns.scatterplot(data=data,x="rating",y="calories")
plt.show()

sns.lineplot(data=data,x="rating",y="calories")
plt.show()
sns.barplot(data=data,x="mfr",y="rating")
plt.show()
sns.barplot(data=data,x="mfr",y="rating")
plt.show()
