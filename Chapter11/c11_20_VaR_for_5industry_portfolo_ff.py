
"""
  Name     : c11_20_VaR_for_5_industry_portfolio.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy as sp
import pandas as pd
from scipy.stats import norm

confidence_level=0.99   # input 3
z=norm.ppf(confidence_level) 
position=(1,1,1,1,1)

x=pd.read_pickle("c:/temp/ff5VWindustryMonthly.pkl")
#print(x.head(1))
mean=sp.mean(x,axis=0)
std=sp.std(x,axis=0)

t=sp.dot(position,z)
VaR=t*std
print("VaR=",VaR)








