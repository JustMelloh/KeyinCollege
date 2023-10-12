################
# Description: OneStop Insurance would like to make reports of sales and policies.
# Created by: Austin Reid
# Written on: July 30, 2023
################

# Import Libraries
import Functions
import datetime as dt
import Validations as VT
import FormatValues as FV

# Define Constants

currDate = dt.datetime.now()
formattedDate = currDate.strftime("%d-%M-%y")


print()
print(" ", "ONE STOP INSURANCE COMPANY")
print(" ", f"POLICY LISTING AS OF {formattedDate}")
print()

print(" POLICY CUSTOMER               INSURANCE               TOTAL        MONTHLY")
print(" NUMBER NAME                    PREMIUM       HST      COST         PAYMENT")
print(" ============================================================================")



monthlyPayCtr = 0
totalCostCtr = 0
hstCtr = 0
policyCtr = 0


f = open('Policies.dat', 'r')
for information in f:
    infLine = information.split(",")
    policyNum = int(infLine[0])
    custFirstName = infLine[1].strip()
    custLastName = infLine[2].strip()
    policyDate = dt.datetime.strptime(infLine[14].strip(), "%Y-%M-%d")
  
    insPrem = float(infLine[13])
    extraLiability = (infLine[9].strip())
    glassCov = (infLine[10].strip())
    loanCar = (infLine[11].strip())
    carAmt = int(infLine[8].strip())
    monthlyPay = infLine[12].strip()

    if monthlyPay == "Monthly":
        premHST = insPrem * 0.15
        totalCost = insPrem + premHST
        monthPayAmt = (totalCost + 39.99) / 12
    else:
        continue                      
           
           

    if infLine[9].strip() == "Y":
            LiaCost = carAmt * 130.00
            
    else:
        
            LiaCost = 0
    if infLine[10] == "Y":
            glassCost = carAmt * 86.00
            
    else:
            glassCost = 0

    if infLine[11] == "Y":
            
            loanCost = carAmt * 58.00
    else:
            loanCost = 0

    
    
    formattedPolicyDate = dt.datetime.strftime(policyDate, "%Y-%M-%d")
    extraCosts = LiaCost + glassCost + loanCost
    insurancePrem = insPrem - extraCosts

    monthlyPayCtr += monthPayAmt
    totalCostCtr += totalCost
    hstCtr += premHST
    policyCtr += 1


    

    print(f" {policyNum} {custFirstName:>12s}{custLastName:>12s}   {formattedPolicyDate}  {FV.FDollar2(premHST):>9s}   {FV.FDollar2(totalCost):>9s}  {FV.FDollar2(monthPayAmt):>9s}")
f.close() 

print(" ============================================================================")
print(f" Total Policies: {policyCtr}                             {FV.FDollar2(hstCtr)}   {FV.FDollar2(totalCostCtr)}    {FV.FDollar2(monthlyPayCtr)}")