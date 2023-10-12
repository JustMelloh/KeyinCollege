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
formattedDate = currDate.strftime("%d-%b-%y")


print()
print(" ", "ONE STOP INSURANCE COMPANY")
print(" ", f"POLICY LISTING AS OF {formattedDate}")
print()

print(" POLICY CUSTOMER                 POLICY      INSURANCE      EXTRA      TOTAL")
print(" NUMBER NAME                      DATE        PREMIUM       COSTS     PREMIUM")
print(" ============================================================================")

policyCtr = 0
insCtr = 0
extrCtr = 0
totalCtr = 0


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

    insCtr += insurancePrem
    extrCtr += extraCosts
    totalCtr += insPrem
    policyCtr += 1

    print(f" {policyNum} {custFirstName:>12s}{custLastName:>12s}   {formattedPolicyDate}  {FV.FDollar2(insurancePrem):>9s}   {FV.FDollar2(extraCosts):>9s}  {FV.FDollar2(insPrem):>9s}")   
f.close() 

print("  ===========================================================================")
print(f" Total Policies: {policyCtr}                            {FV.FDollar2(insCtr)} {FV.FDollar2(extrCtr)} {FV.FDollar2(totalCtr)}")


        

    
    


