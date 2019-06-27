import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("CustomerChurnModel.txt")
print df.head()
df2=df["Account Length"]
print df2.head()
df3=df[["Account Length",  "Phone",  "Eve Charge",  "Day Calls"]]
print df3.head()
desired_columns=["Account Length",  "Phone",  "Night Calls"]
df4=df[desired_columns]
print df4.head()
df5=df[10:35]
print df5

print "\nfiltrando total mins > 500\n"

df6=df[df["Day Mins"]>300]
print df6
print "\nfiltrando por estado\n"
df7=df[df["State"]=="NY"]
print df7
print "\nfiltrando por estado\n"
df8=df[(df["State"]=="NY") & (df["Day Mins"]>300)]
print df8

print "\n\nFiltrando por columnas y filas"

df9=df[["Account Length",  "Phone",  "Night Calls"]][:100]
print df9
print "\n\nFiltrando por columna y fila mismo vector"
print "\n\nPrimero Fila y despues Columna"
df_1=df.iloc[1:10, 3:6]
print df_1

print "\n\nAccediendo por posicion usar iloc\n\n"
df_2=df.iloc[:10, [3,5,7] ]
print df_2

print "\n\nAccediendo por etiqueta  usar loc\n\n"

df_3=df.loc[[1,5,8,36],["Account Length",  "Phone",  "Night Calls"]]
print df_3

df["Total Mins"]=df["Day Mins"]+df["Night Mins"] +df["Eve Calls"]
print df.head()
print df.shape
