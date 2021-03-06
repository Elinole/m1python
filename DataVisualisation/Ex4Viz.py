import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('DataVisualisation/IBM_HR_ATTRITION.csv', index_col=0)
print(df.describe())

sns.distplot(df['MonthlyIncome'][df.MonthlyIncome < 5001])
plt.show()