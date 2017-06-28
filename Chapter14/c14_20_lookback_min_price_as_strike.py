"""
  Name     : c14_20_lookback_min_as_strike.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 3/3/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
#
def lookback_min_price_as_strike(s,T,r,sigma,n_simulation): 
    n_steps=100
    dt=T/n_steps
    total=0
    for j in range(n_simulation): 
        min_price=100000.	# a very big number 
        sT=s
        for i in range(int(n_steps)): 
            e=sp.random.normal()
            sT*=sp.exp((r-0.5*sigma*sigma)*dt+sigma*e*sp.sqrt(dt)) 
            if sT<min_price:
                min_price=sT
                #print 'j=',j,'i=',i,'total=',total 
                total+=p4f.bs_call(s,min_price,T,r,sigma)
    return total/n_simulation

#
import scipy as sp
import p4f
s=40.	            # today stock price
T=0.5               # maturity in years
r=0.05              # risk-free rate
sigma=0.2           # volatility (annualized)
n_simulation=1000   # number of simulations
result=lookback_min_price_as_strike(s,T,r,sigma,n_simulation)
print('lookback min price as strike = ', round(result,3))


