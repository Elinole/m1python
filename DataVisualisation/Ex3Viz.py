import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('DataVisualisation/IBM_HR_ATTRITION.csv', index_col=0)
df.describe()

# sns.catplot(x='Attrition', y='JobSatisfaction', data=df.sample(50))
sns.catplot(x='Attrition', y='JobSatisfaction', data=df, kind="bar")
plt.show()

# sns.boxplot(x='Attrition', y='JobSatisfaction', data=df.sample(50))
sns.boxplot(x='Attrition', y='JobSatisfaction', data=df)
plt.show()

sns.catplot(x='TotalWorkingYears', y='Attrition', data=df)
plt.show()

df['JobSatisfaction'].describe()

# sns.catplot(x='Attrition', y='EducationField', data=df, kind='bar')
# plt.show()

df.Attrition = df.Attrition.replace(to_replace = ["Yes", "No"], value=[1,0])
sns.catplot(x='Attrition', y='EducationField', data=df, kind='bar')
plt.show()