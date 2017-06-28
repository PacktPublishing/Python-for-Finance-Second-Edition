"""
  Name     : c14_11_rainbow_callMaxOn2_viaSimulation.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp 
from scipy import zeros, sqrt, shape 
#
sp.random.seed(123)  # fix our random numbers
s1=100.              # stock price 1 
s2=95.               # stock price 2
k=102.0              # exercise price
T=8./12.             # maturity in years
r=0.08               # risk-free rate
rho=0.75             # correlation between 2
sigma1=0.15          # volatility for stock 1
sigma2=0.20          # volatility for stock 1
nSteps=100.          # number of steps 
nSimulation=1000     # number of simulations 
#
# step 1: generate correlated random number
dt =T/nSteps 
call = sp.zeros([nSimulation], dtype=float) 
x = range(0, int(nSteps), 1) 
#
# step 2: call call prices 
for j in range(0, nSimulation): 
    x1=sp.random.normal(size=nSimulation)
    x2=sp.random.normal(size=nSimulation)
    y1=x1
    y2=rho*x1+sp.sqrt(1-rho**2)*x2
    sT1=s1
    sT2=s2 
    for i in x[:-1]: 
        e1=y1[i]
        e2=y2[i]
        sT1*=sp.exp((r-0.5*sigma1**2)*dt+sigma1*e1*sqrt(dt)) 
        sT2*=sp.exp((r-0.5*sigma2**2)*dt+sigma2*e2*sqrt(dt)) 
        minOf2=min(sT1,sT2)
        call[j]=max(minOf2-k,0) 
#
# Step 3: summation and discount back 
call=sp.mean(call)*sp.exp(-r*T) 
print('Rainbow call on minimum of 2 assets = ', round(call,3))



