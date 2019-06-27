import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

data=pd.read_csv("Advertising.csv")
print data.head()
a=np.random.randn(len(data))
check= (a<0.8)
training=data[check]
testing=data[~check]

print len(data),len(training), len(testing)
lm=smf.ols(formula="Sales~Radio+TV",data=training).fit()
print lm.summary()

print "\nValidando el modelo\n"
sales_pred=lm.predict(testing)
print sales_pred
SSD=sum((testing["Sales"]-sales_pred)**2)
print SSD
RSE=np.sqrt(SSD/(len(testing)-2-1))
print RSE
sales_mean=np.mean(testing["Sales"])
error=RSE/sales_mean
print error
