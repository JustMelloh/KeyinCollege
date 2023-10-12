########################################################################################################################
# Program Description: Calculate electricity used in the last month.
# Written by: May 17 2023
# Date: May 17 2023
########################################################################################################################################################



# Constants

DISC_RATE_500 = 0.03
DISC_RATE = 0.01
HST_RATE = 0.15



# Inputs

custName = input("Enter customer's name: ")
streetAddress = input("Enter street address: ")
lastMonth = int(input("Enter last month: "))
currentMonth = int(input("Enter current month: "))

kiloUsed = currentMonth - lastMonth

# Variables

if  kiloUsed< 100:
    kiloPay = (0.073 * kiloUsed) 
elif kiloUsed >= 100:
    kiloPay = (0.069 * kiloUsed)

if kiloUsed > 500.00:
    discRed = (kiloPay * DISC_RATE_500)
elif kiloUsed <= 500.00:
    discRed = (kiloPay * DISC_RATE)

subTotal = (kiloPay - discRed)
HST = (subTotal * HST_RATE)
total = (subTotal + HST)
totalDisc = (total - discRed)

# Outputs

print("Customer's name: " + custName)
print("Street address: " + streetAddress)
print("Last month: " + str(lastMonth))
print("Current month: " + str(currentMonth))
print()

print("Kilowatts used: ", kiloUsed)

print(f"Discounts: ${discRed:.2f}"),
print(f"HST: ${HST:.2f}")
print(f"Subtotal: ${subTotal:.2f}")
print(f"Total: ${total:.2f}")
print(f"Total Discount: ${totalDisc:.2f}")
print()
print("Payments before the 25th of the month are the discounted amount\n, and payments after the 25th of the month is the total charge.")