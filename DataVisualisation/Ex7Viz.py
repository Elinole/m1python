# Un KPI est un indicateur-clé de performance. 
# Il permet de démontrer un fait via des données statistiques.
# Son avantage est qu'il permet en très peu de temps de prendre
# la meilleure décision pour se fixer des objectifs afin d'optimiser
# au maximum les performances. En très peu de temps, car les 
# résultats qu'il démontre sont indiscutables (on ne peut pas y 
# douter). Ils sont concrets.

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('DataVisualisation/resto.csv', index_col=0)
print(df.describe())

print(df.head(10)) # 10 premières lignes

print(df.size) # Taille du DataFrame (nombre total d'éléments)
print(len(df)) # Taille du DataSet (nombre de lignes)

print(df.columns) # Colonnes

print(df.groupby("item_name").sum().sort_values(["quantity"], ascending=False)[:1]) # Chicken Bowl est le plat le plus commandé

print(df.quantity.sum()) # Nb de commandes total

df.item_price = df.item_price.str.replace('$', '')
df.item_price = pd.to_numeric(df.item_price)
df['ca'] = (df.item_price * df.quantity)
print(df.ca.sum()) # Chiffre d'affaire

print(df.groupby('order_id').ca.sum().mean()) # Revenu moyen par commande
# mean() = Retourne la moyenne des valeurs pour l'axe demandé