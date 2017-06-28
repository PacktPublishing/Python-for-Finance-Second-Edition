"""
  Name     : c6_13_save_Excel_file.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
import pandas_datareader.data as getData
import re
ticker='msft'
df = getData.DataReader(ticker, "google")
f= pd.ExcelWriter('c:/temp/ibm.xlsx')
df.to_excel(f, sheet_name='IBM_data')
f.save()




