import pandas as pd
import scipy as sp
import statsmodels.api as ms

a=pd.read_pickle("c:/temp/ibmMonthly.pkl")
ff=pd.read_pickle("c:/temp/ffMonthly.pkl")
df=pd.merge(a,ff,left_index=True,right_index=True)


y=final['RET']
x=final[['MKT_RF','SMB','HML']]
x=sm.add_constant(x)
results=sm.OLS(y,x).fit()
print(results.summary())


