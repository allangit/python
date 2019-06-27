import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

data=pd.read_csv("Advertising.csv")
print data.head()
a=np.random.randn(len(data))

check=(a<0.8)
training=data[check]
testing=data[~check]
print "training::",len(training)
print "testing::",len(testing)
print "data::",len(data)
lm=smf.ols(formula="Sales~TV+Radio",data=training).fit()
parametros=lm.params
print lm.summary()

sales_pred=lm.predict(testing)
print sales_pred
SSD=sum((testing["Sales"]-sales_pred)**2)
RSE=np.sqrt(SSD/(len(testing)-2-1))
sales_mean=np.mean(testing["Sales"])
error=RSE/sales_mean

print error

plt.show()
