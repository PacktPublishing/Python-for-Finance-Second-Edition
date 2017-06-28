"""
  Name     : c9_52_impacto_of_correlation_on_efficient_frontier.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo_ochl as getData
import matplotlib.pyplot as plt
import numpy as np, pandas as pd, scipy as sp
from numpy.linalg import inv, pinv
begYear,endYear = 2012,2016
stocks=['IBM','WMT']

def ret_monthly(ticker):  #	function 1
    x = getData(ticker,(begYear,1,1),(endYear,12,31),asobject=True,adjusted=True)
    logret=np.log(x.aclose[1:]/x.aclose[:-1]) 
    date=[]
    d0=x.date
    for i in range(0,np.size(logret)): 
        date.append(''.join([d0[i].strftime("%Y"),d0[i].strftime("%m")]))
    y=pd.DataFrame(logret,date,columns=[ticker]) 
    return y.groupby(y.index).sum()
def std_f(ticker):
    x=ret_monthly(ticker)
    return sp.std(x)
def objFunction(W, R, target_ret):
    stock_mean=np.mean(R,axis=0) 
    port_mean=np.dot(W,stock_mean)          # portfolio mean 
    #cov=np.cov(R.T)                         # var-cov matrix
    cov=cov0
    port_var=np.dot(np.dot(W,cov),W.T)	    # portfolio variance 
    penalty = 2000*abs(port_mean-target_ret)# penalty 4 deviation 
    return np.sqrt(port_var) + penalty	    # objective function
R0=ret_monthly(stocks[0])                   # starting from 1st stock 
n_stock=len(stocks)                         # number of stocks
std1=std_f(stocks[0])
std2=std_f(stocks[1])
for jj in sp.arange(1):
    k=0.1*std1*std2
    #cov0=sp.array([[0.00266285,0.00037303],[0.00037303,0.0021296]])
    #cov0=sp.array([[std1**2,k],[k,std2**2]])
    cov0=sp.array([[std1**2,0.00037303],[0.00037303,std2**2]])
    for i in xrange(1,n_stock):                # merge with other stocks 
        x=ret_monthly(stocks[i]) 
        R0=pd.merge(R0,x,left_index=True,right_index=True)
        R=np.array(R0)

    out_mean,out_std,out_weight=[],[],[] 
    stockMean=np.mean(R,axis=0)
    for r in np.linspace(np.min(stockMean),np.max(stockMean),num=100):
        W = np.ones([n_stock])/n_stock	  # starting from equal weights 
        b_ = [(0,1) 
        for i in range(n_stock)]	          # bounds, here no short 
        c_ = ({'type':'eq', 'fun': lambda W: sum(W)-1. })#constraint
        result=sp.optimize.minimize(objFunction,W,(R,r),method='SLSQP',constraints=c_, bounds=b_)
        if not result.success:               # handle error raise 
            BaseException(result.message)
        out_mean.append(round(r,4))           # 4 decimal places 
        std_=round(np.std(np.sum(R*result.x,axis=1)),6) 
        out_std.append(std_)
        out_weight.append(result.x)

    plt.title('Efficient Frontier')
    plt.xlabel('Standard Deviation of the porfolio (Risk))') 
    plt.ylabel('Return of the portfolio') 
    plt.figtext(0.5,0.75,str(n_stock)+' stock are used: ') 
    plt.figtext(0.5,0.7,' '+str(stocks))
    plt.figtext(0.5,0.65,'Time period: '+str(begYear)+' ------ '+str(endYear)) 
    plt.plot(out_std,out_mean,'--')
plt.show()




