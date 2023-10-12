###################
# Description: Process the data file and create reports based on the One Stop Program.
# Written by: Austin Reid
# Created on July 30, 2023
###################


# Import Libraries

import datetime as dt
import OneStop
import Functions
import Validations
import FormatValues as FV

# Define Constants

currDate = dt.datetime.now()
formatDate = currDate.strftime('%d-%M-%y')
# Main Program


f = open('Policies.dat', 'r')
for Information in f:
    infLine = Information.split(",")
    policyNum = int(infLine[0].strip())
    custName = infLine[1,2].strip()
    policyDate = infLine[12].strip()
    insPrem = float(infLine[11].strip())

formatPolicyDate =  policyDate.strftime('%y-%m-%d')

premium = OneStop.insPremium
extraCosts = OneStop.totalExtraCost
totalPrem = OneStop.totalInsurancePremium




print(" ", "ONE STOP INSURANCE COMPANY")
print(" ", f"POLICY LISTING AS OF: {currDate.strftime('%d-%M-%y')}")
print()

print(" ", f"POLICY CUSTOMER                 POLICY      INSURANCE      EXTRA      TOTAL")
print(" ", f"NUMBER NAME                      DATE        PREMIUM       COSTS     PREMIUM")
print(" ", f"============================================================================")
print("  ", f"{policyNum}  {custName}   {[formatPolicyDate]} {FV.FDollar2(premium):>10s}  {FV.FDollar2(extraCosts):>10s}  {FV.FDollar2(totalPrem):>10s}")
print()
print()
print()
print("  ", f"{policyNum}  {custName}   {[formatPolicyDate]} {FV.FDollar2(premium):>10s}  {FV.FDollar2(extraCosts):>10s}  {FV.FDollar2(totalPrem):>10s}")