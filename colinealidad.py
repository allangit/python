

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

data=pd.read_csv("Advertising.csv")
print data.head()

lm_n=smf.ols(formula="Newspaper~TV+Radio",data=data).fit()
rsquared_n=lm_n.rsquared
VIF=1/(1-rsquared_n)
print "rs_quared::",rsquared_n
print "VIF::",VIF


lm_tv=smf.ols(formula="TV~Newspaper+Radio",data=data).fit()
rsquared_tv=lm_tv.rsquared
VIF=1/(1-rsquared_tv)
print "rs_quared::",rsquared_tv
print "VIF::",VIF



lm_r=smf.ols(formula="Radio~Newspaper+TV",data=data).fit()
rsquared_r=lm_r.rsquared
VIF=1/(1-rsquared_r)
print "rs_quared::",rsquared_r
print "VIF::",VIF





