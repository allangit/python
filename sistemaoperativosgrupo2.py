# -*- encoding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("grupoviernes.csv")
df["Examen1"]=0
df["Examen2"]=0
df["Examen3"]=30
df["Quiz1"]=0
df["Quiz2"]=40
df["tarea1"]=0
df["Tarea2"]=0
df["Proyecto1"]=0
df["Proyecto2"]=0
df["notaFinal"]=0.6*df["Examen1"] +df["Examen2"] +df["Examen3"]+df["Quiz1"]+ df["Quiz2"] +df["tarea1"]+df["Tarea2"]
print df
print "\n\n"
print df[df["Nombre"]=="KATHERINE ANDREA"]
