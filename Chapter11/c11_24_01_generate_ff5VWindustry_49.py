import pandas as pd
import scipy as sp
#x=pd.read_csv("c:/temp/ff49VWindustryMonthly.csv",skiprows=11,index_col=0)
#x.to_pickle("c:/temp/ff49VWindustryMonthly.pkl")

x=pd.read_csv("c:/temp/ff5VWindustryMonthly.csv",skiprows=11,index_col=0)
x2=x/100.0
x2.columns = [x.upper() for x in x2.columns]
x2.to_pickle("c:/temp/ff5VWindustryMonthly.pkl")