"""
  Name     : c13_04_print5year_credit_migrationMatrix.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 2/27/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
x=pd.read_pickle("c:/temp/creditRating5yearMigrationMatrix.pkl")
print(x.head(1))
print(x.tail(1))
y=x['Aaa'].transpose()
print(y)






