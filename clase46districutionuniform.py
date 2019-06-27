import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


a=1
b=100
c=20000
data=np.random.uniform(a,b,c)

#plt.hist(data)

print "\n\nDistribucion normal de gauss\n\n"

data2=np.random.randn(100)
x=range(1,101)
plt.plot(x,data2)

plt.show()
