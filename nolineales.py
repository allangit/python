import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from sklearn.feature_selection import RFE
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression





data=pd.read_csv("auto-mpg.csv")
print data.head()
print data.shape
data["mpg"]=data["mpg"].dropna()
data["horsepower"]=data["horsepower"].dropna()
plt.plot(data["horsepower"],data["mpg"],"ro")
plt.title("HORSEPOWER VS MPG")
plt.xlabel("horsepower")
plt.ylabel("MPG")

x=data["horsepower"].fillna(np.mean(data["horsepower"]))
y=data["mpg"].fillna(np.mean(data["mpg"]))
x_data=x[:,np.newaxis]
print x_data
lm=LinearRegression()
lm.fit(x_data,y)
plt.plot(x,y,"ro")
plt.plot(x,lm.predict(x_data))

plt.show()
