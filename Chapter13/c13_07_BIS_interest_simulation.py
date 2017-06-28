"""
  Name     : c13_07_BIS_interest_simulation.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 2/27/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp
import scipy.stats as stats
# input area
R0=0.09              # initial rate
s=0.182              # standard deviation of the risk-free rate
nSimulation=10       # number of simulations
sp.random.seed(123)  # fix the seed
#
num=sp.random.uniform(0,1,size=nSimulation)
z=stats.norm.ppf(num)
#
output=[]
def BIS_f(R,s,n):
    R=R0
    for i in sp.arange(0,n):
        deltaR=z[i]*s/sp.sqrt(2.)
        logR=sp.log(R)
        R=sp.exp(logR+deltaR)
        output.append(round(R,5))
    return output 
#
final=BIS_f(R0,s,nSimulation)
print(final)