"""
  Name     : c8_10_normality_test_from_normal.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from scipy import stats 
import scipy as sp

sp.random.seed(12345)
mean=0.1
std=0.2
n=5000

ret=sp.random.normal(loc=0,scale=std,size=n)

print 'W-test, and P-value' 
print(stats.shapiro(ret))
