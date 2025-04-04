import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
url ="https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"
data=pd.read_csv(url)
sns.histplot(x="mpg",data=data)
plt.show()

sns.boxplot(x="hp",data=data)
plt.show()

avg_mpg_by_cyl = data.groupby("cyl")["mpg"].mean().reset_index()

# Plot the average mpg by number of cylinders
sns.barplot(x="cyl", y="mpg", data=avg_mpg_by_cyl, color="purple")
plt.show()