import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('DataVisualisation/IBM_HR_ATTRITION.csv', index_col=0)
print(df.describe())

sns.lmplot(x='Attrition', y='DistanceFromHome', data=df)
plt.show()

sns.lmplot(x='Attrition', y='YearsWithCurrManager', data=df)
plt.show()