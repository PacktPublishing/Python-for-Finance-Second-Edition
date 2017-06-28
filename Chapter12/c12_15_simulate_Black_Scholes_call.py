"""
  Name     : c12_15_simulate_black_Scholes_call.py
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
S0 = 40.              # stock price at time zero 
X= 40.                # exercise price 
T =0.5                # years 
r =0.05               # risk-free rate 
sigma = 0.2           # annualized volatility 
n_steps=100.          # number of steps 
#
sp.random.seed(12345) # fix those random numbers 
n_simulation = 5000   # number of simulation 
dt =T/n_steps 
call = sp.zeros([n_simulation], dtype=float) 
x = range(0, int(n_steps), 1) 
for j in range(0, n_simulation): 
    sT=S0 
    for i in x[:-1]: 
        e=sp.random.normal() 
        sT*=sp.exp((r-0.5*sigma*sigma)*dt+sigma*e*sqrt(dt)) 
        call[j]=max(sT-X,0) 
#
call_price=sp.mean(call)*sp.exp(-r*T) 
print('call price = ', round(call_price,3)) 
