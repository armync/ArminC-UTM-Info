# Databricks notebook source
# MAGIC %md
# MAGIC # Import data

# COMMAND ----------

# MAGIC %md
# MAGIC Vom folosi pandas. Exista multe functii care permit lucrul cu date tabelare cele mai folosite fiind 
# MAGIC
# MAGIC **read_csv** si **read_table**.

# COMMAND ----------

import pandas as pd
pd.read_csv?

# COMMAND ----------

df = pd.read_csv('auto-mpg_bun.csv')


# COMMAND ----------

df

# COMMAND ----------

df.info()

# COMMAND ----------

df.head()

# COMMAND ----------

df.tail(2)

# COMMAND ----------

df.describe()

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC De multe ori fisierul csv nu are si numele coloanelor (fara header).

# COMMAND ----------

# MAGIC %md
# MAGIC ### Colectia de date: Teaching Assistant Evaluation
# MAGIC
# MAGIC https://archive.ics.uci.edu/ml/datasets/teaching+assistant+evaluation
# MAGIC
# MAGIC    The data consist of evaluations of teaching performance over three
# MAGIC    regular semesters and two summer semesters of 151 teaching assistant
# MAGIC    (TA) assignments at the Statistics Department of the University of
# MAGIC    Wisconsin-Madison. The scores were divided into 3 roughly equal-sized
# MAGIC    categories ("low", "medium", and "high") to form the class variable.
# MAGIC
# MAGIC 5. Number of Instances: 151
# MAGIC
# MAGIC 6. Number of Attributes: 6 (including the class attribute)
# MAGIC
# MAGIC 7. Attribute Information:
# MAGIC   
# MAGIC    1. Whether of not the TA is a native English speaker (binary)
# MAGIC       1=English speaker, 2=non-English speaker
# MAGIC    2. Course instructor (categorical, 25 categories)
# MAGIC    3. Course (categorical, 26 categories)
# MAGIC    4. Summer or regular semester (binary) 1=Summer, 2=Regular
# MAGIC    5. Class size (numerical)
# MAGIC    6. Class attribute (categorical) 1=Low, 2=Medium, 3=High
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

df5 = pd.read_csv('tae.data', header = None) #incarcata fara header. 

# COMMAND ----------

df5

# COMMAND ----------

df5.info()

# COMMAND ----------

headerTAevaluation =['Native English speaker(Y/N)','Course instructor', 'Course', 'Summer or regular semester', 'Class size', 'Class attribute']

df5 = pd.read_csv('tae.data', names=headerTAevaluation) # se completeaza cu numele atributelor


# COMMAND ----------

df5

# COMMAND ----------

df5.info()

# COMMAND ----------

df5.astype('int32').dtypes

# COMMAND ----------

# Folosind functia where (care este diferita de cea din numpy), putem modifica valori in tabel.
df5.where?

# COMMAND ----------

# df5['column_name'].where(condition, other, inplace=True/False)

# cand conditia este falsa se inlocuieste cu valoarea de dupa virgula, inplace default este False

df5['Native English speaker(Y/N)'].where((df5['Native English speaker(Y/N)'] != 2), False, inplace = True) 
df5['Native English speaker(Y/N)'].where((df5['Native English speaker(Y/N)'] != 1), True, inplace = True) 
df5

# COMMAND ----------

df5['Native English speaker(Y/N)'].where((df5['Native English speaker(Y/N)'] != 1), True, inplace = True)
df5

# COMMAND ----------

df5.info()

# COMMAND ----------

df5.astype({'Native English speaker(Y/N)':'bool'}).dtypes


# COMMAND ----------

df5

# COMMAND ----------

df5['Summer or regular semester'].where((df5['Summer or regular semester'] != 1), 'Summer', inplace = True)
df5['Summer or regular semester'].where((df5['Summer or regular semester'] != 2), 'Regular', inplace = True)
df5

# COMMAND ----------


print(df5['Class attribute'].where((df5['Class attribute'] != 1), 'low', inplace = True))

print(df5['Class attribute'].where((df5['Class attribute'] != 2), 'medium', inplace = True))

print(df5['Class attribute'].where((df5['Class attribute'] != 3), 'high', inplace = True))

# COMMAND ----------

df5.dtypes

# COMMAND ----------

type(df5.iloc[0,4])

# COMMAND ----------

df5.astype({'Course instructor':'int32','Course': 'int32','Class size': 'int32'}).dtypes

# COMMAND ----------

df5.info()

# COMMAND ----------

type(df5.iloc[0][1])

# COMMAND ----------

# find all the rows in the DataFrame df5 where the 'Course instructor' is 23; then, from those rows, take the values in the 'Class attribute' column and calculate their average

# Create a mapping dictionary for categorical values
mapping = {'high': 3, 'medium': 2, 'low': 1}

# Create a numeric version of the categorical column
df5['Class attribute numeric'] = df5['Class attribute'].map(mapping)

# Calculate means for specific filters
# For all courses by instructor 23:
print(df5[df5['Course instructor'] == 23]['Class attribute numeric'].mean())

# For summer courses by instructor 23:
print(df5[(df5['Course instructor'] == 23) & (df5['Summer or regular semester'] == 'Summer')]['Class attribute numeric'].mean())


# COMMAND ----------

# MAGIC %md ## Example 
# MAGIC ## Applying Mapping to Create Numeric Column
# MAGIC
# MAGIC A table with four columns: **ID**, **Class attribute**, **Course instructor**, and **Class attribute numeric**. 
# MAGIC
# MAGIC The "Class attribute" column contains categorical data ("high", "low", "medium"). To perform numerical calculations, these categories are mapped to numerical values in the "Class attribute numeric" column:
# MAGIC
# MAGIC * **high** is mapped to **3**
# MAGIC * **low** is mapped to **1**
# MAGIC * **medium** is mapped to **2**
# MAGIC
# MAGIC Here's the data from the table:
# MAGIC
# MAGIC | ID | Class attribute | Course instructor | Class attribute numeric |
# MAGIC |---|---|---|---|
# MAGIC | 17 | high | 23 | 3 |
# MAGIC | 49 | high | 5 | 3 |
# MAGIC | 33 | high | 7 | 3 |
# MAGIC | 26 | low | 23 | 1 |
# MAGIC | 12 | low | 23 | 1 |
# MAGIC | 48 | medium | 48 | 2 |
# MAGIC | 51 | medium | 23 | 2 |
# MAGIC
# MAGIC ## Calculate Mean for Instructor 23
# MAGIC
# MAGIC Calculates the mean of the "Class attribute numeric" values for the rows where the "Course instructor" is 23.
# MAGIC
# MAGIC df5[df5['Course instructor'] == 23]['Class attribute numeric'].mean()
# MAGIC
# MAGIC Values:  3  1  1  2
# MAGIC <br>
# MAGIC Calculation:  (3 + 1 + 1 + 2) ÷ 4 = 1.75
# MAGIC <br>
# MAGIC Mean: 1.75

# COMMAND ----------

df5[df5['Course instructor'] == 23]['Class size'].mean()

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

df6 = pd.read_csv('auto-mpg_bun.csv', nrows=3) #selectam nr de linii pe care le incarcam din fisier
df6

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ex. 1

# COMMAND ----------

# MAGIC %md
# MAGIC + Sa se descarce colectia de date iris.data  de la https://archive.ics.uci.edu/ml/datasets/iris
# MAGIC + Sa se importe colectia de date adaugand si numele coloanelor

# COMMAND ----------

headerIRIS = ('sepal length in cm','sepal width in cm','petal length in cm','petal width in cm','class')

df_ex1 = pd.read_csv('iris.data', names=headerIRIS)

# COMMAND ----------

# MAGIC %md
# MAGIC + Afisati toata colectia
# MAGIC  

# COMMAND ----------

df_ex1 

# COMMAND ----------

# MAGIC %md
# MAGIC + Afisati primele linii
# MAGIC

# COMMAND ----------

df.head(5) 

# COMMAND ----------

# MAGIC %md
# MAGIC + Afisati ultimele linii
# MAGIC  

# COMMAND ----------

df.tail(5)

# COMMAND ----------

# MAGIC %md
# MAGIC + Afisati informatia despre colectie

# COMMAND ----------

df_ex1.info() 

# COMMAND ----------

# MAGIC %md
# MAGIC + Afisati datele statistice (mean, count, etc. ) pentru datele numerice din colectie

# COMMAND ----------

df_ex1.mean() 

# COMMAND ----------

df_ex1.count()

# COMMAND ----------

df_ex1.median()

# COMMAND ----------

# MAGIC %md
# MAGIC # Output data

# COMMAND ----------

df5.to_csv('TA_Evaluation_prelucrat.csv')

# COMMAND ----------

df5.to_csv('TA_Evaluation_prelucrat_tab.txt', sep='\t')


# COMMAND ----------

df6

# COMMAND ----------

import sys
df6.to_csv(sys.stdout, sep='\t')

# COMMAND ----------

df6.to_csv(sys.stdout, sep='\t', index = False)

# COMMAND ----------

df6.to_csv(sys.stdout, sep='\t', index = False, header = False)

# COMMAND ----------

df5.to_csv(sys.stdout, sep='\t', index = False, columns=['Course instructor', 'Class attribute'])

# COMMAND ----------

df5

# COMMAND ----------

# %pip install openpyxl

import openpyxl

df5.to_excel("TA_evaluation.xlsx", sheet_name="TA_eval", index_label = "Nr.crt")
df5.to_excel("TA_evaluation.xlsx", sheet_name="TA_eval2", index_label = "Nr.crt")

# COMMAND ----------

# MAGIC %md
# MAGIC A generat fisierul excel.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Daca vrem sa selectam doar o parte din DataFrame si sa il punem intr-un alt Sheet in acelasi fisier Excel:

# COMMAND ----------

df5_simplified = df5.drop(columns = {'Native English speaker(Y/N)', 'Course', 'Summer or regular semester', 'Class size'})
df5_simplified

# COMMAND ----------

# MAGIC %md
# MAGIC df5.to_excel("TA_evaluation.xlsx", sheet_name="TA_eval", index_label = "Nr.crt")

# COMMAND ----------

with pd.ExcelWriter("TA_eval_multiple_sheets.xlsx") as writer:
    df5.to_excel(writer, sheet_name="TA_eval", index_label = "Nr.crt")
    df5_simplified.to_excel(writer, sheet_name="TA_doar_evaluarile", index_label = "Nr.crt")

# COMMAND ----------

# MAGIC %md
# MAGIC A scris in fisierul TA_eval_multiple_sheets.xlsx primul sheet ca mai sus si al doilea, cu numele TA_doar_evaluarile

# COMMAND ----------

# MAGIC %md
# MAGIC # Ex.2 

# COMMAND ----------

# MAGIC %md
# MAGIC + Plecand de la dataFrame-ul de la Ex. 1 scrieti pe ecran continutul cu datele separate de tab, fara coloana index.

# COMMAND ----------

df_ex1.to_csv(sys.stdout, sep='\t', index = False)

# COMMAND ----------

# MAGIC %md
# MAGIC + Plecand de la dataFrame-ul de la Ex. 1 scrieti continutul intr-un fisier excel cu doua sheet-uri
# MAGIC     - unul cu primele doua coloane, fara coloana de index
# MAGIC     - altul doar cu primele 5 linii, fara coloana de index
# MAGIC

# COMMAND ----------

df5.iloc[:,:2].to_excel("iris_col.xlsx", sheet_name='col_no_index', index=False)

# COMMAND ----------

df5.iloc[:5].to_excel("iris_row.xlsx", sheet_name='row_no_index', index=False)