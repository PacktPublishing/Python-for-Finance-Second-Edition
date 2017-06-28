"""
  Name     : c12_12_randomly_choose_m_from_n_stocks.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp 
n_stocks_available=500 
n_stocks=20 
sp.random.seed(123345) 
x=sp.random.uniform(low=1,high=n_stocks_available,size=n_stocks)
y=[] 
for i in range(n_stocks): 
    y.append(int(x[i])) 
#print y 
final=sp.unique(y) 
print(final) 
print(len(final)) 
