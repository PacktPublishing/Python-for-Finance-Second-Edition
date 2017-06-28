"""
  Name     : c14_26_up_and_out_call2.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 3/3/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy as sp 
import p4f
def up_and_out_call(s0,x,T,r,sigma,n_simulation,barrier):
    n_steps=100.
    dt=T/n_steps 
    total=0
    for j in range(0, n_simulation): 
        sT=s0
        out=False
        for i in range(0,int(n_steps)): 
            e=sp.random.normal()
            sT*=sp.exp((r-0.5*sigma*sigma)*dt+sigma*e*sp.sqrt(dt)) 
            if sT>barrier:
                out=True 
    if out==False:
       total+=p4f.bs_call(s0,x,T,r,sigma) 
    return total/n_simulation
#
s0=40.	             # today stock price
x=40.	             # exercise price
barrier=42.	     # barrier level
T=0.5	             # maturity in years
r=0.05               # risk-free rate 
sigma=0.2	     # volatility (annualized) 
n_simulation=100     # number of simulations
result=up_and_out_call(s0,x,T,r,sigma,n_simulation,barrier) 
print('up-and-out-call = ', round(result,3))



