"""
  Name     : c13_08_KMF_function.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 2/27/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp
import pandas as pd
import scipy.stats as stats
from scipy import log,sqrt,exp
# input area 
D=30.            # debt
E=70.            # equity 
T=1.             # maturity 
r=0.07           # risk-free
sigmaE=0.4       # volatility of equity 
#
# define a function to siplify notations later 
def N(x):
    return stats.norm.cdf(x)
#
def KMV_f(E,D,T,r,sigmaE):
    n=10000
    m=2000
    diffOld=1e6     # a very big number
    for i in sp.arange(1,10):
        for j in sp.arange(1,m):
            A=E+D/2+i*D/n
            sigmaA=0.05+j*(1.0-0.001)/m
            d1 = (log(A/D)+(r+sigmaA*sigmaA/2.)*T)/(sigmaA*sqrt(T))
            d2 = d1-sigmaA*sqrt(T)
            diff4E= (A*N(d1)-D*exp(-r*T)*N(d2)-E)/A  # scale by assets
            diff4A= A/E*N(d1)*sigmaA-sigmaE          # a small number already
            diffNew=abs(diff4E)+abs(diff4A)
            if diffNew<diffOld:
               diffOld=diffNew
               output=(round(A,2),round(sigmaA,4),round(diffNew,5))
    return output
#
print("KMV=", KMV_f(D,E,T,r,sigmaE))
print("KMV=", KMV_f(D=65e3,E=110e3,T=1,r=0.01,sigmaE=0.2))
