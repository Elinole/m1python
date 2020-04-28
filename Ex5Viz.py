import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('IBM_HR_ATTRITION.csv', index_col=0)
df.describe()

sns.lmplot(x='Attrition', y='DistanceFromHome', data=df)
plt.show()

sns.lmplot(x='Attrition', y='YearsWithCurrManager', data=df)
plt.show()