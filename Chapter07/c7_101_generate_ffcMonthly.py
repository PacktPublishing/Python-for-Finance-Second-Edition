# still one issue index should be the date!!!!



import pandas as pd
import scipy as sp
import numpy as np
file=open("c:/temp/ffMom.txt","r")
data=file.readlines()

f=[]
dd=[]
n=sp.size(data)-1
for i in sp.arange(14,n):
    t=data[i].split()
    dd.append(pd.to_datetime(t[0]+'01', format='%Y%m%d').date())
    f.append(float(t[1])/100)


mom=pd.DataFrame(f,index=dd,columns=['MOM'])
import pandas as pd
ff3=pd.read_pickle('c:/temp/ffMonthly.pkl')
ff3['DATE']=ff3.index
mom['DATE']=mom.index
a=pd.merge(ff3,mom)
ffc=pd.DataFrame(a[['DATE','MKT_RF','SMB','HML','MOM','RF']])
ffc.to_pickle("c:/temp/ffcMonthly.pkl")
