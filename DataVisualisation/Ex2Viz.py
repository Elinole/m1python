import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('DataVisualisation/sales_predictions.csv', index_col=0)
df.describe()

pd.to_datetime('date_block_num', unit='s')

sns.relplot(x='date_block_num', y='item_price', data=df.sample(50))
plt.show()