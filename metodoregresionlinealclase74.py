import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x=1.5+2.5*np.random.randn(100)
res=0+0.8*np.random.randn(100)
y_pred=5+1.9*x
print y_pred[:30]
y_act=5+1.9*x+res

x_list=x.tolist()
y_pred_list=y_pred.tolist()
print y_pred_list[:30]
y_actual_list=y_act.tolist()


data=pd.DataFrame (

	{
		"x":x_list,
		"y_actual":y_actual_list,
		"y_prediccion":y_pred_list
	}
)

y_mean=[np.mean(y_act) for i in range(1,len(x_list)+1)]

print data.head()
plt.plot(x,y_pred)
plt.plot(x,y_act,"ro")
plt.plot(x,y_mean,"g")
plt.title("Valor Actual vs Prediccion")

data["SSR"]=(data["y_prediccion"]-np.mean(y_act))**2
data["SSD"]=(data["y_prediccion"]-data["y_actual"])**2
data["SST"]=(data["y_actual"]-np.mean(y_act))**2
print data.head()
SSD=sum(data["SSD"])
SSR=sum(data["SSR"])
SST=sum(data["SST"])
R2=SSR/SST
print "SSD:",SSD
print "SSR:",SSR
print "SST",SST
print "R2",R2

print"\n\nEvaluando los coeficientes de metodo de regresion logistica\n\n"


plt.plot(data["SSD"])
plt.plot(data["SSR"])
plt.plot(data["SSD"])
plt.show()
