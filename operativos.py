
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

data=pd.read_csv("alanoperativos.csv")
print data.head()
print data.values
print data.shape
print data[["Fecha  Incidencia", "Tiempo reduccion",  "Tiempo a reintegrar",  "Semana"]]
