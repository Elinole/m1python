import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('IBM_HR_ATTRITION.csv', index_col=0)
df.describe()

sns.catplot(x='Attrition', y='JobSatisfaction', data=df.sample(50))
plt.show()

sns.boxplot(x='Attrition', y='JobSatisfaction', data=df.sample(50))
plt.show()