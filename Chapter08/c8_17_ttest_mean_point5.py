"""
  Name     : c8_17_ttest_mean_point5.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


from scipy import stats 
import numpy as np
np.random.seed(1235) 
x = stats.norm.rvs(size=10000) 
print("T-value P-value (two-tail)") 
print(stats.ttest_1samp(x,0.5)) 
print(stats.ttest_1samp(x,0)) 
