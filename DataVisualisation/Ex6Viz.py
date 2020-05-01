import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('house_pricing.csv', index_col=0)
df.describe()

sns.heatmap(df)