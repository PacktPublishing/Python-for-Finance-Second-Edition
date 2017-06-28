"""
  Name     : c12_32_scatter_sobol.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import sobol_seq
import scipy as sp
import matplotlib.pyplot as plt
a=[]
n=100
for i in sp.arange(2*n):
     t=sobol_seq.i4_sobol(1,i)
     a.append(t)
print(a[0:10])
#
x=sp.random.permutation(a[:n])
y=sp.random.permutation(a[n:])
plt.scatter(x,y,edgecolors='r')
plt.show()