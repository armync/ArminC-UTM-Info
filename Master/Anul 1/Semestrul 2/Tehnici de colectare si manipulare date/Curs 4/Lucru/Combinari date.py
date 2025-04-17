# Databricks notebook source
# MAGIC %md
# MAGIC # Combinari ale colectiilor de date

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concatenare serii

# COMMAND ----------

import numpy as np
import pandas as pd

# COMMAND ----------

s1 = pd.Series([1,2,3])
print(s1)
s2 = pd.Series([4,5,6])
print(s2)

# COMMAND ----------

s= pd.concat([s1,s2]) # concateneaza pe verticala
s

# COMMAND ----------

s[0]

# COMMAND ----------

s.sort_index(inplace = True)

# COMMAND ----------

s

# COMMAND ----------

s_concatenated= pd.concat([s1,s2, s2], ignore_index=True)

# COMMAND ----------

s_concatenated

# COMMAND ----------

s1

# COMMAND ----------

s= pd.concat([s1,s2], axis = 1) # face concatenarea pe orizontala
s

# COMMAND ----------

s3 = pd.Series([1, 3, 5], name='A')
s3

# COMMAND ----------

s4 = pd.Series([10,20], name="B")
s4

# COMMAND ----------

t = pd.concat([s3,s4], axis = 1)
t

# COMMAND ----------

t = pd.concat([s3,s4])
t

# COMMAND ----------

# MAGIC %md
# MAGIC ## Concatenare dataframes

# COMMAND ----------

df1 = pd.DataFrame({'A': np.array([1, 3, 6, 20]), 'B': np.arange(4)})
df1

# COMMAND ----------

df2 = pd.DataFrame({'A': [3, 4], 'B': [1,2]})
df2

# COMMAND ----------

df_concatenated = pd.concat([df1,df2])
df_concatenated

# COMMAND ----------

df3 = pd.DataFrame([[1,2,3],[4,'a','c'],[12,43,90]], columns = list("XYZ"))
df3

# COMMAND ----------

print(df1)
print(df3)

df_unit_df1_df3 = pd.concat([df1,df3])
df_unit_df1_df3

# COMMAND ----------

df4 = pd.DataFrame([[1,2,3],[4,'a','c'],[12,43,90]], columns = list("XBZ"))
df4

# COMMAND ----------

df_unit_df1_df4 = pd.concat([df1,df4])
df_unit_df1_df4

# COMMAND ----------

df1

# COMMAND ----------

df_unit_df1_df4 = pd.concat([df1,df4], ignore_index=True)
df_unit_df1_df4

# COMMAND ----------

df_unit_df1_df4 = pd.concat([df1,df4], join = "inner") # combina si retine doar coloanele comune (cu acelasi nume)
df_unit_df1_df4

# COMMAND ----------

df_10 = pd.concat([df1,df2], axis =1)
df_10

# COMMAND ----------

df_11 = pd.concat([df1,df3], axis =1)
df_11

# COMMAND ----------

df_11 = pd.concat([df1,df3], axis =1, join="inner") # retine doar liniile comune
df_11

# COMMAND ----------

df1

# COMMAND ----------

df3

# COMMAND ----------

# MAGIC %md
# MAGIC ### 

# COMMAND ----------

df_11 = pd.concat([df1,df3], verify_integrity=True) # verificam daca sunt indici care se suprapun; 
                                                     # daca da nu se va face concatenarea
df_11

# COMMAND ----------

# MAGIC %md
# MAGIC Adaugam un rand nou in dataframe

# COMMAND ----------

df3

# COMMAND ----------

s10 = pd.Series ({'X':10, 'Y': 20, 'Z':'0'})
print(s10)
print(s10.to_frame())
print(s10.to_frame().T) # transpusa

# COMMAND ----------

new_row = pd.concat([df3, s10.to_frame().T], ignore_index=True)
new_row

# COMMAND ----------

# MAGIC %md
# MAGIC ## Merge

# COMMAND ----------

df1 = pd.DataFrame({'A': np.array([1, 3, 6, 20]), 'B': np.arange(4)})
df1

# COMMAND ----------

df3 = pd.DataFrame({'A': [1, 3, 20, 6], 'C': [10,20, 30, 40], 'D':[1,2,3, 4]})
df3

# COMMAND ----------

pd.merge(df1,df3, on="A") #implicit how = "inner" adica le selecteaza pe cele comune

# COMMAND ----------

df3 = pd.DataFrame({'A': [10, 3, 20, 6], 'C': [10,20, 30, 40], 'D':[1,2,3, 4]})
df3

# COMMAND ----------

pd.merge(df1,df3, on="A", how = "outer") #implicit how = "inner" adica le selecteaza pe cele comune

# COMMAND ----------

df2 = pd.DataFrame({'A': [3, 4], 'B': [10,2]})
df2
df1

# COMMAND ----------

pd.merge(df1,df2, on = "A")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Groupby

# COMMAND ----------

df = pd.DataFrame(
    {
        "animal": "cat dog cat fish dog cat cat".split(),
        "size": list("SSMMMLL"),
        "weight": [8, 10, 11, 1, 20, 12, 12],
        "adult": [False] * 5 + [True] * 2,
    }
)

# COMMAND ----------

df

# COMMAND ----------

print(df)

df.groupby("animal").sum(numeric_only=True)

# COMMAND ----------

df.groupby("size").sum(numeric_only=True)

# COMMAND ----------

df.groupby("animal").get_group("cat")

# COMMAND ----------

df.groupby("size").get_group("M")

# COMMAND ----------

df.groupby("adult").get_group(False)

# COMMAND ----------

# split DataFrame cu sample()
df1 = df.sample(frac = 0.75, random_state = 200)
print(df1)
df1.reset_index()

# COMMAND ----------

df = pd.read_csv('adult.csv')
df.info()

# COMMAND ----------

df.columns = df.columns.map(lambda x: x[1:])

# COMMAND ----------

df.info()

# COMMAND ----------

df = df.rename(columns={ "ge":"age"})

# COMMAND ----------

df.drop_duplicates(inplace=True)

# COMMAND ----------

df

# COMMAND ----------

t=df.groupby("race").get_group(" White").groupby("education").get_group(" Bachelors")
t

# COMMAND ----------

t.groupby("education").get_group(" Bachelors") 