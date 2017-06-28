"""DATE,START,END
10006,19570301,19840718
10030,19570301,19690108
10049,19251231,19321001
"""

import pandas as pd
x=pd.read_csv("c:/temp/sp500add.csv")
x.columns=['PERMNO','DATEADDED','DAYDELETED']
print(x.head())
print(x.tail())

x.to_pickle("c:/temp/sp500add.pkl")


