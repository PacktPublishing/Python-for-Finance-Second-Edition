
"""
  Name     : c12_36_terminal_stock_price_distribution.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy as sp 
import matplotlib.pyplot as plt
from scipy import zeros, sqrt, shape 
#input area
S0 = 9.15               # stock price at time zero 
T =1.                   # years
n_steps=100.            # number of steps 
mu =0.15                # expected annual return 
sigma = 0.2             # volatility (annual) 
sp.random.seed(12345)   # fix those random numbers 
n_simulation = 1000     # number of simulation 
dt =T/n_steps 
#
S = zeros([n_simulation], dtype=float) 
x = range(0, int(n_steps), 1) 
for j in range(0, n_simulation): 
    tt=S0 
    for i in x[:-1]: 
        e=sp.random.normal() 
        tt+=tt*(mu-0.5*pow(sigma,2))*dt+sigma*tt*sqrt(dt)*e; 
        S[j]=tt 
#
plt.title('Histogram of terminal price') 
plt.ylabel('Number of frequencies') 
plt.xlabel('Terminal price') 
plt.figtext(0.5,0.8,'S0='+str(S0)+',mu='+str(mu)+',sigma='+str(sigma)) 
plt.figtext(0.5,0.76,'T='+str(T)+', steps='+str(int(n_steps))) 
plt.figtext(0.5,0.72,'Number of terminal prices='+str(int(n_simulation))) 
plt.hist(S) 
plt.show()
