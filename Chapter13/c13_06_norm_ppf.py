"""
  Name     : c13_68_norm_ppf.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 2/27/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy.stats as stats
#
cumulativeProb=0
print(stats.norm.ppf(cumulativeProb))
#
cumulativeProb=0.5
print(stats.norm.ppf(cumulativeProb))
#
cumulativeProb=0.99
print(stats.norm.ppf(cumulativeProb))

