
"""
  Name     : c9_44_impact_of_correlation_2stock_portfolio.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo_ochl as getData
import numpy as np
import pandas as pd
import scipy as sp
from scipy.optimize import fmin
import matplotlib.pyplot as plt

ticker=('IBM','C')   # tickers
begdate=(1990,1,1)         # beginning date 
enddate=(2012,12,31)       # ending date
rf=0.0003                  # annual risk-free rate
def ret_annual(ticker,begdate,enddte):
    x=getData(ticker,begdate,enddate,asobject=True,adjusted=True)
    logret =sp.log(x.aclose[1:]/x.aclose[:-1])
    date=[]
    d0=x.date
    for i in range(0,sp.size(logret)):
        date.append(d0[i].strftime("%Y"))
    y=pd.DataFrame(logret,date,columns=[ticker])
    return sp.exp(y.groupby(y.index).sum())-1
def portfolio_var(R,w):
    cor=corr # here!!!!
    std_dev=sp.std(R,axis=0)
    var = 0.0
    for i in xrange(n):
        for j in xrange(n):
            var += w[i]*w[j]*std_dev[i]*std_dev[j]*cor[i, j]
    return var
def portfolioRet(R,w):
    mean_return=sp.mean(R,axis=0)
    ret = sp.array(mean_return)
    return sp.dot(w,ret)
def sharpe(R,w):
    var = portfolio_var(R,w)
    return (portfolioRet(R,w) - rf)/sp.sqrt(var)
def negative_sharpe_n_minus_1_stock(w):
    w2=sp.append(w,1-sum(w))
    return -sharpe(R,w2)        # using a return matrix here!!!!!!

n=len(ticker)              # number of stocks
portStd=[]
portReturn=[]
for i in sp.arange(20):
    k=i*0.1-1
    #k=0.26488575
    corr=np.array([[ 1., k],  [k,1.]])
    x2=ret_annual(ticker[0],begdate,enddate) 
    for i in range(1,n):
        x_=ret_annual(ticker[i],begdate,enddate) 
        x2=pd.merge(x2,x_,left_index=True,right_index=True)
    R = sp.array(x2)
    w0= sp.ones(n-1, dtype=float) * 1.0 /n 
    w1 = fmin(negative_sharpe_n_minus_1_stock,w0)
    final_w = sp.append(w1, 1 - sum(w1))
    final_sharpe = sharpe(R,final_w)
    var=portfolio_var(R,final_w)
    portStd.append(sp.sqrt(var))
    portReturn.append(portfolioRet(R,final_w))
    #print("porfolio var")
    #print(portfolio_var(R,final_w))

plt.plot(portStd,portReturn)
plt.show()

