import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("001.csv")
print df.head()


for i in range(2,3333):

	if i<10:

		filename="00"+str(i)
	if 10 <= i <20:

		filename="0"+str(i)

	file=filename+".csv"
	df2=pd.read_csv(file)
	data=pd.concat([df,df2],axis=0)
print data.head()
print data.shape
