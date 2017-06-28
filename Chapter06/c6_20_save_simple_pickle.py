"""
  Name     : c6_20_save_simple_pickle.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd 
import numpy as np 
np.random.seed(1234) 
a = pd.DataFrame(np.random.randn(6,5)) 
a.to_pickle('c:/temp/a.pickle') 

