########################################################################################################################
#Program Desctiption: Evaluate retail staff on a weekly basis.
########################################################################################################################

# Constants

HOUR_PAYMENT = 26.00
COMMISSION_RATE = 0.01




# Inputs and variables

while True:
    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'")
    regName = input("Please enter the name of the region you would like to evaluate: ")

    if regName == "":
        print("Please enter a valid region name.")

    elif set(regName).issubset(allowed_char) == False:
        print("Please enter a valid region name.")
    
    else:
        break

# Check for proper inputs on first name.

while True:
    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'")
    firstName = input("Please enter the first name of the employee:")

    if firstName == "":
        print("Please enter a valid first name.")
    elif set(firstName).issubset(allowed_char) == False:
        print("Names can only contain letters, ' and -.")
    
    else:
        break

# Check for proper inputs on last name.

while True:
    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'")
    lastName = input("Please enter the last name of the employee:")

    if lastName == "":
        print("Please enter a valid last name.")
    elif set(lastName).issubset(allowed_char) == False:
        print("Names can only contain letters, ' and -.")

    else:
        break

#Check for proper inputs on sales.

while True:

    try:
        salesWeek = float(input("Please enter the sales for the week (0.00 - 30000.00):"))
    except:
        print("Please enter a valid number with decimal places.")
        
    if salesWeek == "":
        print("Please enter a number for sales.")
    elif salesWeek > 30000.00:
        print("Cannot exceed 30000.00")
        
    else:
        break


# Check for proper inputs on hours worked.
while True:
    try:
        hourWorked = int(input("Please enter the hours worked during the week (0 - 60):"))
    except:
        print("Please enter a valid number")

    if hourWorked == "":
        print("Please enter a number for hours worked.")
    elif hourWorked > 60:
        print("Cannot exceed 60 hours worked.")
    elif hourWorked < 10:
        print("Cannot be less than 10 hours worked.")
    else:
        break

# Calculations 

grossPay = (hourWorked * HOUR_PAYMENT)
commissionPay = (grossPay * COMMISSION_RATE)

if commissionPay < 250.00:
    grossPay -= commissionPay


if grossPay == "":
        print("Please enter a number.") 
elif grossPay > 30000.00:
        print("Cannot exceed 30000.00")
elif grossPay < 20000.00:
        print("Above Average.")
elif 10000.00 > grossPay < 20000.00:
        print("OK.")
else:
    print("Below Average.")
    
for i in range(2,21):
    grosspayPerc = grossPay * (i / 100)
    commissionPayPerc = grosspayPerc * COMMISSION_RATE
    finalPayPerc = grosspayPerc + commissionPayPerc
    print(f"Pay after a {i}% increase is ${finalPayPerc:.2f} and commission is ${commissionPayPerc:.2f}")

    break

