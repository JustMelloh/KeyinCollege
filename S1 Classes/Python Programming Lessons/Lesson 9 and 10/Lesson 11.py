########################################################################################################################
# Written by: Austin Reid
# Date written: May 17, 2023
# Program description: Create program to help process orders.
########################################################################################################################

# Constants

SNUGGLE_FIRST = 29.99
SNUGGLE_SECOND = 24.99
SNUGGLE_THIRD = 21.99

SCOST_SIX = 3.99
SCOST_UNDER_SIX = 5.99
HST_RATE = 0.15
SER_CHARGE = 0.03

# Inputs


custName = input("Please enter customers' name: ")
streetAdd = input("Please enter street address: ")
city = input("Please enter city: ")
postalCode = input("Please enter postal code: ")
snuggleOrder = int(input("Please enter the amount of Snugglys' you'd like to order: "))

# Calculations 

if snuggleOrder >= 10:
    addCost = SNUGGLE_THIRD
elif snuggleOrder < 10:
    addCost = SNUGGLE_SECOND

snuggTotal = SNUGGLE_FIRST + ((addCost)*(snuggleOrder-1))

if snuggTotal >= 6:
    shipRate = SCOST_SIX
elif snuggTotal <= 6:
    shipRate = SCOST_UNDER_SIX

subTotal = snuggTotal + (shipRate*snuggleOrder)

taxTotal = (subTotal * HST_RATE) 
totalCost = taxTotal + subTotal 
serCharge = totalCost * SER_CHARGE


# Outputs

print(f"Customer Name: {custName}")
print(f"Street Address: {streetAdd}")
print(f"City: {city}")
print(f"Postal Code: {postalCode}")
print(f"Snugglys' Order: {snuggleOrder}")
print("-"*30)
print()
print(f"Subtotal is: ${subTotal:.2f}")
print(f"Total cost is: ${totalCost:.2f}")
print(f"Tax: ${taxTotal:.2f}")
print(f"serCharge: ${serCharge:.2f}")
print("-"*30)

    

