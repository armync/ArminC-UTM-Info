# Databricks notebook source
# MAGIC %md
# MAGIC # Vizualizarea

# COMMAND ----------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# COMMAND ----------

x = np.linspace(-5, 5, 100)

# COMMAND ----------

x

# COMMAND ----------

# MAGIC %md
# MAGIC Putem reprezenta grafic mai multe functii. 
# MAGIC Am definit valorile pe care trebuie sa le ia x. Valorile lui y vor fi valorile functiei in fiecare valoare din x.

# COMMAND ----------

# Mai multe ploturi pe o singura figura, in aceeasi celula.
plt.plot(x, x ** 3 - 3*x +1)
plt.plot(x, x*x)
plt.plot(x, -x**3 + 3*x -1)
plt.plot(x, - x*x)
plt.title('O figura complexa')
plt.legend(['a','b','c','d'])
plt.xlabel('x')
plt.ylabel('functia')

# COMMAND ----------

plt.plot(x, x*x)

# COMMAND ----------

f1 = plt.figure() # salvam figura astfel incat sa putem adauga mai multe ploturi ulterior.
plt.plot(x, x*x)

# COMMAND ----------

plt.figure(f1)
plt.plot(x,-x*x) #acest plot se va face pe aceeasi figura (f1) ca si mai sus.

# COMMAND ----------

plt.figure(f1)
plt.plot(x, x) # inca un plot

# COMMAND ----------

plt.figure(figsize=(10,5)) # O figura noua in care am precizat si dimensiunea.
                           # 10 inch. (pe orizontala- adica latimea)  si 5 inch (pe verticala)
                           # default [6.4, 4.8]
plt.plot(x, x*x)

# COMMAND ----------

# MAGIC %md
# MAGIC # Ex. 1 

# COMMAND ----------

# MAGIC %md
# MAGIC - Sa se
# MAGIC deseneze in aceeasi figura graficele functiilor sin(x) si cos(x) pe intervalul [0, 2 pi]. 
# MAGIC - Etichetati si axele si legenda si adaugati titlu.

# COMMAND ----------

import math
x = np.linspace(0, 2*math.pi, 100)
 

# COMMAND ----------

x = np.linspace(0, 2*math.pi, 100)
f = np.sin(x)
g = np.cos(x)

plt.plot(x, f, label='sin(x)')
plt.plot(x, g, label='cos(x)')

plt.xlabel('x')
plt.ylabel('f(x), g(x)')
plt.title('Graficul functiilor sin(x) si cos(x)')
plt.legend()


# COMMAND ----------

math.pi

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC Putem avea mai multe plot-uri intr-o figura cu **plt.subplot**

# COMMAND ----------

fig, axes = plt.subplots(2, 3, figsize=(16, 8))  # 2x3 grid of subplots
fig.suptitle('Puterile lui x') 

# 1st row
axes[0, 0].plot(x, x)
axes[0, 0].legend(['X'])
axes[0, 0].set_xlabel('X')
axes[0, 0].set_ylabel('X')

axes[0, 1].plot(x, x ** 2)
axes[0, 1].legend(['X^2'])
axes[0, 1].set_xlabel('X')
axes[0, 1].set_ylabel('X^2')

axes[0, 2].plot(x, x ** 3)
axes[0, 2].legend(['X^3'])
axes[0, 2].set_xlabel('X')
axes[0, 2].set_ylabel('X^3')

# 2nd row
axes[1, 0].plot(x, -x)
axes[1, 0].legend(['-X'])
axes[1, 0].set_xlabel('X')
axes[1, 0].set_ylabel('-X')

axes[1, 1].plot(x, -(x ** 2))
axes[1, 1].legend(['-X^2'])
axes[1, 1].set_xlabel('X')
axes[1, 1].set_ylabel('-X^2')

axes[1, 2].plot(x, -(x ** 3))
axes[1, 2].legend(['-X^3'])
axes[1, 2].set_xlabel('X')
axes[1, 2].set_ylabel('-X^3')

plt.tight_layout(rect=[0, 0, 1, 0.96])  # layout adjust
plt.show()


# COMMAND ----------

# MAGIC %md
# MAGIC ----

# COMMAND ----------

# MAGIC %md
# MAGIC # Ex. 2

# COMMAND ----------

# MAGIC %md
# MAGIC Sa se reprezinte intr-o imagine cu 4 ploturi (2 linii si 2 coloane) graficele functiilor sin(x), cos(x), tan(x), arctan(x) pe intervalul [-pi, pi]

# COMMAND ----------

fig_ex2, axes_ex2 = plt.subplots(2, 2, figsize=(16, 8))  # 2x3 grid of subplots
fig_ex2.suptitle('Graficul functiilor sin(x) si cos(x)') 

x = np.linspace(-math.pi, math.pi, 100)
f = np.sin(x)
g = np.cos(x)
h = np.tan(x)
i = np.arctan(x)

# 1st row
axes_ex2[0, 0].plot(x, f)
axes_ex2[0, 0].legend(['sin(x)'])
axes_ex2[0, 0].set_xlabel('x')
axes_ex2[0, 0].set_ylabel('f(x)')

axes_ex2[0, 1].plot(x, g)
axes_ex2[0, 1].legend(['cos(x)'])
axes_ex2[0, 1].set_xlabel('x')
axes_ex2[0, 1].set_ylabel('f(g)')


# 2nd row
axes_ex2[1, 0].plot(x, h)
axes_ex2[1, 0].legend(['tan(x)'])
axes_ex2[1, 0].set_xlabel('x')
axes_ex2[1, 0].set_ylabel('f(h)')

axes_ex2[1, 1].plot(x, i)
axes_ex2[1, 1].legend(['arctan(x)'])
axes_ex2[1, 1].set_xlabel('x')
axes_ex2[1, 1].set_ylabel('f(i)')


plt.tight_layout(rect=[0, 0, 1, 0.96])  # layout adjust
plt.show()


# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC Sa consideram o colectie de date generata cu Google Trends: termeni de cautare **"tenis"** si **"Paste"**.
# MAGIC
# MAGIC Reprezinta nr de cautari in Romania in decurs de 7 zile pe ora.

# COMMAND ----------

dftenis_paste = pd.read_csv("multiTimeline_2.csv")
dftenis_paste.info()

# COMMAND ----------

dftenis_paste

# COMMAND ----------

dftenis_paste.info()

# COMMAND ----------

type(dftenis_paste['Time'][0])

# COMMAND ----------

from dateutil.parser import parse

# COMMAND ----------

parse(dftenis_paste['Time'][1])

# COMMAND ----------

dftenis_paste.head()

# COMMAND ----------

dftenis_paste['Time'] = pd.to_datetime(dftenis_paste['Time'])
dftenis_paste

# COMMAND ----------

plt.figure(figsize=(20,10))
plt.plot(dftenis_paste['Time'], dftenis_paste['tenis: (Romania)'])

# COMMAND ----------

plt.figure(figsize=(20,10))
plt.subplot(1, 2, 1)
plt.plot(dftenis_paste['Time'], dftenis_paste['tenis: (Romania)'])
plt.subplot(1, 2, 2)
plt.plot(dftenis_paste['Time'], dftenis_paste['paste: (Romania)'])

# COMMAND ----------

plt.figure(figsize=(20,10))
plt.plot(dftenis_paste['Time'], dftenis_paste['tenis: (Romania)'])
plt.plot(dftenis_paste['Time'], dftenis_paste['paste: (Romania)'])

# COMMAND ----------

# MAGIC %md
# MAGIC ## Alte tipuri de plot-uri

# COMMAND ----------

dftenis_paste.plot(x= 'tenis: (Romania)', y= 'paste: (Romania)', kind= 'scatter')

# COMMAND ----------

dftenis_paste['tenis: (Romania)'].plot(kind='hist')

# COMMAND ----------

f = dftenis_paste['tenis: (Romania)'].plot(kind='density')
f.axvline(dftenis_paste['tenis: (Romania)'].mean(), color = 'g')
f.axvline(dftenis_paste['tenis: (Romania)'].median(), color = 'r')


# COMMAND ----------

f = dftenis_paste['paste: (Romania)'].plot(kind='density')
f.axvline(dftenis_paste['paste: (Romania)'].mean(), color = 'g')
f.axvline(dftenis_paste['paste: (Romania)'].median(), color = 'r')

# COMMAND ----------

dftenis_paste.describe()

# COMMAND ----------

plt.scatter(x= dftenis_paste['tenis: (Romania)'], y= dftenis_paste['paste: (Romania)'])

# COMMAND ----------

plt.hist(dftenis_paste['tenis: (Romania)'], bins = 10)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ex. 3

# COMMAND ----------

# MAGIC %md
# MAGIC Sa se genereze o alta colectie de date cu Google Trends si sa se prelucreze ca mai sus.

# COMMAND ----------

df_alegeri = pd.read_csv("multiTimeline.csv")
df_alegeri.info()

# COMMAND ----------

df_alegeri

# COMMAND ----------

plt.figure(figsize=(20,10))
plt.plot(df_alegeri['Time'], df_alegeri['George Simion: (Romania)'])

# COMMAND ----------

plt.figure(figsize=(20,10))
plt.subplot(3, 2, 1)
plt.plot(df_alegeri['Time'], df_alegeri['George Simion: (Romania)'])
plt.title("GS")
plt.subplot(3, 2, 2)
plt.plot(df_alegeri['Time'], df_alegeri['Victor Ponta: (Romania)'])
plt.title("VP")
plt.subplot(3, 2, 3)
plt.plot(df_alegeri['Time'], df_alegeri['Nicusor Dan: (Romania)'])
plt.title("ND")
plt.subplot(3, 2, 4)
plt.plot(df_alegeri['Time'], df_alegeri['Elena-Valerica Lasconi: (Romania)'])
plt.title("EL")
plt.subplot(3, 2, 5)
plt.plot(df_alegeri['Time'], df_alegeri['Crin Antonescu: (Romania)'])
plt.title("CA")

# COMMAND ----------

df_alegeri.plot(x= 'Elena-Valerica Lasconi: (Romania)', y= 'Nicusor Dan: (Romania)', kind= 'scatter')

# COMMAND ----------

df_alegeri['Elena-Valerica Lasconi: (Romania)'].plot(kind='hist')

# COMMAND ----------

f = df_alegeri['Crin Antonescu: (Romania)'].plot(kind='density')
f.axvline(df_alegeri['Crin Antonescu: (Romania)'].mean(), color = 'g')
f.axvline(df_alegeri['Crin Antonescu: (Romania)'].median(), color = 'r')

# COMMAND ----------

f = df_alegeri['Elena-Valerica Lasconi: (Romania)'].plot(kind='density')
f.axvline(df_alegeri['Elena-Valerica Lasconi: (Romania)'].mean(), color = 'g')
f.axvline(df_alegeri['Elena-Valerica Lasconi: (Romania)'].median(), color = 'r')

# COMMAND ----------

df_alegeri.describe()