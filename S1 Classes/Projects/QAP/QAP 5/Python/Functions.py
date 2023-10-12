# Functions for the main program are listed below.

# Import th default files for functions

f = open('OSICDef.dat', 'r')
POLICY_NUM = int(f.readline())
BASIC_RATE = float(f.readline())
ADD_DISCOUNT_RATE = float(f.readline())
LIA_PER_CAR_RATE = float(f.readline())
GLASS_COV_RATE = float(f.readline())
LOANER_CAR = float(f.readline())
HST_RATE = float(f.readline())
PROCESS_FEE_RATE = float(f.readline())
f.close()

# Determing the insurance premium depending on the amount of cars.

def Calc_insurance(numCars):
    if numCars <= 0:
        return 0
    elif numCars == 1:
        return BASIC_RATE
    else:
        addCar = BASIC_RATE * ADD_DISCOUNT_RATE
        insPremium = BASIC_RATE + (BASIC_RATE - addCar) * (numCars - 1)
        return insPremium
    
def extra_Liability(numCars, Liability):
    if numCars <= 0 or Liability == "N":
        return 0
    elif numCars == 1:
        return LIA_PER_CAR_RATE
    else:
        totalLiability = LIA_PER_CAR_RATE * numCars
        return totalLiability

def glassCov(numCars, glassCov):
    if numCars <= 0 or glassCov == "N":
        return 0
    elif numCars == 1:
        return GLASS_COV_RATE
    else:
        totalGlassCov = GLASS_COV_RATE * numCars
        return totalGlassCov
    
def loanCar(numCars, optLoaner):
    if numCars <= 0 or optLoaner == "N":
        return 0
    elif numCars == 1:
        return LOANER_CAR
    else:
        loanCarTotal = LOANER_CAR * numCars
        return loanCarTotal
    
def insurancePay(totalCost, typePay,):
    if typePay == "Full":
        return totalCost
    elif typePay == "Monthly":
        monthlyPay = (totalCost + PROCESS_FEE_RATE) / 8
        return monthlyPay

def phoneFormat(custPhone):
    return f"({custPhone[:3]}) {custPhone[3:6]}-{custPhone[6:]}"
