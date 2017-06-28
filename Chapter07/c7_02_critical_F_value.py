"""
  Name     : c7_02_critical_F_value.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy.stats
alpha=0.05
dfNumerator=3
dfDenominator=1

f=scipy.stats.f.ppf(q=1-alpha, dfn=dfNumerator, dfd=dfDenominator)
print(f)