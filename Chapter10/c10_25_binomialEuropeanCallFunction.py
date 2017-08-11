# -*- coding: utf-8 -*-
"""
  Name     : c10_25_binomialCall_EuropeanFunction.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def binomialCallEuropean(s,x,T,r,sigma,n=100):
    from math import exp,sqrt 
    deltaT = T /n
    u = exp(sigma * sqrt(deltaT)) 
    d = 1.0 / u
    a = exp(r * deltaT)
    p = (a - d) / (u - d)
    v = [[0.0 for j in xrange(i + 1)]  for i in xrange(n + 1)] 
    for j in xrange(i+1):
        v[n][j] = max(s * u**j * d**(n - j) - x, 0.0) 
    for i in xrange(n-1, -1, -1):
        for j in xrange(i + 1):
            v[i][j]=exp(-r*deltaT)*(p*v[i+1][j+1]+(1.0-p)*v[i+1][j]) 
    return v[0][0]

