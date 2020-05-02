import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


mod=LinearRegression()
data = pd.read_excel('cours.xls',index_col='DATE',parse_dates=True)
data = data.dropna(axis=0)
y = data['COURS']
X = data.drop('COURS',axis=1)

mod.fit(X,y)
mod.score(X,y)

A=mod.predict(X)

B=A.reshape(1101, 1)

pointMax=B.max()
pointMin=B[-200]
print("L'euros va se negocier autour de", pointMin, "et de", pointMax,"Ariary")
