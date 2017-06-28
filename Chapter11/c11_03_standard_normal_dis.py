"""
  Name     : c11_03_standard_normal_dist.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy as sp
import scipy.stats as stats
x = sp.arange(-3,3,0.01)
ret=stats.norm.pdf(x)
confidence=0.99
position=10000
z=stats.norm.ppf(1-confidence)
print("z=",z)
zES=-stats.norm.pdf(z)/(1-confidence)
print("zES=", zES)
std=sp.std(ret)
VaR=position*z*std
print("VaR=",VaR)
ES=position*zES*std
print("ES=",ES)


