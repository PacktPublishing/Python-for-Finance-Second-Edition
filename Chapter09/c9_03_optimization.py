"""
  Name     : c9_03_optimization.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
#
# define a function 
def f(x):
    return 3.4-2*np.exp(-(x - 0.8)**2)
#
# see the plot
x=np.arange(-3,3,0.1)
y=f(x)
plt.plot(x,y)
plt.show()

# find the miniumu
solution= optimize.brent(f) 
print(solution)

