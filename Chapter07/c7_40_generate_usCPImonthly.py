"""
  Name     : c7_40_generate_usCPImonthly.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy as sp
import pandas as pd
#
x=pd.read_csv("c:/temp/CPI_19jan2017.csv",skiprows=8)
n=len(x)

ddate=[]
cpi0=[]
k=1
for i in sp.arange(n):
    y=sp.array(x[i:(i+1)])
    for j in sp.arange(12):
        ddate.append(y[0,0]*100+j+1)
        cpi0.append(y[0,j+1]/100)
    #print(y)

cpi=pd.DataFrame(cpi0,index=ddate)
cpi.to_pickle("c:/temp/usCPImonthly.pkl")