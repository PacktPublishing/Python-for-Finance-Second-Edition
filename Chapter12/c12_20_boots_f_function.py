
"""
  Name     : c12_20_boots_f_function.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np 
#
def boots_f(data,n_obs,replacement=None):
    n=len(data) 
    if (n<n_obs):
        print "n is less than n_obs" 
    else: 
        if replacement==None:
            y=np.random.permutation(data) 
            return y[0:n_obs] 
        else:
            y=[] 
    #
    for i in range(n_obs): 
        k=np.random.permutation(data) 
        y.append(k[0]) 
    return y 



