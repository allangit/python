import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


for x in range (0,12,1):

	dato=np.random.randint(1,100)
	print dato
for y in range (0,12,1):

	datox=np.random.random()
	print datox

def generate_num(n,a,b):

	x=[]
	for i in range(n):

		x.append(np.random.randint(a,b))

	return x

print generate_num(25,1,50)
