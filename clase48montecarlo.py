import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print "\n\nSimulacion del metodo montecarlo\n\n"

pi_avg=0
pi_value_list=[]
n=100
exp=2000
for i in range(exp):

	value=0
	x=np.random.uniform(0,1,n).tolist()
	y=np.random.uniform(0,1,n).tolist()
	for j in range(n):

		z=np.sqrt(x[j]*x[j]+y[j]*y[j])
		if z<=1:
			value+=1

	float_value=float(value)
	pi_value=float_value*4/n
	pi_value_list.append(pi_value)
	pi_avg+=pi_value

pi=pi_avg/exp
print pi
plt.plot(pi_value_list)
plt.show()
