import pandas as pd
import scipy as sp
import numpy as np
file=open("c:/temp/ffMonthly.txt","r")
data=file.readlines()
f=[]
index=[]
for i in range(4,sp.size(data)):
       t=data[i].split()
       index.append(int(t[0]))
       for j in range(1,5):
           k=float(t[j])
           f.append(k/100)
n=len(f)       
f1=np.reshape(f,[n/4,4])
ff=pd.DataFrame(f1,index=index,columns=['MKT_RF','SMB','HML','RF'])
ff.to_pickle("c:/temp/ffMonthly.pkl")


