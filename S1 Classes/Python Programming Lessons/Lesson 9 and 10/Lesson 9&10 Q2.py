# Program description: Local gas station does repairs, calculate costs
# Written by: Austin Reid
# Date written: May 16, 2023

# Constants

TAX_RATE = 0.15
LABOR_COST = 34.00

# Inputs

custName = input("Please enter the name of the customer: ")
partCost = float(input("Please enter the cost of the parts: "))
numLab = int(input("Please enter the number of labor hours: "))

labCost = LABOR_COST * numLab
subTotal = labCost + partCost
subTax = (subTotal * TAX_RATE) + subTotal
total = subTotal + subTax

if total >= 500:
    discCost = total - (total * 0.10)
   
else:
   pass

# Outputs

print(f"The name of the customer is: {custName}")
print(f"The cost of the parts is: {partCost}")
print(f"The number of labor hours is: {numLab}")
print("-"*30)
print(f"The labor cost is: ${labCost:,.2f}")
print(f"The sub total is: ${subTotal:,.2f}")
print("-"*30)
print(f"With taxes the price is: ${subTax:,.2f}")

if total >= 500:
    discCost = total - (total * 0.10)
    print(f"In total the discount cost is: ${discCost:,.2f}")
else:
   print(f"In total the cost is: ${total:,.2f}")
print("-"*30)




