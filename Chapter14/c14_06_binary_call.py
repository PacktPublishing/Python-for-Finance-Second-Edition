
"""
  Name     : c14_06_binary_call.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import random
import scipy as sp
#
def terminalStockPrice(S, T,r,sigma):
    tao=random.gauss(0,1.0)
    terminalPrice=S * sp.exp((r - 0.5 * sigma**2)*T+sigma*sp.sqrt(T)*tao)
    return terminalPrice
#
def binaryCallPayoff(x, sT,payoff):
    if sT >= x:
        return payoff
    else:
        return 0.0
# input area 
S = 40.0            # asset price
x = 40.0            #  exericse price 
T = 0.5             # maturity in years 
r = 0.01            # risk-free rate 
sigma = 0.2         # vol of 20%
fixedPayoff = 10.0  # payoff 
nSimulations =10000 # number of simulatins 
#
payoffs=0.0
for i in xrange(nSimulations):
    sT = terminalStockPrice(S, T,r,sigma) 
    payoffs += binaryCallPayoff(x, sT,fixedPayoff)
#
price = sp.exp(-r * T) * (payoffs / float(nSimulations))
print('Binary options call= %.8f' % price)
