import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_csv("Medals.csv")
print data.head()
data2=data["Athlete"].unique().tolist()
print len(data2)

data3=pd.read_csv("Athelete_Country_Map.csv")
print data3.head()
print len(data3)

print data3[data3["Athlete"]=="Aleksandar Ciric"]
print data3.head()

data4=pd.read_csv("Athelete_Sports_Map.csv")
print len(data4)

data5=data4[(data4["Athlete"]=="Cheng Jing")| (data4["Athlete"]=="Richard Thompson")|(data4["Athlete"]=="Matt Ryan")]
print data5


data_country_dp=data.drop_duplicates(subset="Athlete")
print len(data_country_dp)


data_merge=pd.merge(left=data, right=data3, left_on="Athlete", right_on="Athlete")
print data_merge.head()
print data_merge.shape
print data_merge[data_merge["Athlete"]=="Aleksandar Ciric"]


data_merge2=pd.merge(left=data, right=data_country_dp, left_on="Athlete", right_on="Athlete")
print data_merge2.head()
print data_merge2.shape
print data_merge2[data_merge2["Athlete"]=="Aleksandar Ciric"]

print"\n\nEliminando los duplicados de Athlete Sport Maps\n\n"

data_sport_dp=data4.drop_duplicates(subset="Athlete")
print len(data_sport_dp)
data_merge3=pd.merge(left=data, right=data_sport_dp, left_on="Athlete", right_on="Athlete")
print data_merge3.head()
