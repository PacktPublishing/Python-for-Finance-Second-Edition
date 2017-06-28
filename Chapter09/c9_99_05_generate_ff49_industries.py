import pandas as pd
import scipy as sp
x=pd.read_csv("c:/temp/49_industry_portfolios.csv",skiprows=11,index_col=0)
#x=pd.read_csv("c:/temp/49_industry_portfolios.csv",skiprows=11)
x.to_pickle("c:/temp/ff49industries.pkl")



