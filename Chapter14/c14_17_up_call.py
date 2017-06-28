"""
  Name     : c14_17_up_call.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 3/3/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def upCall(s,x,T,r,sigma,nSimulation,barrier):
    import scipy as sp
    import p4f 
    n_steps=100
    dt=T/n_steps 
    inTotal=0 
    outTotal=0
    for j in range(0, nSimulation): 
        sT=s
        inStatus=False 
        outStatus=True
        for i in range(0,int(n_steps)):
            e=sp.random.normal()
            sT*=sp.exp((r-0.5*sigma*sigma)*dt+sigma*e*sp.sqrt(dt)) 
            if sT>barrier:
                outStatus=False 
                inStatus=True
        if outStatus==True:
            outTotal+=p4f.bs_call(s,x,T,r,sigma) 
        else:
            inTotal+=p4f.bs_call(s,x,T,r,sigma) 
    return outTotal/nSimulation, inTotal/nSimulation
#
import p4f
s=40.                 # today stock price 
x=40.                 # exercise price 
barrier=42.0          # barrier level 
T=0.5                 # maturity in years 
r=0.05                # risk-free rate 
sigma=0.2             # volatility (annualized) 
nSimulation=500       # number of simulations 
#
upOutCall,upInCall=upCall(s,x,T,r,sigma,nSimulation,barrier) 
print 'upOutCall=', round(upOutCall,2),'upInCall=',round(upInCall,2) 
print 'Black-Scholes call', round(p4f.bs_call(s,x,T,r,sigma),2) 
