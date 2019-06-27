import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from sklearn.feature_selection import RFE
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression


data=pd.read_csv("auto-mpg.csv")
print data.head()
data["horsepower"]=data["horsepower"].dropna()
data["mpg"]=data["mpg"].dropna()
plt.plot(data["horsepower"],data["mpg"],"ro")
plt.title("CCV vs MPG")
plt.xlabel("HORSEPOWER")
plt.ylabel("MPG")

print "\nprimer modelo lineal :: mpg=a+b*horsepower"


x=data["horsepower"].fillna(np.mean(data["horsepower"]))
y=data["mpg"].fillna(np.mean(data["mpg"]))
x_data=x[:,np.newaxis]
lm=LinearRegression()
lm.fit(x_data,y)
plt.plot(x,y,"ro")
plt.plot(x,lm.predict(x_data),color="blue")

print "\nSegundo modelo cuadratico :: mpg=a+b*horsepower**2"

x_data=x**2
x_data=x_data[:,np.newaxis]
lm=LinearRegression()
lm.fit(x_data,y)
print lm.score(x_data,y)
SSD=np.sum((y-lm.predict(x_data))**2)
RSE=np.sqrt(SSD/(len(x_data)-1))
y_mean=np.mean(y)
error=RSE/y_mean

print SSD,RSE,y_mean,error*100
plt.show()
