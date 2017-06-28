import pandas as pd
x=pd.read_csv("c:/temp/indexMonthly2.csv")

x.columns=(['DATE','VWRETD', 'VWRETX', 'EWRETD', 'EWRETX','SP500RET','SP500INDEX','TOTALVAL','TOTALN','USEDVAL', 'USEDN'])
x.to_pickle("c:/temp/indexMonthly.pkl")
