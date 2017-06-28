"""
  Name     : c9_03_graph_anoterh_pari_y_x.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp
import matplotlib.pyplot as plt
x=sp.arange(-5,5,0.01)
y=3.4-2*sp.exp(-(x-0.8)**2)
plt.plot(x,y)
plt.title("y= 3.4 -2exp(-(x-0.5)^2)")
plt.ylabel("y")
plt.xlabel("x")
plt.show()