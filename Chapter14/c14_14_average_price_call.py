"""
  Name     : c14_14_average_price_call.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy as sp 
s0=30.                 # today stock price 
x=32.                  # exercise price 
T=3.0/12.              # maturity in years 
r=0.025                # risk-free rate 
sigma=0.18             # volatility (annualized) 
sp.random.seed(123)    # fix a seed here 
n_simulation=1000      # number of simulations 
n_steps=500.           # number of steps
#
dt=T/n_steps 
call=sp.zeros([n_simulation], dtype=float) 
for j in range(0, n_simulation): 
    sT=s0 
    total=0 
    for i in range(0,int(n_steps)): 
         e=sp.random.normal()
         sT*=sp.exp((r-0.5*sigma*sigma)*dt+sigma*e*sp.sqrt(dt)) 
         total+=sT 
         price_average=total/n_steps 
    call[j]=max(price_average-x,0) 
#
call_price=sp.mean(call)*sp.exp(-r*T) 
print('call price based on average price = ', round(call_price,3))
