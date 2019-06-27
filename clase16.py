import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data=pd.read_csv("CustomerChurnColumns.csv")
print data.head()
print data.shape
print data.columns.values
data_cols=data["Column_Names"].tolist()
print data_cols
