import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("CustomerChurnModel.txt")
print df.head()
df.plot(kind="scatter", x="Day Mins", y="Day Charge")
df.plot(kind="scatter",x="Night Mins", y="Night Charge")
figure,axs=plt.subplots(2,2,sharex=True, sharey=True)
df.plot(kind="scatter",x="Day Mins", y="Day Charge",ax=axs[0][0])
df.plot(kind="scatter",x="Night Mins", y="Night Charge",ax=axs[0][1])
df.plot(kind="scatter",x="Day Calls", y="Day Charge",ax=axs[1][0])
plt.hist(df["Day Calls"],bins=10)


plt.show()
