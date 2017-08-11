"""
  Name     : c10_10_target_beta_portfolio_hedging.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy as ps
# input area
todaySP500index=2297.42
valuePortfolio=50e6    
betaPortfolio=1.1
betaTarget=0

priceEachPoint=250  
contractFuturesSP500=todaySP500index*priceEachPoint
n=(betaTarget-betaPortfolio)*valuePortfolio/contractFuturesSP500
print("number of contracts SP500 futures=",n)
