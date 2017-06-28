"""
  Name     : c14_07_mvn_multiVariateNormalGraph.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#
# input area
n   = 60                      # number of intervals
x   = np.linspace(-3, 3, n)   # x dimention
y   = np.linspace(-3, 4, n)   # y dimention 
x,y = np.meshgrid(x, y)       # grid 
#
# Mean vector and covariance matrix
mu = np.array([0., 1.])
cov= np.array([[ 1. , -0.5], [-0.5,  1.5]])
#
# combine x and y into a single 3-dimensional array
pos = np.empty(x.shape + (2,))
pos[:, :, 0] = x
pos[:, :, 1] = y
#
def multiNormal(pos, mu, cov):
    n = mu.shape[0]
    Sigma_det = np.linalg.det(cov)
    Sigma_inv = np.linalg.inv(cov)
    n2 = np.sqrt((2*np.pi)**n * Sigma_det)
    fac = np.einsum('...k,kl,...l->...', pos-mu, Sigma_inv, pos-mu)
    return np.exp(-fac/2)/n2
#
z    = multiNormal(pos, mu, cov)
fig  = plt.figure()
ax   = fig.gca(projection='3d')
ax.plot_surface(x, y, z, rstride=3, cstride=3,linewidth=1, antialiased=True,cmap=cm.viridis)
cset = ax.contourf(x, y, z, zdir='z', offset=-0.15, cmap=cm.viridis)
ax.set_zlim(-0.15,0.2)
ax.set_zticks(np.linspace(0,0.2,5))
ax.view_init(27, -21)
plt.title("Bivariate normal distribtuion")
plt.ylabel("y values ")
plt.xlabel("x values")
plt.show()
