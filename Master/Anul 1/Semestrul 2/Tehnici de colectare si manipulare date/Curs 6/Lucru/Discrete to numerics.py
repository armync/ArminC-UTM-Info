# Databricks notebook source
# MAGIC %md
# MAGIC # Reprezentarea atributelor discrete prin valori numerice

# COMMAND ----------

# MAGIC %md
# MAGIC Anumiti algoritmi de ML (Regresia liniara, Arbori de decizie) cer ca atributele de intrare sa fie numerice.

# COMMAND ----------

import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# COMMAND ----------

import matplotlib.pyplot as plt

# COMMAND ----------

import seaborn as sns

# COMMAND ----------

df = sns.load_dataset('tips')

# COMMAND ----------

df.head()

# COMMAND ----------

df.info()

# COMMAND ----------

df['time'].value_counts()

# COMMAND ----------

for column in df.columns:
    if df[column].dtype != 'float64':
        print("Nume coloana:", column)
        print(df[column].value_counts(),'\n' )

# COMMAND ----------

# MAGIC %md
# MAGIC Atributul 'sex' care are doua valori posibile, vrem sa il transformam intr-un atribut cu valori numerice.

# COMMAND ----------

df['sex'].value_counts()

# COMMAND ----------

df['sex']

# COMMAND ----------

pd.get_dummies(df['sex'])


# COMMAND ----------

pd.get_dummies(df['sex'], drop_first=True)

# COMMAND ----------

pd.get_dummies(df['sex'], prefix=True)

# COMMAND ----------

pd.get_dummies(df['sex'], prefix='sex')

# COMMAND ----------

print(pd.get_dummies(df['sex'], drop_first=True)) #se foloseste pentru a inlatura valorile redundante
print(pd.get_dummies(df['sex'], prefix=True))
print(pd.get_dummies(df['sex'], prefix='sex'))
print(pd.get_dummies(df['sex'], prefix=df['sex'].name))

# COMMAND ----------

print(pd.get_dummies(df['sex'][:10]))
print(pd.get_dummies(df['sex'][:10], drop_first=True)) 

# COMMAND ----------

# MAGIC %md
# MAGIC Vrem sa modificam mai multe coloane ale unui dataframe

# COMMAND ----------

df2 = pd.get_dummies(df, columns=['sex', 'time'])
df2

# COMMAND ----------

df2 = pd.get_dummies(df, columns=['sex', 'time'], drop_first=True)
df2

# COMMAND ----------

df = pd.get_dummies(df, columns=['sex', 'time'], drop_first=True)
df

# COMMAND ----------

df.head()

# COMMAND ----------

df = sns.load_dataset('tips')
df

# COMMAND ----------

df2 = pd.get_dummies(df)
df2

# COMMAND ----------

# MAGIC %md
# MAGIC Uneori dorim ca datele lipsa sa fie tratate direct.

# COMMAND ----------

df3 = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Green']})
df3


# COMMAND ----------

pd.get_dummies(df3)

# COMMAND ----------

df3 = pd.DataFrame({'Color': ['Red', 'Blue', None, 'Green']})
df3

# COMMAND ----------

pd.get_dummies(df3)

# COMMAND ----------

df3_dummies = pd.get_dummies(df3, dummy_na=True)
df3_dummies

# COMMAND ----------

# MAGIC %md
# MAGIC O alta functie: factorize

# COMMAND ----------

df = sns.load_dataset('tips')
df

# COMMAND ----------

pd.factorize(df['day'])

# COMMAND ----------

df['day_discrete'] = pd.factorize(df['day'])[0]
df

# COMMAND ----------

# MAGIC %md
# MAGIC Folosind codes pentru variabilele de tip categorical

# COMMAND ----------

df['time_discrete'] = df['time'].cat.codes
df

# COMMAND ----------

df['time_discrete'].value_counts()

# COMMAND ----------

df['smoker_discrete'] = df['smoker'].cat.codes
df

# COMMAND ----------

# MAGIC %md
# MAGIC Folosind functia map

# COMMAND ----------

time_map = {'Dinner': 10, 'Lunch': 11}
df['time_discrete_map'] = df['time'].map(time_map)
df

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exercitiu
# MAGIC
# MAGIC Sa se modifice in colectia de date diamonds din seaborn variabilele de tip discret in valori numerice folosind pd.get_dummies, factorize, codes, map.

# COMMAND ----------

df_ex = sns.load_dataset('diamonds')
df_ex

# COMMAND ----------

pd.get_dummies(df_ex['cut'])

# COMMAND ----------

df_ex = pd.get_dummies(df_ex, columns=['cut'])

# COMMAND ----------

df_ex

# COMMAND ----------

df_ex['clarity_discrete'] = pd.factorize(df_ex['clarity'])[0]
df_ex

# COMMAND ----------

df_ex['color_discrete'] = df_ex['color'].cat.codes
df_ex

# COMMAND ----------

df_ex

# COMMAND ----------

clarity_map = {'SI1': 7, 'SI2': 8}
df_ex['clarity_discrete_map'] = df_ex['clarity'].map(clarity_map)
df_ex