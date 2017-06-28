"""
  Name     : c14_12_Rainbow2.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import math
import numpy as np
#
def calc_px(self, corr, **kwargs):
    self.save2px_spec(corr=corr, **kwargs)
    return getattr(self, '_calc_' + self.px_spec.method.upper())()

def _calc_MC(self, keep_hist=False):
    dt = T / n
    df = math.exp(-rf_r * T)
    np.random.seed(rng_seed)
    h = list()
    for path in range(0, m):
        # Generate correlated Wiener Processes
        # Compute random variables with correlation
        z1 = np.random.normal(loc=0.0, scale=1.0, size=n)
        z2 = np.random.normal(loc=0.0, scale=1.0, size=n)
        r1 = z1 * math.sqrt(dt)
        r2 = (corr * z1 + math.sqrt(1 - corr ** 2) * z2) * math.sqrt(dt)
        # Simulate the paths
        S1 = [S0[0]]
        S2 = [S0[1]]
        mu = net_r * dt
        # Compute stock price
        for t in range(0, len(z1)):
            S1.append(S1[-1] * (mu + vol[0] * r1[t]) + S1[-1])
            S2.append(S2[-1] * (mu + vol[1] * r2[t]) + S2[-1])
        # Maximum payout of S1 and S2
        payout = np.maximum(sCP * (S1[-1] - S1[0]), sCP * (S2[-1] - S2[0]))
        v = np.maximum(payout, 0.0) * df
        # The payout is maximum of V and 0
        h.append(v)
        _spec.add(px=float(np.mean(h)), sub_method='J.C.Hull p.601')
        return self

#    def _calc_FD(self, nsteps=3, npaths=4, keep_hist=False):
#        """ Internal function for option valuation.        """
#        return self
