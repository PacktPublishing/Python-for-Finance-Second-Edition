# generate ff_monthly.pickle   

import pandas as pd
import scipy as sp
import numpy as np
file=open("c:/temp/ffMonthly5.txt","r")
data=file.readlines()
f=[]
dd=[]
for i in range(4,sp.size(data)):
       t=data[i].split()
       dd.append(pd.to_datetime(t[0]+'01', format='%Y%m%d').date())
       for j in range(1,7):
           k=float(t[j])
           f.append(k/100)
n=len(f)       
f1=np.reshape(f,[n/6,6])
ff=pd.DataFrame(f1,index=dd,columns=['MKT_RF','SMB','HML','RMW','CMA','RF'])
ff.to_pickle("c:/temp/ffMonthly5.pkl")


