# -*- coding: utf-8 -*-
"""
  Name     : c10_11_area_under_normal_dist.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
#
z=0.325	          # user can change this number 
def f(t):
    return sp.stats.norm.pdf(t) 
plt.ylim(0,0.45)
x = np.arange(-3,3,0.1) 
y1=f(x)
plt.plot(x,y1)
x2= np.arange(-4,z,1/40.) 
sum=0
delta=0.05
s=np.arange(-10,z,delta) 
for i in s:
    sum+=f(i)*delta
plt.annotate('area is '+str(round(sum,4)),xy=(-1,0.25),xytext=(-3.8,0.4), arrowprops=dict(facecolor='red',shrink=0.01))
plt.annotate('z= '+str(z),xy=(z,0.01)) 
plt.fill_between(x2,f(x2))
plt.show()




