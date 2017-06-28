"""
  Name     : c12_30_n_stock_efficient_forntier.py
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
import matplotlib.pyplot as plt
from datetime import datetime as dt
from scipy.optimize import minimize
#
# Step 1: input area
nStocks=20
sp.random.seed(1234)                        # produce the same random numbers 
n_corr=nStocks*(nStocks-1)/2                # number of correlation 
corr_0=sp.random.uniform(0.05,0.25,n_corr)  # generate correlations 
mean_0=sp.random.uniform(-0.1,0.25,nStocks) # means
std_0=sp.random.uniform(0.05,0.35,nStocks)  # standard deviation 
nSimulations=1000                           # number of simulations 
#
# Step 2: produce correlation matrix: Cholesky decomposition
corr_=sp.zeros((nStocks,nStocks))
for i in range(nStocks):
    for j in range(nStocks):
        if i==j:
            corr_[i,j]=1
        else:
            corr_[i,j]=corr_0[i+j]
U=np.linalg.cholesky(corr_)
#
# Step 3: Generate two uncorrelated time series 
R0=np.zeros((nSimulations,nStocks))
for i in range(nSimulations):
    for j in range(nStocks):
        R0[i,j]=sp.random.normal(loc=mean_0[j],scale=std_0[j],size=1)
if(R0.any()<=-1.0):
    print ('Error: return is <=-100%')
#
# Step 4: generate correlated return matrix: Cholesky     
R=np.dot(R0,U)
R=np.array(R)
#
# Step 5: define a few functions
def objFunction(W, R, target_ret): 
    stock_mean=np.mean(R,axis=0)  
    port_mean=np.dot(W,stock_mean)           # portfolio mean
    cov=np.cov(R.T)                          # var-covar matrix
    port_var=np.dot(np.dot(W,cov),W.T)       # portfolio variance
    penalty = 2000*abs(port_mean-target_ret) # penalty 4 deviation 
    return np.sqrt(port_var) + penalty       # objective function 
#
# Step 6: estimate optimal portfolo for a given return 
out_mean,out_std,out_weight=[],[],[] 
stockMean=np.mean(R,axis=0)    
#
for r in np.linspace(np.min(stockMean), np.max(stockMean), num=100):
    W = sp.ones([nStocks])/nStocks              # starting:equal w 
    b_ = [(0,1) for i in range(nStocks)]       # bounds
    c_ = ({'type':'eq', 'fun': lambda W: sum(W)-1. })# constraint
    result=minimize(objFunction,W,(R,r),method='SLSQP',constraints=c_, bounds=b_)    
    if not result.success:                    # handle error
        raise BaseException(result.message) 
    out_mean.append(round(r,4))               # a few decimal places
    std_=round(np.std(np.sum(R*result.x,axis=1)),6)
    out_std.append(std_)
    out_weight.append(result.x) 
#
# Step 7: plot the efficient frontier
plt.title('Simulation for an Efficient Frontier: '+str(nStocks)+' stocks')
plt.xlabel('Standard Deviation of the Porfolio')
plt.ylabel('Return of the2-stock portfolio')
plt.plot(out_std,out_mean,'--',linewidth=3)
plt.show()

