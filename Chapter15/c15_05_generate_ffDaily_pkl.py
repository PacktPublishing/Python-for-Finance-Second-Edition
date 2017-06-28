"""
  Name     : c15_05_generate_ffDaily_pkl.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import datetime
import numpy as np
import pandas as pd 
file=open("c:/temp/ffDaily.txt","r") 
data=file.readlines()
f=[]
index=[]
#
for i in range(5,np.size(data)): 
    t=data[i].split() 
    t0_n=int(t[0]) 
    y=int(t0_n/10000) 
    m=int(t0_n/100)-y*100 
    d=int(t0_n)-y*10000-m*100
    index.append(datetime.datetime(y,m,d)) 
    for j in range(1,5):
         k=float(t[j]) 
         f.append(k/100)
#
n=len(f) 
f1=np.reshape(f,[n/4,4])
ff=pd.DataFrame(f1,index=index,columns=['Mkt_Rf','SMB','HML','Rf'])
ff.to_pickle("c:/temp/ffDaily.pkl")
