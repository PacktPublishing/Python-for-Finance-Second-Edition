"""
  Name     : c7_24_generateffmonMonthly.py
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
mom.to_pickle("c:/temp/ffMomMonthly.pkl")
