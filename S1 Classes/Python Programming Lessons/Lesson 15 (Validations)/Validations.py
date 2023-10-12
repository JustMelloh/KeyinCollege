# Comment like a pro xD
'''
while True:

    # User inputs and Validations
    custName = input("Enter customer name: ")

    if custName == "":
        print("Error - the customer name cannot be empty")
    else:
        break

while True:
    phoneNumber = input("Enter phone number (999-999-9999): ")

    if phoneNumber =="":
        print("Error - the phone number cannot be empty")
    else:
        break

while True:
    bikeCode = input("Enter the type of bike rented (T, M, B): ").upper()

    if bikeCode == "":
        print("Error - the bike code cannot be empty")
    elif bikeCode != "T" and bikeCode!= "M" and bikeCode!= "B":
        print("Error - the bike code must be either T, M or B")
    else:
        break

while True:

    try:
        numRented = int(input("Enter the number of rented bikes (1-3): "))
    except:
        print("Error - the number of rented bikes must be an integer")
    else:
        if numRented < 1 or numRented > 3:
            print("Error - the number of rented bikes must be between 1 and 3")
        else:
            break

ccNum = input("Enter the credit card number: ")
expDate = input("Enter the expiration date (MM/YY): ")

# Calculations and Outputs

print()

while True:
        
    Continue = input("Do you want to process another rental? (Y / N): ").upper()

    if Continue == "":
        print("Error - Continue cannot be blank")

    elif Continue != "Y" and Continue!= "N":
        print("Error - Continue must be either Y or N")

    else:
        break

    if Continue == "N":
        break
    
print("Thank you for using the validation program!")
'''
'''
while True:
    afterHours = input("Was this job completed after hours? (Y / N): ").upper()

    if afterHours == "":
        print("Error - the after hours cannot be blank")

    elif afterHours != "Y" and afterHours!= "N":
        print("Error - the after hours must be either Y or N")
        
    else:
        break


while True:

    try:
        hours = int(input("Enter the number of hours worked (1-20): "))
    except:
        print("Error - the number of hours worked must be an integer")
    else:
        if hours < 1 or hours > 20:
            print("Error - Number of hours worked must be between 1 and 20")
        else:
            break
'''


# Main Program

while True:

    # User inputs and Validations

    while True:
        custName = input("Enter customer name: ")

        if custName == "":
            print("Error - the customer name cannot be empty")
        
        else:
            break

    while True:
        phoneNumber = input("Enter phone number (999-999-9999): ")

        if phoneNumber =="":
            print("Error - the phone number cannot be empty")
        elif len(phoneNumber) != 10:
            print("Error - the phone number must be 10 digits")
        elif phoneNumber.isdigit()== False:
            print("Error - the phone number must only contain digits")
            # Function syntax is FuncName(parameters)
            # Method syntax is VariableName.MethodName(parameters)
        else:
            break

while True:
    cMM = input("Enter the car year make and model: ")

    if cMM =="":
        print("Error - the car year make and model cannot be empty")

    else:
        break
    

while True:
    try:
        carPrice = float(input("Enter the price of the car(1000.00 - 10000.00): "))
    except:
        print("Error - Car price is not a valid number.")
    else:
        if carprice < 1000.00 or carprice > 10000.00:
            print("Error - Car price must be between 1000.00 and 10000.00")
        
        else:
            break

while True:
    try:
        trade = float(input("Enter the trade in allowance: "))
    except:
        print("Error - Trade in allowance is not a valid float.")
    else:
        if trade > 10000.00:
            print("Error - Trade in cannot exceed 10000.00.")
        elif trade < 10000.00:
            print("Kill me first")



print()
    
while True:
        Continue = input("Do you want to process another rental (Y / N): ").upper()
        if Continue == "":
            print("Error - Continue cannot be blank.")
        elif Continue != "Y" and Continue != "N":
            print("Error - Continue ust be a Y or an N.")
        else:
            break
        if Continue == "N":
            break

print("Thank you for using the validation program.")