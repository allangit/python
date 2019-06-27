import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=open("CustomerChurnModel.txt","r")
cols=data.readline().strip().split(",")
n_cols=len(cols)

counter=0
main_dict={}

for col in cols:

	main_dict[col]=[]

print main_dict

for line in data:

	values=line.strip().split(",")
	for i in range(n_cols):

		main_dict[cols[i]].append(values[i])
	counter+=1

print counter,n_cols

df3=pd.DataFrame(main_dict)
print df3.head()
