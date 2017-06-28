"""
  Name     : c4_13_generate_ffMonthly_txt2.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np
import pandas as pd
#
file=open("c:/temp/ffMonthly.txt","r")
data=file.readlines()
dd=[]    # should not use dd=mkt=smb=hml=rf=[]!!!!!
mkt=[]
smb=[]
hml=[]
rf=[]
n=len(data)
index=range(1,n-3)

for i in range(4,n):
    t=data[i].split()
    dd.append(pd.to_datetime(t[0]+'01', format='%Y%m%d').date())
    mkt.append(float(t[1])/100)
    smb.append(float(t[2])/100)
    hml.append(float(t[3])/100)
    rf.append(float(t[4])/100)
    
d=np.transpose([dd,mkt,smb,hml,rf])
ff=pd.DataFrame(d,index=index,columns=['DATE','MKT_RF','SMB','HML','RF'])
ff.to_pickle("c:/temp/ffMonthly.pkl")

