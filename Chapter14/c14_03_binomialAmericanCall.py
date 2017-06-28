# -*- coding: utf-8 -*-

"""
  Name     : c14_03_binomialAmericanCall.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
def binomialCallAmerican(s,x,T,r,sigma,n=100):
    from math import exp,sqrt
    import numpy as np
    deltaT = T /n
    u = exp(sigma * sqrt(deltaT)) 
    d = 1.0 / u
    a = exp(r * deltaT)
    p = (a - d) / (u - d)
    v = [[0.0 for j in np.arange(i + 1)] for i in np.arange(n + 1)] 
    for j in np.arange(n+1):
        v[n][j] = max(s * u**j * d**(n - j) - x, 0.0) 
    for i in np.arange(n-1, -1, -1):
        for j in np.arange(i + 1):
            v1=exp(-r*deltaT)*(p*v[i+1][j+1]+(1.0-p)*v[i+1][j]) 
            v2=max(v[i][j]-x,0)	       # early exercise 
            v[i][j]=max(v1,v2)
    return v[0][0]
#
s=40.        # stock price today 
x=40.        # exercise price
T=6./12      # maturity date ii years
tao=1/12     # when to choose
r=0.05       # risk-free rate
sigma=0.2    # volatility 
n=1000       # number of steps
#
price=binomialCallAmerican(s,x,T,r,sigma,n)
print("American call =", price)




