import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('DataVisualisation/house_pricing.csv', index_col=0)
print(df.describe())

sns.lmplot(x='LotArea', y='SalePrice', data=df[df.LotArea<20000][df.SalePrice<500000], fit_reg=False)
plt.show()

sns.lmplot(x='LotFrontage', y='LotArea', data=df[df.LotFrontage<200][df.LotArea<100000], fit_reg=False)
plt.show()