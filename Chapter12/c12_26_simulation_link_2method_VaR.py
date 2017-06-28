
"""
  Name     : c12_26_simulation_link_2method_VaR.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import scipy as sp
import pandas as pd
from scipy.stats import norm
#
position=1e6              # portfolio value
std=0.2                   # volatility
mean=0.08                 # mean return
confidence=0.99           # confidence level
nSimulations=50000        # number of simulations
# Method I
z=norm.ppf(1-confidence)
VaR=position*(mean+z*std)
print("Holding=",position, "VaR=", round(VaR,0), "tomorrow")
#
# Method II: Monte Carlo simulaiton 
sp.random.seed(12345) 
ret2=sp.random.normal(mean,std,nSimulations) 
ret3=np.sort(ret2) 
m=int(nSimulations*(1-confidence))
VaR2=position*(ret3[m])
print("Holding=",position, "VaR2=", round(VaR2,0), "tomorrow")
