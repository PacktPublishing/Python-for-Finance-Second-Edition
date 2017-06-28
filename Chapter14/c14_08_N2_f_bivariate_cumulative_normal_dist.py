"""
  Name     : c14_08_N2_f_bivariate_cumulative_normal_dist.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def N2_f(d1,d2,rho):
    """cumulative bivariate standard normal distribution 
       d1: the first value
       d2: the second value
       rho: correlation

       Example1:
               print(N2_f(0,0,1.)) => 0.5
       Example2:
               print(N2_f(0,0,0)  => 0.25
     """
    import statsmodels.sandbox.distributions.extras as extras
    muStandardNormal=0.0    # mean of a standard normal distribution 
    varStandardNormal=1.0   # variance of standard normal distribution 
    upper=([d1,d2])         # upper bound for two values
    v=varStandardNormal     # simplify our notations
    mu=muStandardNormal     # simplify our notations
    covM=([v,rho],[rho,v])
    return extras.mvnormcdf(upper,mu,covM)
#

d1=0
d2=0
rho=1.
print("d1,=",d1,"d2=",d2,"rho=",rho,"N2=",N2_f(d1,d2,rho))


