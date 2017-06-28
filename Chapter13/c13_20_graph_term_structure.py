"""
  Name     : c13_20_graph_term_structure.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 2/27/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import matplotlib.pyplot as plt
time=[3./12.,6./12.,2.,3.,5.,10.,30.]
rate=[0.49,0.51,1.18,1.46,1.89,2.40,3.0]
plt.title("Term Structure of Interest Rate ")
plt.xlabel("Time (in years) ")
plt.ylabel("Risk-free rate (%)")
plt.plot(time,rate)
plt.show()
