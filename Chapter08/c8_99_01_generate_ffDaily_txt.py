# generate ff_monthly.pickle   

import pandas as pd
import scipy as sp
import numpy as np
file=open("c:/temp/ffDaily.txt","r")
data=file.readlines()
f=[]
dd=[]
for i in range(5,sp.size(data)):
       t=data[i].split()
       dd.append(pd.to_datetime(t[0], format='%Y%m%d').date())
       for j in range(1,5):
           k=float(t[j])
           f.append(k/100)
n=len(f)       
f1=np.reshape(f,[n/4,4])
ff=pd.DataFrame(f1,index=dd,columns=['MKT_RF','SMB','HML','RF'])
ff.to_pickle("c:/temp/ffDaily.pkl")

