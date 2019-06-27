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
print y_mean[:10]
print data.head()


data["SSR"]=(data["y_prediccion"]-np.mean(y_act))**2
data["SSD"]=(data["y_prediccion"]-data["y_actual"])**2
data["SST"]=(data["y_actual"]-np.mean(y_act))**2
print data.head()
SSD=sum(data["SSD"])
SSR=sum(data["SSR"])
SST=sum(data["SST"])
R2=SSR/SST
print R2

print "\n\nOBTENIENDO LA RECTA DE REGRESION LINEAL\n\n"

x_mean=np.mean(data["x"])
y_mean=np.mean(data["y_actual"])
print "x promedio::", x_mean
print "y promedio::",y_mean

data["beta_n"]=(data["x"]-x_mean)*(data["y_actual"]-y_mean)
data["beta_d"]=(data["x"]-x_mean)**2
beta=sum(data["beta_n"])/(sum(data["beta_d"]))
alpha=y_mean-beta*x_mean

print "beta::",beta
print "alpha::",alpha

data["y_model"]=alpha+beta*data["x"]

print data.head()

SSR=sum((data["y_model"]-y_mean)**2)
SSD=sum((data["y_model"]-data["y_actual"])**2)
SST=sum((data["y_actual"]-y_mean)**2)
R_2=SSR/SST

print "\n\ny=5.073709294705427+1.92596091515x\n\n"
print "imprimiendo el nuevo valor de r2::",R_2

y_mean=[np.mean(y_act) for i in range(1,len(x_list)+1)]

plt.plot(data["x"],data["y_prediccion"])
plt.plot(data["x"],data["y_actual"],"ro")
plt.plot(data["x"],y_mean,"g")
plt.plot(data["x"],data["y_model"])
plt.title("Valor Actual vs Prediccion")

RSE=np.sqrt(SSD/(len(data)-2))

print "RSE::",RSE

plt.show()
