import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

data=pd.read_csv("Advertising.csv")
print data.head()
lm=smf.ols(formula="Sales~TV",data=data).fit()
parametros=lm.params
print parametros
p_valores=lm.pvalues
print p_valores
r2=lm.rsquared
print r2
resumen=lm.summary()
print resumen

sales_pred=lm.predict(pd.DataFrame(data["TV"]))
print sales_pred.head()
data.plot(kind="scatter",x="TV",y="Sales")
plt.plot(pd.DataFrame(data["TV"]),sales_pred,c="red",linewidth=2)
data["sales_pred"]=7.03+0.047537*data["TV"]
data["RSE"]=(data["Sales"]-data["sales_pred"])**2
SSD=sum(data["RSE"])
RSE=np.sqrt(SSD/(len(data)-2))
print RSE
print data.head()
sales_m=np.mean(data["Sales"])
print sales_m
error=RSE/sales_m
print error

print"\n\n\nModelado Regresion Multiple\n\n\n"

lm2=smf.ols(formula="Sales~TV+Newspaper",data=data).fit()
parametros2=lm2.params
pvalues_2=lm2.pvalues
sales_2=lm2.predict(data[["TV","Newspaper"]])
print sales_2
print pvalues_2
print parametros2


print"\n\n\nModelado Regresion Multiple add radio\n\n\n"

lm3=smf.ols(formula="Sales~TV+Radio",data=data).fit()
sales_pred3=lm3.predict(data[["TV","Radio"]])
SSD=sum((data["Sales"]-sales_pred3)**2)
RSE=np.sqrt(SSD/(len(data)-2-1))
print RSE
print RSE/sales_m
print lm3.summary()


print "\n\n ADD todo el modelos\n\n"

lm4=smf.ols(formula="Sales~TV+Radio+Newspaper",data=data).fit()
print lm4.summary()

print "\nproblema de multicolinialidad de los datos\n"
print "si VIF=1 no estan correlacionadas\n"
print "si VIF < 5 tiene correlacion moderada y pueden quedar en modelo\n"
print "si VIF >5 Estan altamente correlacionadas y deben desaparecer del modelo\n"

lm_n=smf.ols(formula="Newspaper~TV+Radio",data=data).fit()
rsquared_n=lm_n.rsquared
VIF_n=1/(1-rsquared_n)
print VIF_n

lm_tv=smf.ols(formula="TV~Newspaper+Radio",data=data).fit()
rsquared_tv=lm_tv.rsquared
VIF_tv=1/(1-rsquared_tv)
print VIF_tv

lm_radio=smf.ols(formula="Radio~TV+Newspaper",data=data).fit()
rsquared_radio=lm_radio.rsquared
VIF_radio=1/(1-rsquared_radio)
print VIF_radio





plt.show()
