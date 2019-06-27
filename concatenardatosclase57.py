
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("winequality-red.csv",sep=";")
print df.head()
print df.columns.values
print df.shape

df2=pd.read_csv("winequality-white.csv",sep=";")
print df2.head()
print df2.shape

df3=pd.concat([df,df2],axis=0)
print df3.columns.values
print df3.head()

df4=df3[300:320]
print df4

df5=df3.head(10)
print df5

df6=df3.tail()
print df6


total=pd.concat([df4,df5,df6], axis=0)
print total
