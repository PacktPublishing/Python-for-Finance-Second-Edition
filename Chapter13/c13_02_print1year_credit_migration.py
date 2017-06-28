"""
  Name     : c13_02_print1year_credit_migration.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 2/27/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import pandas as pd
x=pd.read_pickle("c:/temp/creditRating1yearMigrationMatrix.pkl")
print(x.head(1))
print(x.tail(1))




