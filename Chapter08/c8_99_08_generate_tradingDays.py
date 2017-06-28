import pandas as pd

x=pd.read_table("c:/temp/tradingDaysMonthly.txt")

x.to_pickle("c:/temp/tradingDaysMonthly.pkl")


a=pd.read_table("c:/temp/tradingDaysDaily.txt")

a.to_pickle("c:/temp/tradingDaysDaily.pkl")