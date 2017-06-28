"""
  Name     : c12_03_histogram.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp 
import matplotlib.pyplot as plt 
#
sp.random.seed(12345) 
mean=0.1
std=0.2
n=1000
x=sp.random.normal(mean,std,n) 
plt.hist(x, 15, normed=True) 
plt.title("Histogram for random numbers drawn from a normal distribution")
plt.annotate("mean="+str(mean),xy=(0.6,1.5))
plt.annotate("std="+str(std),xy=(0.6,1.4))
plt.show()



