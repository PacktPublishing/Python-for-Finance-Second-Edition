"""
  Name     : c8_55_high_frequency_from_Google.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

"""
  Name     : c8_55_high_frequency_from_google.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import tempfile
import pandas as pd, numpy as np, datetime 
ticker='AAPL' 
path="https://www.google.com/finance/getprices?q=ttt&i=300&p=10d&f=d,o,%20h,l,c,v"
x=np.array(pd.read_csv(path.replace('ttt',ticker),skiprows=7,header=None)) 
#
date=[] 
for i in np.arange(0,len(x)): 
    if x[i][0][0]=='a': 
        t= datetime.datetime.fromtimestamp(int(x[i][0].replace('a',''))) 
        print ticker, t, x[i][1:] 
        date.append(t) 
    else: 
        date.append(t+datetime.timedelta(minutes =int(x[i][0]))) 

final=pd.DataFrame(x,index=date) 
final.columns=['a','CLOSE','LOW','OPEN','VOL'] 
del final['a'] 
fp = tempfile.TemporaryFile()
#final.to_csv('c:/temp/abc.csv'.replace('abc',ticker)) 
final.to_csv(fp) 
print(final.head())
