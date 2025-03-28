import seaborn as sns
import matplotlib.pyplot as plt
data=sns.load_dataset('taxis')
sns.barplot(x='color',y='payment',data=data)
plt.show()