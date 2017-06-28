import pandas as pd 
url='http://chart.yahoo.com/table.csv?s=IBM' 
x=pd.read_csv(url,index_col=0,parse_dates=True) 
print(x.head())
