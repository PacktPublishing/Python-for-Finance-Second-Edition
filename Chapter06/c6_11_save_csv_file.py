"""
  Name     : c6_11_save_csv_file.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.finance import quotes_historical_yahoo_ochl as getData
import csv
f=open("c:/temp/c.csv","w")

ticker='c'
begdate=(2016,1,1)
enddate=(2017,1,9)
p = getData(ticker, begdate, enddate,asobject=True,adjusted=True)

writer = csv.writer(f)
writer.writerows(p)
f.close()
