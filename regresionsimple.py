import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

data=pd.read_csv("Advertising.csv")
print data.head()

lm=smf.ols(formula="Sales~TV",data=data).fit()
parametros=lm.params
print parametros
p_valor=lm.pvalues
print p_valor
R2=lm.rsquared
print R2
Rajust=lm.rsquared_adj
print Rajust
resumen=lm.summary()
print resumen

sales_pred=lm.predict(pd.DataFrame(data["TV"]))
print sales_pred.head()
print data.head()
data.plot(kind="scatter", x="TV", y="Sales")
plt.plot(pd.DataFrame(data["TV"]),sales_pred,c="red",linewidth=2)


data["sales_pred"]=7.032+0.047*data["TV"]
SSD=sum((data["Sales"]-data["sales_pred"])**2)
RSE=np.sqrt(SSD/(len(data)-2))
sales_mean=np.mean(data["Sales"])
error=RSE/sales_mean
print RSE,sales_mean, error
plt.show()
