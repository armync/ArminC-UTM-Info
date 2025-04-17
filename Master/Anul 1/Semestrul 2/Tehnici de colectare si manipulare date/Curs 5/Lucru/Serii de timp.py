# Databricks notebook source
# MAGIC %md
# MAGIC # Serii de timp

# COMMAND ----------

from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# COMMAND ----------

acum = datetime.now()
acum

# COMMAND ----------

acum.year

# COMMAND ----------

acum.month

# COMMAND ----------

acum.day

# COMMAND ----------

acum.hour

# COMMAND ----------

acum.minute


# COMMAND ----------

acum.second

# COMMAND ----------

acum.microsecond

# COMMAND ----------

datetime.now() - datetime(2003,5,6)

# COMMAND ----------

print(datetime.now())
datetime.now() + timedelta(1) # plus 24 ore

# COMMAND ----------

timedelta(1, 50, 100)

# COMMAND ----------

timedelta(0,0,0,0,0,0,1)
timedelta?

# COMMAND ----------

timedelta(1, hours=3, minutes = 2)

# COMMAND ----------

print(datetime.now())
datetime.now() + timedelta(1, 50, 100)

# COMMAND ----------

datetime.date(datetime.now()) # doar data calendaristica

# COMMAND ----------

datetime.time(datetime.now()) # doar ora

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ex. 1

# COMMAND ----------

# MAGIC %md
# MAGIC Sa se afiseze varsta dvs in zile si secunde (puteti folosi si o zi de nastere "fake"; o pretinsa zi de nastere; pt GDPR)

# COMMAND ----------

zi_nastere = datetime(2002,2,4)

# COMMAND ----------

# MAGIC %md
# MAGIC Sa se afiseze data si timpul la care varsta dvs va fi cu 100 de zile, 100 de minute si 100 de secunde mai mare. 

# COMMAND ----------

viitor = datetime.now() - zi_nastere + timedelta(days=100, hours=0, minutes = 100, seconds=100)

print(viitor)

# COMMAND ----------

# MAGIC %md
# MAGIC Scrieti o functie care returneaza data calendaristica si ora in doua variabile separate, avand ca parametru o variabila de tip datetime.

# COMMAND ----------

def timp(rn):
    data_calend = rn.date()
    ora = rn.hour

    return data_calend, ora

# COMMAND ----------

# MAGIC %md
# MAGIC Apelati functia de mai sus pentru data si timpul curent (now).

# COMMAND ----------

rn = datetime.now()

data, ora = timp(rn)

print(f"Data: ", data)
print(f"Ora: ", ora)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Conversie datetime-> string

# COMMAND ----------

str(acum)

# COMMAND ----------

acum.strftime("%d/%m/%Y - %w- %H") #format de tiparire Testati si: %y, %h, %w (a cata zi a saptamanii), %H, %I
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC # Ex.2 

# COMMAND ----------

# MAGIC %md
# MAGIC Afisati data de azi in formatul  
# MAGIC
# MAGIC Monday, April 03, 2023 - 10:02 AM

# COMMAND ----------

azi = datetime.now()
azi

azi.strftime("%A, %B %d, %Y - %I:%M %p")

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ### Conversie string ->datetime

# COMMAND ----------

azi = '03/30/2025'

# COMMAND ----------

zi1 = datetime.strptime(azi, '%m/%d/%Y')  # am precizat formatul datei
zi1

# COMMAND ----------

# MAGIC %md
# MAGIC Exista functii si biblioteci care recunosc multe formate. De exemplu, functia **parse**.

# COMMAND ----------

from dateutil.parser import parse

# COMMAND ----------

parse(azi)

# COMMAND ----------

parse('20:30:00')

# COMMAND ----------

parse('1 April 2023 11:50 PM')

# COMMAND ----------

azi = '1/4/23' # 1 aprilie - ZIUA PACALELII!
parse(azi)  #  considera ca este 4 ianuarie

# COMMAND ----------

parse(azi, dayfirst = True)  # intr-adevar 1 aprilie

# COMMAND ----------

# MAGIC %md
# MAGIC Putem folosi si to_datetime.

# COMMAND ----------

import pandas as pd
pd.to_datetime('1 April 2023 11:50 PM')
 

# COMMAND ----------

pd.to_datetime('1/4/23', dayfirst=True)

# COMMAND ----------

# MAGIC %md
# MAGIC # Ex. 3.

# COMMAND ----------

# MAGIC %md
# MAGIC Transformati stringul urmator in obiect de tipul datetime:
# MAGIC
# MAGIC
# MAGIC Monday, April 03, 2023 - 10:02 AM

# COMMAND ----------

str_date = ('Monday, April 03, 2023 - 10:02 AM')

dt = pd.to_datetime(str_date)

# COMMAND ----------

# MAGIC %md
# MAGIC Afisati data si ora pentru obiectul datetime de mai sus.

# COMMAND ----------

 
print(dt.date())
print(dt.hour)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Serii de timp

# COMMAND ----------

# MAGIC %md
# MAGIC O serie de timp este o colectie de date (informatii) indexate dupa data (si ora, eventual). O serie de observatii inregistrate in timp.
# MAGIC
# MAGIC De exemplu, 
# MAGIC - inregistrarea temperaturii aerului dintr-o anumita zona - zilnic sau din ora in ora.
# MAGIC - inregistrarea plecarilor sau sosirilor unui tren
# MAGIC - inregistrarea pozitiei in timp a unui obiect
# MAGIC - inregistrarea pretului unui produs in decursul unei luni
# MAGIC - etc.

# COMMAND ----------

# MAGIC %md
# MAGIC Vom crea DataFrame cu DateTimeIndex

# COMMAND ----------

# MAGIC %md
# MAGIC Generam intai un DateTimeIndex folosind functia date_range

# COMMAND ----------

dt_index1 = pd.date_range("2023-01-01", "2023-02-28") # observati ca sunt incluse si capetele; frecventa este "D" daily implicit
dt_index1

# COMMAND ----------

dt_index2 = pd.date_range(datetime.date(datetime.now()) - timedelta(4), datetime.date(datetime.now()))
dt_index2

# COMMAND ----------

pd.date_range("2023-01-01", periods=6) # periods = nr de indici care se formeaza; dimensiunea vectorului DateTimeIndex
                                       # implicit freq = 'D' daily

# COMMAND ----------

pd.date_range("2023-03-01", periods=6, freq='5D')

# COMMAND ----------

pd.date_range("2023-03-01", periods=6, freq='12H')

# COMMAND ----------

dt_index3 = pd.date_range("2025-03-01", periods=7, name = "Prima sapt primavara")
dt_index3

# COMMAND ----------

# MAGIC %md
# MAGIC Generam un dataframe cu acest index. 

# COMMAND ----------

df_1 = pd.DataFrame(np.random.randint(0, 15,7), index = dt_index3, columns = ['Temp'])
df_1

# COMMAND ----------

# MAGIC %md
# MAGIC # Ex.4 

# COMMAND ----------

# MAGIC %md
# MAGIC Generati urmatorul dataframe cu index de tip Timeindex. Valorile de pe coloane sunt intregi generate aleator cu valori in intervalul [10, 49].
# MAGIC

# COMMAND ----------

date_ex4 = pd.date_range(start="2025-03-01", end="2025-03-10")
values_ex4 = np.random.randint(10, 50, size=(len(date_ex4), 3))
dt_ex4 = pd.DataFrame(values_ex4, index=date_ex4, columns=["X", "Y", "Z"])
dt_ex4

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC Generam un alt dataframe cu doua atribute, denumite A si B si index de tip Timeindex.

# COMMAND ----------

df_2 = pd.DataFrame( np.random.randn(5, 2)*10,
    index=pd.date_range("2025-03-01", periods=5, freq='12H'),
    columns=list("AB"))
df_2

# COMMAND ----------

# MAGIC %md
# MAGIC Adaugam o coloana noua C. Acelasi index.

# COMMAND ----------

df_2['C'] = pd.Series(np.array([12, 29, 43, 56, 77]), index = pd.date_range("2025-03-01", periods=5, freq='12H'))
df_2

# COMMAND ----------

df_2.index

# COMMAND ----------

# MAGIC %md
# MAGIC Revenim la primul dataframe.

# COMMAND ----------

df_1

# COMMAND ----------

# MAGIC %md
# MAGIC Accesam elementele de pe coloana Temp.

# COMMAND ----------

df_1['Temp'][dt_index3[0]]

# COMMAND ----------

df_1['Temp']['2025-03-04']


# COMMAND ----------

df_1.loc['2025-03-04']

# COMMAND ----------

df_1['2025-03-04':'2025-03-07']

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC # Ex.5.

# COMMAND ----------

# MAGIC %md
# MAGIC Plecand de la dataframe-ul de la ex. 4

# COMMAND ----------

# MAGIC %md
# MAGIC Sa se acceseze elementele de pe coloana Y

# COMMAND ----------

print(dt_ex4)

dt_ex4['Y']

# COMMAND ----------

# MAGIC %md
# MAGIC Sa se acceseze elementele din data de 05.03.2023

# COMMAND ----------

dt_ex4.loc['2025-03-05']

# COMMAND ----------

# MAGIC %md
# MAGIC Sa se modifice valoarea atributului Z din data de 07.03.2023 in 100. 

# COMMAND ----------

dt_ex4.loc['2025-03-05','Z'] = 100

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC Revenim la fisierul csv generat cu Google Trends din notebook-ul Vizualizare. Il incarcam astfel incat generam o dataframe cu index coloana Time.
# MAGIC
# MAGIC La citire parsam si atributul Time.

# COMMAND ----------

df_alegeri = pd.read_csv("multiTimeline.csv", index_col=0, parse_dates=True)
df_alegeri

# COMMAND ----------

# MAGIC %md
# MAGIC Reprezentare grafica a intregii colectii.

# COMMAND ----------

df_alegeri.plot()

# COMMAND ----------

df_alegeri.loc['2025-03-24'] # selectarea tuturor randurilor cu indicele '2025-03-24'

# COMMAND ----------

df_alegeri.loc['2025-03-24':'2025-03-24'] # selectarea tuturor randurilor cu indicii de la  '2025-03-24' la '2025-03-25'

# COMMAND ----------

df_alegeri.loc['2025-03-28'].plot()

# COMMAND ----------

# MAGIC %md
# MAGIC Acelasi grafic se obtine si astfel:

# COMMAND ----------

df_alegeri['2025-03-24':'2025-03-25'].plot()

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC # Ex.6.

# COMMAND ----------

# MAGIC %md
# MAGIC Plecand de la dataframe-ul de la ex. 4

# COMMAND ----------

# MAGIC %md
# MAGIC Reprezentati grafic toata colectia.

# COMMAND ----------

dt_ex6 = dt_ex4

dt_ex6.plot()

dt_ex6

# COMMAND ----------

# MAGIC %md
# MAGIC Reprezentati grafic colectia de la 03.03 - 06.03

# COMMAND ----------

dt_ex6['03-03-2025':'06-03-2025'].plot()

# COMMAND ----------

# MAGIC %md
# MAGIC Reprezentati grafic colectia de la 03.03 - 06.03 in 3 subplot-uri, pe aceeasi linie, cate unul pe coloana, cate un atribut in fiecare subplot.

# COMMAND ----------

#

# COMMAND ----------

