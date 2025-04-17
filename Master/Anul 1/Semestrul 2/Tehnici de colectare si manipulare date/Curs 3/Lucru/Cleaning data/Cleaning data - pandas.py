# Databricks notebook source
# MAGIC %md
# MAGIC # Cleaning data cu pandas
# MAGIC
# MAGIC
# MAGIC + Identificarea datelor lipsa si tratarea acestora 
# MAGIC + identificarea si corectarea erorilor in colectia de date
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC + # Identificarea datelor lipsa

# COMMAND ----------

import pandas as pd
import numpy as np
import matplotlib as plt

# COMMAND ----------

df = pd.DataFrame({'x': [ 1, 6, 9 , 0 ], 'y': [3, np.nan, 8, 2], 'z':['T', np.nan, 'F', 'F'], 't':[5,8, 4, None]})
df

# COMMAND ----------

df.info()

# COMMAND ----------

print(df.isnull()) # sau df.isna() sau pd.isnull(df) (na = not-available). La fel pentru functia inversa: notnull() respectiv notna()
print(df.isna())
print(pd.isnull(df))
print(pd.isna(df))
print(pd.notnull(df))
print(df.isnull())

# COMMAND ----------

print(df)
print('\n')
print(df['y'][df['y'].notnull()])

# COMMAND ----------

print(df.isnull().sum()) # Coloanele cu suma 0 nu au elemente lipsa; cele cu suma nenula au elemente lipsa
print(df.count()) # returneaza nr nenule de pe coloana respectiva

# COMMAND ----------

df.notnull().sum()

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ex. 1

# COMMAND ----------

# MAGIC %md
# MAGIC Am creat un csv cu o bd f mica ex1_bd.csv si cu elemente lipsa. Importati baza de date si scrieti 3 instructiuni diferite prin care puteti sa identificati care sunt coloanele cu elemente lipsa

# COMMAND ----------

df_ex1 = pd.read_csv('ex1_bd.csv', sep=';')


# COMMAND ----------

df_ex1.isnull().sum()

# COMMAND ----------

df_ex1.isnull().any()

# COMMAND ----------

df_ex1.info()

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC
# MAGIC + # Tratarea datelor lipsa
# MAGIC
# MAGIC Metode:
# MAGIC
# MAGIC - inlocuirea datelor lipsa 
# MAGIC         - cu o valoare scalara - functia **fillna()**
# MAGIC         - cu valoarea urmatoarea sau anterioara: fill - forward - functia **ffill()** sau backward - functia **bfill()**
# MAGIC         - cu Mean, Median sau Mode - functia **fillna()**
# MAGIC         * Mean = medie - pentru tipul numeric
# MAGIC         * Median = mediana - pentru tipul numeric
# MAGIC         * Mode = valoarea care apare cel mai frecvent - pentru tipul object
# MAGIC - stergerea liniilor sau coloanelor care contin date lipsa - functia **dropna()**

# COMMAND ----------

# MAGIC %md
# MAGIC ### Inlocuirea datelor lipsa

# COMMAND ----------

df

# COMMAND ----------

print(df)

m = df['y'].mean()
print(m)

df['y'].fillna(m, inplace=True)
print(df)

# COMMAND ----------

print(df['z'].ffill()) # back- fill functioneaza si ffill() adica forward fill
df

# COMMAND ----------

descriere = df.describe()
print(descriere.loc['mean'])
print(df.describe())

# COMMAND ----------

print(df.fillna(descriere.loc['mean']))
print(df.fillna(df.mean(numeric_only=True)))
df.mean(numeric_only=True)

# COMMAND ----------

#df.fillna(df.mean(numeric_only=True))
del df['z']

 
df

# COMMAND ----------

print(df.fillna(df.mean(numeric_only=True)))
df

# COMMAND ----------

df.fillna(df.median())

# COMMAND ----------

# MAGIC %md
# MAGIC Fara a sterge coloana z -nu merge foarte bine -> warnings

# COMMAND ----------

df = pd.DataFrame({'x': [ 1, 6, 9 , 0 ], 'y': [3, np.nan, 8, 2], 'z':['T', np.nan, 'F', 'F'], 't':[5,8, 4, None]})
df

# COMMAND ----------

print(df.fillna(df.mean(numeric_only=True)))

# COMMAND ----------

df = pd.DataFrame({'x': [ 1, 6, 9 , 0 ], 'y': [3, np.nan, 8, 2], 'z':['T', np.nan, 'F', 'F'], 't':[5,8, 4, None]})
df

# COMMAND ----------

df.interpolate()

# COMMAND ----------

df.plot()

# COMMAND ----------

df.interpolate().plot()

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC # Ex. 2

# COMMAND ----------

# MAGIC %md
# MAGIC Plecand de la DF din Ex. 1, tratati datele lipsa prin inlocuirea cu alte date in 3 feluri distincte. Salvati cele trei DF care rezulta.

# COMMAND ----------

print(df_ex1)

df_1 = df_ex1.fillna(df_ex1.mean(numeric_only=True))
df_1

# COMMAND ----------

print(df_ex1)

df_2 = df_ex1.fillna(df_ex1.median(numeric_only=True))
df_2

# COMMAND ----------

df_3 = df_ex1.copy()
print(df_3)
df_3.plot()


df_3 = df_3.interpolate().plot()

df_3 = df_ex1.ffill()
print(df_3)

df_3.plot()

# COMMAND ----------

df_4 = df_ex1.copy()
print(df_4)

for col in df_4.select_dtypes(include=['object','number']).columns:
    mode_values = df_4[col].mode()
    df_4[col] = df_4[col].fillna(mode_values[0])

print(df_4)

# COMMAND ----------

# MAGIC %md
# MAGIC Verificam daca cele trei nu mai au date lipsa.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Stergerea liniilor si coloanelor

# COMMAND ----------

df = pd.DataFrame({'x': [ 1, 6, 9 , 0 ], 'y': [3, np.nan, 8, 2], 'z':['T', np.nan, 'F', 'F'], 't':[5,8, 4, None]})
df

# COMMAND ----------

df.dropna() # sterge toate liniile ce contin date lipsa
df

# COMMAND ----------

df.dropna(axis = 1) # sterge toate coloanele ce contin date lipsa

# COMMAND ----------

df

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ex. 3.

# COMMAND ----------

# MAGIC %md
# MAGIC Plecand de la DF din Ex. 1, tratati datele lipsa prin stergerea tuturor liniilor cu elemente nule.

# COMMAND ----------

df_ex3 = df_ex1.copy()
print(df_ex3)

df_ex3.dropna(inplace=True)
print(df_ex3)

# COMMAND ----------

# MAGIC %md
# MAGIC Plecand de la DF din Ex. 1, tratati datele lipsa prin stergerea tuturor coloanelor cu elemente nule.

# COMMAND ----------

df_ex3 = df_ex1.copy()
print(df_ex3)

df_ex3.dropna(axis=1, inplace=True)
print(df_ex3)

# COMMAND ----------

# MAGIC %md
# MAGIC Plecand de la DF din Ex. 1, tratati datele lipsa prin stergerea tuturor liniilor (doar acelor linii) cu toate elemente nule.
# MAGIC Pentru aceasta invocati helpul functiei pd.dropna cu ?

# COMMAND ----------

help(pd.DataFrame.dropna)

# COMMAND ----------

df_ex3 = df_ex1.copy()
print(df_ex3)

print(df_ex3.dropna(how='all'))

# COMMAND ----------

df_ex3 = df_ex1.copy()
print(df_ex3)

print(df_ex3.dropna(thresh=3)) # keep rows that have at least 3 non-NaN values

# COMMAND ----------

df_ex3 = df_ex1.copy()
print(df_ex3)

print(df_ex3.dropna(subset=['A', 'C'])) # drop rows where NaN appears in columns 'A' and 'C' only

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exemplu de tratare a datelor lipsa

# COMMAND ----------

df1 = pd.read_csv("auto-mpg_bun.csv")

# COMMAND ----------

df1

# COMMAND ----------

df1.info()

# COMMAND ----------

type(df1['horsepower'][0])
 
# Observam ca este o problema cu tipul de date pt horsepower

# COMMAND ----------

df1['horsepower'].unique()    
# observam ca apare ? pe coloana ; vom  inlocui cu valoarea NaN

# COMMAND ----------

df1.replace('?', pd.NA, inplace = True)
print(df1)
df1.isnull().sum()

# COMMAND ----------

for x in df1['horsepower']:
    print(x)

# COMMAND ----------

df1.info()

# COMMAND ----------

df1['horsepower'].ffill(inplace = True)

# COMMAND ----------

print(df1.info())
df1.isnull().sum().sum()

# COMMAND ----------

df1.info()

# COMMAND ----------

sir1 = df1['horsepower'].astype(float, copy = False)
sir1

# COMMAND ----------

df1.info()

# COMMAND ----------

df1['horsepower_float'] =  sir1

# COMMAND ----------

df1

# COMMAND ----------

df1.info()

# COMMAND ----------

df1.describe()

# COMMAND ----------

# MAGIC %md
# MAGIC Eliminam coloana horsepower

# COMMAND ----------

del df1['horsepower']

# COMMAND ----------

df1.info()

# COMMAND ----------

# MAGIC %md
# MAGIC Redenumim atributul horsepower_float ca si horsepower

# COMMAND ----------

df1.rename(columns={'horsepower_float':'horsepower'}, inplace=True)

# COMMAND ----------

df1.info()

# COMMAND ----------

# MAGIC %md
# MAGIC Acum putem lucra cu toate atributele numerice asa cum ne-am dorit. 