"""
  Name     : c9_01_optimize.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from scipy.optimize import minimize
def myFunction(x):
    return (3.2+5*x**2)

x0=100
res = minimize(myFunction,x0,method='nelder-mead',options={'xtol':1e-8,'disp': True})

