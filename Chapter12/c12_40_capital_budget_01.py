
"""
  Name     : c12_40_capital_budget_01.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


import scipy as sp
nYear=5                 # number of years
costEquipment=5e6       # 5 million 
n=nYear+1               # add year zero
price=28                # price of the product
units=100000            # estimate number of units sold 
otherCost=100000        # other costs
sellingCost=1500        # selling and administration cost 
R_and_D=200000          # Research and development
costRawMaterials=0.3    # percentage cost of raw materials
R=0.15                  # discount rate
tax=0.38                # corporate tax rate
#
sales=sp.ones(n)*price*units
sales[0]=0              # sales for 1st year is zero
cost1=costRawMaterials*sales
cost2=sp.ones(n)*otherCost
cost3=sp.ones(n)*sellingCost
cost4=sp.zeros(n)
cost4[0]=costEquipment
RD=sp.zeros(n)
RD[0]=R_and_D                     # assume R&D at time zero
D=sp.ones(n)*costEquipment/nYear  # straight line depreciation 
D[0]=0                            # no depreciation at time 0
EBIT=sales-cost1-cost2-cost3-cost4-RD-D
NI=EBIT*(1-tax)
FCF=NI+D                         # add back depreciation
npvProject=sp.npv(R,FCF)         # estimate NPV
print("NPV of project=",round(npvProject,0))
