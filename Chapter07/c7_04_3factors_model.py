"""
  Name     : c7_04_3factor_model.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm

inFile='http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv'
df_adv = pd.read_csv(inFile, index_col=0)
X = df_adv[['TV', 'Radio', 'Newspaper']]
y = df_adv['Sales']
df_adv.head()
X = sm.add_constant(X)
result = sm.OLS(y, X).fit()
print(result.summary())


