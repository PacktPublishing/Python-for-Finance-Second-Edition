import pandas as pd
import scipy as sp
x=pd.read_csv("c:/temp/GDP_Yan.csv",skiprows=10)
n=len(x)
ddate=[]
a=[]
k=1
for i in sp.arange(n):
    y=sp.array(x[i:(i+1)])
    ddate.append( pd.to_datetime(y[0,0]).date())
    a.append(y[0,1])
    #print(y)

GDP=pd.DataFrame(a,columns=['AdjustedGDPannualBillion'],index=ddate)
GDP.to_pickle("c:/temp/usGDPquarterly.pkl")
