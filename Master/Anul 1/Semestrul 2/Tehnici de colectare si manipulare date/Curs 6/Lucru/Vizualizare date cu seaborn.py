# Databricks notebook source
# MAGIC %md
# MAGIC # Seaborn 
# MAGIC bibliotecă de vizualizare în Python, construită pe baza matplotlib, concepută pentru vizualizarea datelor statistice. Oferă o interfață de nivel înalt pentru crearea de grafice atractive.

# COMMAND ----------

import seaborn as sns

# COMMAND ----------

import matplotlib.pyplot as plt
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

# COMMAND ----------

# MAGIC %md
# MAGIC Exista mai multe colectii de date incluse in seaborn.

# COMMAND ----------

sns.load_dataset('iris') # iris = colectie de date pt clasificarea florilor de iris

# COMMAND ----------

import seaborn as sns

datasets = sns.get_dataset_names() # care sunt colectiile de date
display(datasets)

# COMMAND ----------

df = sns.load_dataset('flights') 

# COMMAND ----------

df.describe()

# COMMAND ----------

df

# COMMAND ----------

# MAGIC %md
# MAGIC ### Colectia de date tips 
# MAGIC contine informatii despre note de plata la un restaurant, inclusiv bacsisul dat de clienti.
# MAGIC
# MAGIC Atribute:
# MAGIC - total_bill: suma totala in $
# MAGIC - tip: bacsisul in $
# MAGIC - sex: (Male, Female) client
# MAGIC - smoker: (Yes, No) client
# MAGIC - day: ziua saptamanii (Thur, Fri, Sat, Sun)
# MAGIC - time: (Lunch, Dinner)
# MAGIC - size: nr persoane la masa

# COMMAND ----------

df2 = sns.load_dataset('tips') 

# COMMAND ----------

df2.head()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Tipuri de grafice

# COMMAND ----------

sns.barplot(x='day', y='total_bill', data=df2)

# COMMAND ----------

sns.scatterplot(x='total_bill', y='tip', data=df2)

# COMMAND ----------

df2.describe()

# COMMAND ----------

sns.scatterplot(x='total_bill', y='tip', data=df2, hue ='sex')

# COMMAND ----------

sns.scatterplot(x='total_bill', y='tip', data=df2[df2.day == 'Sun'], hue ='sex')

# COMMAND ----------

sns.scatterplot(x='total_bill', y='size', data=df2[df2.day == 'Sun'], hue ='sex')

# COMMAND ----------

sns.scatterplot(x='total_bill', y='size', data=df2, style='time', hue = 'sex')

# COMMAND ----------

sns.scatterplot(x='total_bill', y='size', data=df2[df2.time == 'Dinner'], hue = 'sex')

# COMMAND ----------

sns.lineplot(x='total_bill', y='tip', data=df2)

# COMMAND ----------

sns.histplot(x='total_bill', data=df2)

# COMMAND ----------

sns.histplot(x='total_bill', data=df2, bins=20)

# COMMAND ----------

sns.histplot(x='total_bill', data=df2, bins=20, kde=True) #kde = kernel density estimation

# COMMAND ----------

sns.boxplot(x='day', y='total_bill', data=df2)

# COMMAND ----------

df2.columns

# COMMAND ----------

sns.boxplot(x = 'sex', y='total_bill', data=df2)

# COMMAND ----------

sns.boxplot(x = 'sex', y='total_bill', data=df2, hue='time')

# COMMAND ----------

sns.boxplot(x = 'sex', y='tip', data=df2, hue='time')

# COMMAND ----------

sns.boxplot(x ='smoker', y='tip', data=df2, hue='time')

# COMMAND ----------

sns.boxplot(x='day', y='total_bill', data=df2)

# COMMAND ----------

sns.boxplot(x='day', y='total_bill', data=df2, showfliers=False)

# COMMAND ----------

sns.violinplot(x='day', y='total_bill', data=df2)

# COMMAND ----------

sns.pairplot(df2)

# COMMAND ----------

sns.pairplot(data=df2, corner= True)

# COMMAND ----------

sns.pairplot(data=df2, corner=True, hue='time')

# COMMAND ----------

sns.pairplot(data=df2, corner=True, hue='sex')

# COMMAND ----------

sns.heatmap(df2.corr(), annot=True) # df2.corr este matricea de corelatie
# annot = True => afiseaza valoarea corelatiei in interiorul celulei

# COMMAND ----------

df2.corr()

# COMMAND ----------

sns.heatmap(df2.corr(), annot=True, cmap='coolwarm')

# COMMAND ----------

sns.heatmap(df2.corr(), annot=True, cmap='coolwarm', linewidths=1, linecolor='black')

# COMMAND ----------

sns.heatmap(df2.corr(), annot=True, cmap='coolwarm', linewidths=1, linecolor='black', fmt='.2f')

# COMMAND ----------

sns.heatmap(df2.corr(), annot=True, cmap='YlGnBu', linewidths=1, linecolor='black', fmt='.2f') #YlGnBu = Yellow-Green-Blue
plt.title('Heatmap - Corelatie')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Heatmap pentru data de tip discret

# COMMAND ----------


#Afisam media tip vs.day vs. time ca heatmap
pivot_table = df2.pivot_table(values='tip', index='day', columns='time', aggfunc='mean')
pivot_table

# COMMAND ----------

sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', linewidths=1, linecolor='black', fmt='.2f')

# COMMAND ----------

sns.heatmap(pivot_table, annot=True, cmap='coolwarm', fmt='.2f')

# COMMAND ----------

#Afisam media tip vs.smoker vs.time ca heatmap
pivot_table = df2.pivot_table(values='tip', index='smoker', columns='time', aggfunc='mean')
pivot_table

# COMMAND ----------

sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', linewidths=1, linecolor='black', fmt='.2f')

# COMMAND ----------

#Afisam media tip vs.smoker vs.day ca heatmap  
pivot_table = df2.pivot_table(values='tip', index='smoker', columns='day', aggfunc='mean')
pivot_table

# COMMAND ----------

sns.heatmap(pivot_table, annot=True, cmap='coolwarm', fmt='.2f')

# COMMAND ----------

#Afisam media tip vs.smoker vs. sex ca heatmap  
pivot_table = df2.pivot_table(values='tip', index='smoker', columns='sex', aggfunc='mean')
sns.heatmap(pivot_table, annot=True, cmap='coolwarm', fmt='.2f')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ex. 1

# COMMAND ----------

# MAGIC %md
# MAGIC Incarcati colectia de date diamonds din biblioteca seaborn care cuprinde descrierea mai multor diamante si pretul lor.
# MAGIC

# COMMAND ----------

df3 = sns.load_dataset('diamonds')
df3

# COMMAND ----------

# MAGIC %md
# MAGIC Reprezentati relatia dintre pret si celelalte caracteristici ale diamantelor prin mai multe grafice, tabele de corelatie, heatmap, de tipul celor de mai sus. 

# COMMAND ----------

df3.describe()

# COMMAND ----------

sns.barplot(x='cut',y='price',data=df3)

# COMMAND ----------

sns.scatterplot(x='carat',y='price',data=df3[df3.cut == 'Good'])

# COMMAND ----------

sns.boxplot(x='clarity', y='price', data=df3)

# COMMAND ----------

sns.pairplot(data=df3, corner= True)

# COMMAND ----------

df3.corr()

# COMMAND ----------

sns.heatmap(df3.corr(), annot=True)