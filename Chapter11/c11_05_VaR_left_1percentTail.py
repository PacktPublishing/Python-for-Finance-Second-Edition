
"""
  Name     : c11_05_VaR_left_1percentTail.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy as sp
from matplotlib import pyplot as plt

z=-2.325       # user can change this number 
xStart=-3.8    # arrow line start x
yStart=0.2     # arrow line start x
xEnd=-2.5      # arrow line start x
yEnd=0.05      # arrow line start x

def f(t):
    return sp.stats.norm.pdf(t) 

plt.ylim(0,0.45)
x = sp.arange(-3,3,0.1) 
y1=f(x)
plt.plot(x,y1)
x2= sp.arange(-4,z,1/40.) 
sum=0
delta=0.05
s=sp.arange(-10,z,delta) 
for i in s:
    sum+=f(i)*delta

plt.annotate('area is '+str(round(sum,4)),xy=(xEnd,yEnd),xytext=(xStart,yStart), arrowprops=dict(facecolor='red',shrink=0.01))
plt.annotate('z= '+str(z),xy=(z,0.01)) 
plt.fill_between(x2,f(x2))
plt.show()
