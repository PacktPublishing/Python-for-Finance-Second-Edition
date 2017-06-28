
"""
  Name     : c12_28_basic_income_best.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
  original : https://gist.github.com/stucchio/7447067
"""
from pylab import *
from scipy.stats import *
#input area
million=1e6                        # unit of million 
billion=1e9                        # unit of billion 
trillion=1e12                      # unit of trillion 
tiny=1e-7                          # a small number 
hourlyPay = 7.5                    # hourly wage
workingHoursPerWeek=40             # working hour per week                                
workingWeeksPerYear=50             # working weeks per year
nAdult           = 227*million     # number of adult
laborForce       = 154*million     # labor force
disabledAdults   =  21*million     # disability 
nSimulations     = 1024*32         # number of simulations 
#
basicIncome = hourlyPay*workingHoursPerWeek*workingWeeksPerYear
# define a few function
def geniusEffect(nNonWorkers):
    nGenious = binom(nNonWorkers,tiny).rvs()
    return nGenious* billion
#
def costBasicIncome():
    salaryCost= nAdult * basicIncome
    unitAdmCost = norm(250,75)
    nonWorkerMultiplier = uniform(-0.10, 0.15).rvs()
    nonWorker0=nAdult-laborForce-disabledAdults
    nNonWorker = nonWorker0*(1+nonWorkerMultiplier)
    marginalWorkerHourlyProductivity = norm(10,1)
    admCost = nAdult * unitAdmCost.rvs()
    unitBenefitNonWorker=40*52*marginalWorkerHourlyProductivity.rvs()
    benefitNonWorkers = 1 * (nNonWorker*unitBenefitNonWorker)
    geniusBenefit=geniusEffect(nNonWorker)
    totalCost=salaryCost + admCost - benefitNonWorkers-geniusBenefit
    return totalCost
#
def costBasicJob():
    unitAdmCost4disabled= norm(500,150).rvs()
    unitAdmCost4worker = norm(5000, 1500).rvs()
    nonWorkerMultiplier = uniform(-0.20, 0.25).rvs()
    hourlyProductivity = uniform(0.0, hourlyPay).rvs()
    cost4disabled=disabledAdults * (basicIncome + unitAdmCost4disabled)
    nBasicWorkers=((nAdult-disabledAdults-laborForce)*(1+nonWorkerMultiplier))
    annualCost=workingHoursPerWeek*workingWeeksPerYear*hourlyProductivity
    cost4workers=nBasicWorkers * (basicIncome+unitAdmCost4worker-annualCost)
    return cost4disabled + cost4workers
#
# take a long time here!!!
N = nSimulations
costBI = zeros(shape=(N,),dtype=float)
costBJ = zeros(shape=(N,),dtype=float)
for k in range(N):
    costBI[k] = costBasicIncome()
    costBJ[k] = costBasicJob()
#
def myPlot(data,myTitle,key):
    subplot(key)
    width = 4e12
    height=50*N/1024
    title(myTitle)
    #xlabel("Cost (Trillion = 1e12)")
    hist(data, bins=50)
    axis([0,width,0,height])
#
myPlot(costBI,"Basic Income",211)
myPlot(costBJ,"Basic Job",212)
show()

