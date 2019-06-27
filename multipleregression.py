import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

data=pd.read_csv("Advertising.csv")
print data.head()

lm=smf.ols(formula="Sales~TV+Newspaper",data=data).fit()
parametros=lm.params
p_valores=lm.pvalues
sales_pred=lm.predict(data[["TV","Newspaper"]])
SSD=sum((data["Sales"]-sales_pred)**2)
RSE=np.sqrt(SSD/(len(data)-2-1))
sales_mean=np.mean(data["Sales"])
error=RSE/sales_mean
print "error",error
print sales_pred
print p_valores
print parametros

print "\n\nHaciendo el estudio con TV, Radio\n"

lm2=smf.ols(formula="Sales~TV+Radio",data=data).fit()
parametros2=lm2.params
p_valores=lm2.pvalues
sales_pred2=lm2.predict(data[["TV","Radio"]])
SSD=sum((data["Sales"]-sales_pred2)**2)
RSE=np.sqrt(SSD/(len(data)-2-1))
sales_mean=np.mean(data["Sales"])
error=RSE/sales_mean
print "error",error
print "sales_pred2", sales_pred2
print "p_valores", p_valores
print "parametros2",parametros2
print lm2.summary()

