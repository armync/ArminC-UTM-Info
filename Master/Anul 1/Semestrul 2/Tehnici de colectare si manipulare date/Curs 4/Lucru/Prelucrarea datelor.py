# Databricks notebook source
# MAGIC %md
# MAGIC # Prelucrarea datelor

# COMMAND ----------

# MAGIC %md
# MAGIC ## 

# COMMAND ----------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Redenumire index si coloane

# COMMAND ----------

# MAGIC %md
# MAGIC Vrem sa modificam numele coloanelor din baza de date corespunzatoare colectiei de date
# MAGIC
# MAGIC https://archive.ics.uci.edu/ml/datasets/adult
# MAGIC     
# MAGIC Adult Census Income Binary Classification dataset

# COMMAND ----------

df = pd.read_csv('adult.csv')
df.info()

# COMMAND ----------

df.columns

# COMMAND ----------

# MAGIC %md
# MAGIC Scriem o functie care modifica numele coloanelor eliminand spatiul. 

# COMMAND ----------

transform =  lambda x: x[1:]

# COMMAND ----------

df.columns = df.columns.map(transform)
df.columns

# COMMAND ----------

df.info()

# COMMAND ----------

df.rename(columns = {"ge": "age"}, inplace = True)
df

# COMMAND ----------

df.drop_duplicates(inplace=True) 
df
#df.describe()

# COMMAND ----------

df.describe()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Cum redenumim indicii?

# COMMAND ----------

df.reset_index(inplace = True, drop = True)
# del df['index']
df

# COMMAND ----------

transform2 =  lambda x: (x + 1)

# COMMAND ----------

df.index

# COMMAND ----------

# Echivalent cu
# def transformare(x):
#    return x + 1

# COMMAND ----------

df.index = df.index.map(transform2)


# COMMAND ----------

df.index

# COMMAND ----------

df.head()

# COMMAND ----------

df['race'].unique()

# COMMAND ----------

df['race'].value_counts()

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ex. 1.

# COMMAND ----------

# MAGIC %md
# MAGIC Sa se incarce colectia de date din fisierul trial.csv https://archive.ics.uci.edu/ml/datasets/Audit+Data

# COMMAND ----------

df_ex1 = pd.read_csv('trial.csv')

df_ex1

# COMMAND ----------

# MAGIC %md
# MAGIC Sa se verifice cu info() daca baza de date contine date lipsa.

# COMMAND ----------

df_ex1.info()

# COMMAND ----------

# MAGIC %md
# MAGIC Sa se afiseze care sunt toate valorile unice si cate sunt din fiecare ale atributului 'LOCATION_ID'

# COMMAND ----------

print(df_ex1['LOCATION_ID'].unique())
len(df_ex1['LOCATION_ID'].unique())

# COMMAND ----------

# MAGIC %md
# MAGIC Sa se elimine din dataframe liniile pentru care 'LOCATION_ID' nu sunt in concordanta cu restul valorilor.
# MAGIC

# COMMAND ----------

df_ex1 = df_ex1[df_ex1['LOCATION_ID'].str.isnumeric()]

# COMMAND ----------

df_ex1['LOCATION_ID'].unique()

# COMMAND ----------

len(df_ex1['LOCATION_ID'].unique())

# COMMAND ----------

# MAGIC %md
# MAGIC Sa se modifice tipul de date al coloanei LOCATION_ID in float

# COMMAND ----------

df_ex1['LOCATION_ID'] = df_ex1['LOCATION_ID'].astype(float)
df_ex1.info()

# COMMAND ----------

# MAGIC %md
# MAGIC Sa se scrie afiseze lista coloanelor DF

# COMMAND ----------

df_ex1.columns.tolist()

# COMMAND ----------

# MAGIC %md
# MAGIC Redenumiti toate numele coloanelor cu litere mari.

# COMMAND ----------

# The .upper() method is available for string objects, but not for an Index.
# Converts the column names to a list of strings and then applies .upper()

df_ex1.columns = df_ex1.columns.str.upper()

# COMMAND ----------

df_ex1.columns.tolist()

# COMMAND ----------

# MAGIC %md
# MAGIC Renumerotati indicii colectiei de date cu 1,2,3....

# COMMAND ----------

df_ex1.index

# COMMAND ----------

new_index = lambda x: x + 1

df_ex1.index = df_ex1.index.map(new_index)

df_ex1.index

# COMMAND ----------

# MAGIC %md
# MAGIC # Discretizarea atributelor continui - binning

# COMMAND ----------

print(df.describe())
df['age'].unique()

# COMMAND ----------

np.sort(df['age'].unique())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Discretizare in n intervale egale - (equal width discretization)
# MAGIC

# COMMAND ----------

n = 3 # nr intervale

# COMMAND ----------

lungime_interval = df['age'].max() - df['age'].min()
lungime_interval

# COMMAND ----------

lungimi_egale = lungime_interval/n
lungimi_egale

# COMMAND ----------

df['age']

# COMMAND ----------

t_ew = pd.cut(df['age'], n) #intervalul [min, max] se imparte in n intervale de lungime egala unde min = df['age'].min(), max = df['age'].max()
print(t_ew)
print('\n')
t_ew.unique()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Functia cut descrie intervalele in care se va face impartirea atributului.
# MAGIC Este un array de string care indica numele fiecarui interval (categorie).
# MAGIC
# MAGIC Functia returneaza o coloana care corespunde pentru fiecare inregistrare, intervalul care se asociaza valorii atributului continuu care a fost discretizat. 
# MAGIC
# MAGIC De exemplu, prima inregistrare: age = 39 si corespunde intervalului (16.927, 41.333]
# MAGIC
# MAGIC Functia cut returneaza un obiect de tip categorie (Categorical).
# MAGIC
# MAGIC  

# COMMAND ----------

t_ew.dtype # precizeaza cele n categorii in care se impart valorile atributului age 
        # (intervalele de varsta in care se imparte atributul.)

# COMMAND ----------

# MAGIC %md
# MAGIC # Discretizare cu valori individualizate

# COMMAND ----------

t_v1 = pd.cut(df['age'], [df['age'].min()-1, 30, 65, df['age'].max()]) # se precizeaza vectorul taieturilor 
        # adica a valorilor din capetele intervalelor in care se impart valorile atributului
t_v1

# COMMAND ----------

t_v1.values

# COMMAND ----------

t_v2 = pd.cut(df['age'], [df['age'].min(), 30, 65, df['age'].max()], include_lowest=True)
t_v2

# COMMAND ----------

t_v2, bins = pd.cut(df['age'], [df['age'].min(), 30, 65, df['age'].max()], include_lowest=True, retbins=True) 
print(t_v2, '\n')
print('bins=', bins)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Discretizare in intervale de frecventa egala (equal frequency discretization)

# COMMAND ----------

df['age'].value_counts()

# COMMAND ----------

df.describe()

# COMMAND ----------

t_efq = pd.qcut(df['age'], [0, 0.25,0.5, 0.75, 1])
t_efq

# COMMAND ----------

t_efq, bins = pd.qcut(df['age'], [0, 0.25,0.5, 0.75, 1], retbins=True)
bins

# COMMAND ----------

t_ew= pd.qcut(df['age'], 3, labels=["young", "adult", "old"]) # intervalul [min, max] se imparte in n intervale 
# de frecventa egala cu etichetele corespunzatoare
t_ew


# COMMAND ----------

t_ew, t_ew_bins = pd.qcut(df['age'], 3, labels=["young", "adult", "old"], retbins=True)

t_ew_bins

# COMMAND ----------

df

# COMMAND ----------

df['age_disc_efq']= pd.qcut(df['age'], 3, labels=["young", "adult", "old"])
df

# COMMAND ----------

df.info()

# COMMAND ----------

corr = df.corr(numeric_only=True) # matricea de corelatie (pentru variabile de tip continuu)
corr

# COMMAND ----------

fig = plt.figure(figsize=(8,8))
plt.matshow(corr, cmap='RdBu')
plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical')
plt.yticks(range(len(corr.columns)), corr.columns);

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ex. 2.

# COMMAND ----------

# MAGIC %md
# MAGIC - Plecand de la colectia de date de la ex1 sa se discretizeze 
# MAGIC     - atributul SCORE in 3 intervale de lungime egala
# MAGIC     - atributul SECTOR_SCORE in 4 intervale de frecventa egala
# MAGIC     - atributul DISTRICT dupa un set de taieturi specificate cu etichetele d2, d4, d6

# COMMAND ----------

df_ex2 = df_ex1
df_ex2

# COMMAND ----------

df_ex2_score = pd.cut(df_ex2['SCORE'],3)  # lungime egala
df_ex2_score

# COMMAND ----------

df_ex2_sector = pd.qcut(df_ex2['SECTOR_SCORE'],4) #frecventa egala
df_ex2_sector

# COMMAND ----------

#atributul DISTRICT dupa un set de taieturi specificate cu etichetele d2, d4, d6

cut_points = [0, 2, 4, 6, 8]

df_ex2_district = pd.cut(df_ex2['DISTRICT'], bins=cut_points, labels=['d2', 'd4', 'd6', 'other'])

df_ex2_district

# COMMAND ----------

# MAGIC %md
# MAGIC Sa se construiasca matricea de corelatie

# COMMAND ----------

df_ex2_corr = df_ex2.corr(numeric_only=True)
df_ex2_corr

# COMMAND ----------

# MAGIC %md
# MAGIC Sa se construiasca matricea corelatiei in formatul color

# COMMAND ----------

df_ex2_fig = plt.figure(figsize=(8,8))
plt.matshow(df_ex2_corr, cmap='RdBu')
plt.xticks(range(len(df_ex2_corr.columns)), df_ex2_corr.columns, rotation='vertical')
plt.yticks(range(len(df_ex2_corr.columns)), df_ex2_corr.columns);

# COMMAND ----------

# MAGIC %md
# MAGIC # Prelucrare atribute discrete

# COMMAND ----------

df['race'].value_counts()

# COMMAND ----------

df['race'].value_counts().plot(kind = 'bar')
plt.title('Race')

# COMMAND ----------

df['race'].value_counts().plot(kind = 'pie', figsize=(7,8))

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ex.3.

# COMMAND ----------

# MAGIC %md
# MAGIC Plecand de la baza de date de la exercitiul 2 
# MAGIC - sa se reprezinte grafic in doua feluri atributul discretizare a lui DISTRICT 

# COMMAND ----------

df_ex2_dis_view = pd.cut(df_ex2['DISTRICT'],3).value_counts().plot(kind = 'pie')
df_ex2_dis_view

# COMMAND ----------

df_ex2['DISTRICT'].hist(bins=3, color='green', edgecolor='black')
plt.xlabel('Intervale')
plt.ylabel('Frecventa')
plt.title('Distributie')
plt.show()