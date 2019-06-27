import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


check=[]
check2=[]
data=pd.read_csv("CustomerChurnModel.txt")
print data.shape
a=np.random.randn(len(data))

for i in range(len(data)):

	if a[i] <0.8:

		check.append(a[i])
	else:

		check2.append(a[i])

print len(check)
print len(check2)

train,test=train_test_split(data, test_size=0.2)

print len(train)
print len(test)
