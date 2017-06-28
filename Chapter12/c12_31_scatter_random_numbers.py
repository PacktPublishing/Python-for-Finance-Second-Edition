
"""
  Name     : c12_31_scatter_random_numbers.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(12345)
n=200
a = np.random.uniform(size=(n*2))
plt.scatter(a[:n], a[n:])
plt.show()




"""
import cython
#%load_ext cythonmagic
def bessel_J0(double x):
    return gsl_sf_bessel_J0(x)


%%cython -l gsl
# Include the right header file and declare the function
cdef extern from "gsl/gsl_sf_bessel.h":
    double gsl_sf_bessel_J0(double x)

# small python wrapper to give it a nicer name
def bessel_J0(double x):
    return gsl_sf_bessel_J0(x)

"""