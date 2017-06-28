"""
  Name     : c15_14_GARCH_2_1.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
#
sp.random.seed(12345) 
m=2
n=100              # n is the number of observations
nDrop=100          # we need to drop the first several observations 
delta=2
omega=1e-6 
alpha=(0.05,0.05)
#
beta=0.8 
mu,ma,ar=0.0,0.0,0.0
gamma=(0.0,0.0) 
order_ar=sp.size(ar) 
order_ma=sp.size(ma) 
order_beta=sp.size(beta)
#
order_alpha =sp.size(alpha) 
z0=sp.random.standard_normal(n+nDrop) 
deltainv=1/delta 
spec_1=np.array([2])
spec_2=np.array([2])
spec_3=np.array([2])
z = np.hstack((spec_1,z0)) 
t=np.zeros(n+nDrop)
h = np.hstack((spec_2,t)) 
y = np.hstack((spec_3,t)) 
eps0 = h**deltainv  * z
for i in range(m+1,n +nDrop+m-1):
    t1=sum(alpha[::-1]*abs(eps0[i-2:i]))	# reverse 
    alpha =alpha[::-1] 
    t2=eps0[i-order_alpha-1:i-1]
    t3=t2*t2 
    t4=np.dot(gamma,t3.T)
    t5=sum(beta* h[i-order_beta:i-1]) 
    h[i]=omega+t1-t4+ t5
    eps0[i] = h[i]**deltainv * z[i] 
    t10=ar * y[i-order_ar:i-1] 
    t11=ma * eps0[i -order_ma:i-1]
    y[i]=mu+sum(t10)+sum(t11)+eps0[i] 
    garch=y[nDrop+1:] 
    sigma=h[nDrop+1:]**0.5 
    eps=eps0[nDrop+1:] 
    x=range(1,len(garch)+1) 
#
plt.plot(x,garch,'r')
plt.plot(x,sigma,'b')
plt.title('GARCH(2,1) process')
plt.figtext(0.2,0.8,'omega='+str(omega)+', alpha='+str(alpha)+',beta='+str(beta))
plt.figtext(0.2,0.75,'gamma='+str(gamma)) 
plt.figtext(0.2,0.7,'mu='+str(mu)+', ar='+str(ar)+',ma='+str(ma)) 
plt.show()
