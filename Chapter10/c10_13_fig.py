# -*- coding: utf-8 -*-

"""
  Name     : c10_13_fig.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from scipy import exp,sqrt,stats,arange,ones
from matplotlib import pyplot as plt 
import numpy as np
z=0.325
def f(x):
    return stats.norm.cdf(x) 

x = arange(-3,3,0.1)
y1=f(x)
y2=ones(len(x))*0.5 
x3=[0,0]
y3=[0,1]
plt.plot(x,y1) 
plt.plot(x, y2, 'b-')
plt.plot(x3,y3)
plt.annotate('f(z)=f('+str(z)+') is '+str(np.round(f(z),4)),xy=(z,f(z)), xytext=(z-3,f(z)), arrowprops=dict(facecolor='red',shrink=0.01))
plt.annotate('z is '+str(z),xy=(z,0),xytext=(1.5,0.3), arrowprops=dict(facecolor='blue',shrink=0.01))
plt.show()



