"""
  Name     : c14_09_rainbowFormulaMinimum2.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from math import exp,sqrt,log
import statsmodels.sandbox.distributions.extras as extras
#
def dOne(s,k,r,sigma,T):
    #print(s,k,r,sigma,T)
    a=log(s/k)+(r-0.5*sigma**2)*T
    b=(sigma*sqrt(T))
    return a/b
#
def sigmaA_f(sigma1,sigma2,rho):
    return sqrt(sigma1**2-2*rho*sigma1*sigma2+sigma2**2)
#
def dTwo(d1,sigma,T):
    return d1+sigma*sqrt(T)
#
def rhoTwo(sigma1,sigma2,sigmaA,rho):
    return (rho*sigma2-sigma1)/sigmaA
#
def N2_f(d1,d2,rho):
    import statsmodels.sandbox.distributions.extras as extras
    muStandardNormal=0.0    # mean of a standard normal distribution 
    varStandardNormal=1.0   # variance of standard normal distribution 
    upper=([d1,d2])         # upper bound for two values
    v=varStandardNormal     # simplify our notations
    mu=muStandardNormal     # simplify our notations
    covM=([v,rho],[rho,v])
    return extras.mvnormcdf(upper,mu,covM)
#
def dOneTwo(s1,s2,sigmaA,T):
    a=log(s2/s1)-0.5*sigmaA**2*T
    b=sigmaA*sqrt(T)
    return a/b
#
def rainbowCallOnMinimum(s1,s2,k,T,r,sigma1,sigma2,rho):
    d1=dOne(s1,k,r,sigma1,T)
    d2=dOne(s2,k,r,sigma2,T)
    d11=dTwo(d1,sigma1,T)
    d22=dTwo(d2,sigma2,T)
    sigmaA=sigmaA_f(sigma1,sigma2,rho)
    rho1=rhoTwo(sigma1,sigma2,sigmaA,rho)
    rho2=rhoTwo(sigma2,sigma1,sigmaA,rho)
    d12=dOneTwo(s1,s2,sigmaA,T)
    d21=dOneTwo(s2,s1,sigmaA,T)
    #
    part1=s1*N2_f(d11,d12,rho1)
    part2=s2*N2_f(d21,d22,rho2)
    part3=k*exp(-r*T)*N2_f(d1,d2,rho)
  #  print("d1=",d1)   # ok
  #  print("d11=",d11)  #ok 
  #    print("d2=",d2)  #ok 
    print("sigmaA=",sigmaA) # good
    print("d12=",d12)
    print("d21=",d21)
   # print("d22=",d22)   # good 
    print("rho1=",rho1)  # good
    print("rho2=",rho2)  # good 
    print("part 1=",part1)
    print("part 2=",part2)
    print("part 3=",part3)
    return part1 + part2 - part3
#
s1=100.
s2=95.
k=102.0
T=8./12.
r=0.08
rho=0.75
sigma1=0.15
sigma2=0.20
price=rainbowCallOnMinimum(s1,s2,k,T,r,sigma1,sigma2,rho)
print("price of call based on the minimum of 2 assets=",price)