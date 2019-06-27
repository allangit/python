import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df=pd.read_csv("titanic3.csv")

print df.head()
print df.shape
print df.columns.values
print df.describe()

df2=df.dropna(axis=0, how="all")
print df2
df3=df.dropna(axis=0,how="any")
print df3
df4=df.fillna(0)
print df4
df5=df.fillna("Desconocido")
print df5
df6=df["body"].fillna(0)
print df6
df7=pd.isnull(df["age"]).values.ravel().sum()
print df7
df8=df["age"].fillna(df["age"].mean())
print df8
df9=pd.get_dummies(df["sex"],prefix="sex")
print df9.head()
columns=df.columns.values.tolist()
print columns
columna=df.drop(["sex"],axis=1)
print columna.head()
data_new=pd.concat([columna,df9],axis=1)
print data_new
