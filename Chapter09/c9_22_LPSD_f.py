"""
  Name     : c9_22_LPSD.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""



import scipy as sp
import numpy as np

mean=0.15;
Rf=0.01
std=0.20
n=200
sp.random.seed(3412)
x=sp.random.normal(loc=mean,scale=std,size=n)


def LPSD_f(returns, Rf):
    y=returns[returns-Rf<0]  
    m=len(y)
    total=0.0
    for i in sp.arange(m):
        total+=(y[i]-Rf)**2
    return total/(m-1)

answer=LPSD_f(x,Rf)
print("LPSD=",answer)
