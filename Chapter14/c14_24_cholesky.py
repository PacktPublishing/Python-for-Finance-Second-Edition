"""
  Name     : c14_24_cholesky.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
# input area
nSimulation=5000              # number of simulations
c=np.array([[1.0, 0.5, 0.3],  # correlation matrix
            [0.5, 1.0, 0.4],
            [0.3, 0.4, 1.0]])
np.random.seed(123)           # fix random numbers 
#
# generate uncorrelated random numbers
x=np.random.normal(size=3*nSimulation)
U=np.reshape(x,(nSimulation,3))
#
# Cholesky decomposition 
L=np.linalg.cholesky(c)
# generate correlated random numbers
r=np.dot(U,L)
#check the correlation matrix
print(np.corrcoef(r.T))

