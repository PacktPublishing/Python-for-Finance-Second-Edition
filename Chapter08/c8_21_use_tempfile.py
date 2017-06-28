"""
  Name     : c8_17_ttest_mean_point5.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import tempfile
import re, string 
import pandas as pd 
ticker='AAPL'                    # input a ticker 
f1="c:/temp/ttt.txt"             # ttt will be replace with above sticker
f2=f1.replace("ttt",ticker) 
outfile=open(f2,"w") 
#path="http://www.google.com/finance/getprices?q=ttt&i=300&p=10d&f=d,o, h,l,c,v" 
path="https://www.google.com/finance/getprices?q=ttt&i=300&p=10d&f=d,o,%20h,l,c,v"
path2=path.replace("ttt",ticker) 
df=pd.read_csv(path2,skiprows=8,header=None) 
fp = tempfile.TemporaryFile()
df.to_csv(fp) 
print(df.head())
fp.close()
