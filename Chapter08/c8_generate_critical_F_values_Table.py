import scipy.stats
import scipy as sp
import pandas as pd

alpha=0.05
output=[]
for i in sp.arange(1,36):
    dfDenominator=i
    for j in sp.arange(1,11):
        dfNumerator=j
        f=scipy.stats.f.ppf(q=1-alpha, dfn=dfNumerator, dfd=dfDenominator)
        output.append(round(f,2))
        #print(f)

n=sp.size(output)
out=sp.reshape(output,[n/10,10])
rowNames=list(range(1,36))
#index=list(range(1,36))
out2=pd.DataFrame(out,index=rowNames,columns=[1,2,3,4,5,6,7,8,9,10])


# output to screen
import sys
out2.to_csv(sys.stdout)





#out2=round(out,2)

#old_names = ['$a', '$b', '$c', '$d', '$e'] 
#new_names = ['a', 'b', 'c', 'd', 'e']
#df.rename(columns=dict(zip(old_names, new_names)), inplace=True)

#oldNames=out2.columns
#newNames=sp.arange(1,11)
#out2=out2.rename(columns=dict(zip(oldNames,newNames)),inplace=True)