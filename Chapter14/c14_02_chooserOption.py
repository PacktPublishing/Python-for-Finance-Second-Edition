# -*- coding: utf-8 -*-
"""
  Name     : c14_02_chooserOption.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from scipy import log,exp,sqrt,stats 
def callAndPut(S,X,T,r,sigma,tao,type='C'):
    d1=(log(S/X)+r*T+0.5*sigma*sigma*tao)/(sigma*sqrt(tao)) 
    d2 = d1-sigma*sqrt(tao)
    if type.upper()=='C':
        c=S*stats.norm.cdf(d1)-X*exp(-r*T)*stats.norm.cdf(d2)
        return c
    else:
        p=X*exp(-r*T)*stats.norm.cdf(-d2)-S*stats.norm.cdf(-d1)
        return p
#
def chooserOption(S,X,T,r,sigma,tao):
    call_T=callAndPut(S,X,T,r,sigma,T)
    put_tao=callAndPut(S,X,T,r,sigma,tao,type='P')
    return call_T- put_tao
#
s=40.        # stock price today 
x=40.        # exercise price
T=6./12      # maturity date ii years
tao=1./12.   # when to choose
r=0.05       # risk-free rate
sigma=0.2    # volatility 
#
price=chooserOption(s,x,T,r,sigma,tao)
print("price of a chooser option=",price)

    

