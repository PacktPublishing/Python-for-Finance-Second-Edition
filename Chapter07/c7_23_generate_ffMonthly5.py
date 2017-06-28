"""
  Name     : c7_23_generate_ffMonthly5.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import pandas as pd
import scipy as sp
import numpy as np
file=open("c:/temp/ffMonthly5.txt","r")
data=file.readlines()

f=[]
dd=[]
n=sp.size(data)-1
for i in sp.arange(14,n):
    t=data[i].split()
    dd.append(pd.to_datetime(t[0]+'01', format='%Y%m%d').date())
    f.append(float(t[1])/100)

"""
mom=pd.DataFrame(f,index=dd,columns=['MOM'])
import pandas as pd
ff3=pd.read_pickle('c:/temp/ffMonthly.pkl')
ff3['DATE']=ff3.index
mom['DATE']=mom.index
a=pd.merge(ff3,mom)
ff4=pd.DataFrame(a[['DATE','MKT_RF','SMB','HML','MOM','RF']])


#ff.to_pickle("c:/temp/ffMonthly5.pkl")
"""
