import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('DataVisualisation/house_pricing.csv', index_col=0)
df.describe()

df = df[df.columns[-15:]]
sns.heatmap(df.corr()) # corr() = corrélation
plt.show()

# Il faut garder ceux les plus dans les couleurs claires : WoodDeck, OpenPorch et SalePrice