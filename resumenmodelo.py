import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from sklearn.feature_selection import RFE
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression



data=pd.read_csv("Advertising.csv")
print data.head()
feature_cols=["TV","Radio","Newspaper"]
x=data[feature_cols]
y=data["Sales"]

estimador=SVR(kernel="linear")
selector=RFE(estimador,2,step=1)
selector=selector.fit(x,y)
print selector.support_
print selector.ranking_

X_pred=x[["TV","Radio"]]
lm=LinearRegression()
lm.fit(X_pred,y)
print lm.intercept_
print lm.coef_
print lm.score(X_pred,y)
