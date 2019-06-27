import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

data=pd.read_csv("Advertising.csv")
print data.head()

a=np.random.randn(len(data))
check=(a<0.8)
training=data[check]
testing=data[~check]

print len(training),len(testing)

lm=smf.ols(formula="Sales~TV+Radio",data=training).fit()
print lm.summary()
print "2.8190 +2.8190*data[TV]+0.1948*data[Radio]"
sales_pred=lm.predict(testing)
print sales_pred

SSD=sum((testing["Sales"]-sales_pred)**2)
RSE=np.sqrt(SSD/(len(testing)-2-1))
sales_mean=np.mean(testing["Sales"])
error=RSE/sales_mean

print "SSD",SSD
print "RSE",RSE
print "Sales_mean",sales_mean
print "Error",100*error,"%"
