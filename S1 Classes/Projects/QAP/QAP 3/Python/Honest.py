#####################################################
# Program Description: Keep track of all sales.
# Written by: Austin Reid
# Written on: June 7, 2023
####################################################


import datetime
import re

allowed_Letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'-")
allowed_Numbers = set("01234567890")
currDate = datetime.datetime.now()
LOW_LICENSE_FEE_RATE = 75
HIGH_LICENSE_FEE_RATE = 165
TRANSFER_FEE_RATE = 0.01
TRANSFER_FEE_RATE_ADD = 0.016
TAX_RATE = 0.15


while True:

    while True:
        firstName = input("Enter the first name: (Type END to stop Program) ").title()   
        
        if firstName =="":
            print("Error: Must enter a first name.")
        elif not set(firstName).issubset(allowed_Letters):
            print("Error: Must use valid characters.")
            break
        else:
            break
    if firstName.upper() == "END":
        break
    
    while True:
        
        lastName = input("Enter the last name: ").title()
        if lastName =="":
            print("Error: Must use valid characters.")
        elif not set(lastName).issubset(allowed_Letters):
            print("Error: Must use valid characters.")
        else:
            break

    while True:
        # Get the input for the phonenumber.
        # Then format it.
        custPhone = input("Enter the customers phone number: ")
    
        if custPhone =="":
            print("Error: Must enter customers phone number.")
        elif set(custPhone).issubset(allowed_Letters):
            print("Error: Phone number must include digits.")
        elif len(custPhone) != 10:
            print("Error: Phone number must be 10 digits.")
        else:
            custPhone = format(int(custPhone[:-1]), ",").replace(",", "-") + custPhone[-1]
            break

    while True:
        #Get the plate number for the vehicle.
        plateNumber = input("Enter the plate number (AAA999): ").upper()

        if plateNumber =="":
            print("Error: License must include letters and digits.")
        elif len(plateNumber) != 6:
            print("Error: License plate must be 6 characters.")
        elif not set(plateNumber[0:1:2]).issubset(allowed_Letters):
            print("Error: First three characters must be letters.")
        elif not set(plateNumber[3:4:5]).issubset(allowed_Numbers):
            print("Error: Last three characters must be numbers.")
        else:
            break

    while True:
        # Get Make, year and model of the vehicle.

        carMake = input("Enter the make of the vehicle: ").capitalize()

        if carMake == "":
            print("Error: Must enter the make of a Car.")
        elif not set(carMake).issubset(allowed_Letters):
            print("Error: Must enter letters for the make.")
        else:
            break

    while True:
        
        carYear = input("Enter the year of the vehicle: ").capitalize()

        if carYear == "":
            print("Error: Enter the year the vehicle was made.")
        elif not set(carYear).issubset(allowed_Numbers):
            print("Error: Must enter digits for the year.")
        else:
            break

    carModel = input("Enter the model of the vehicle: ").capitalize()

    while True:
        if carModel == "":
            print("Error: Must enter a car model.")
        elif not set(carModel).issubset(allowed_Letters):
            print("Error: Please do not enter digits for the model.")
        else:
            break

    while True:

        try:

            sellPrice = float(input("Please enter the selling amount of the vehicle (Cannot exceed $50,000.00): "))
        except:
            print("Error: Selling price must be a valid number.")

        if sellPrice > 50000:
            print("The selling price cannot exceed $50,000.00.")
        else:
            break
    while True:

        try:
            tradePrice = float(input("What is the trade-in amount?: "))
        except:
            print("Error: The trade in price must be a number.")
        if tradePrice > 50000:
            print("The trade in price cannot exceed the selling price.")
        else:
            break

        # Calculations for Price after trade.

    

        # Checking to see what the rate will be for cars.
    if sellPrice <= 5000:
        licenseFee = LOW_LICENSE_FEE_RATE
    else:
        licenseFee = HIGH_LICENSE_FEE_RATE

    if sellPrice <= 20000:
        extraFee = sellPrice * TRANSFER_FEE_RATE
    elif sellPrice > 20000:
        extraFee = (sellPrice * TRANSFER_FEE_RATE) + (TRANSFER_FEE_RATE_ADD * sellPrice)
    else:
        break

# Calculate the Subtotal price.
    priceAfterTrade = (sellPrice - tradePrice)
    subTotalPrice = (priceAfterTrade + licenseFee + extraFee)
    totalTax = (subTotalPrice * TAX_RATE)
    totalPrice = (totalTax + subTotalPrice)

#Print the outputs

    print()
    print(f"Honest Harry Car Sales                          Invoice Date:   {currDate.strftime('%B-%d-%Y')}")
    print(f"Used Car Sale and Receipt                       Receipt No:     {firstName[0]}-{lastName[0]}-{plateNumber[3:6]}-{custPhone[6:12]}")
    print()
    print(f"                                                Sale Price:         {f'${sellPrice:,.2f}':>10s}")
    print(f"Sold to:                                        Trade Allowance:    {f'${tradePrice:,.2f}':>10s}")
    print(" "*40,"-"*37)
    print(f"      {firstName[0]}. {lastName}                                    Price after trade: {f'${priceAfterTrade:,.2f}':>10s}")
    print(f"      403 Melbourne Rd                           License Fee:       {f'${licenseFee:,.2f}':>10s}")
    print(f"      Blakesville, NL, A2N1X0                    Transaction Fee:   {f'${extraFee:,.2f}':>10s}")
    print(" "*40,"-"*37)

    print(f"Car Details:                                     Subtotal:          {f'${subTotalPrice:,.2f}':>10s}")
    print(f"                                                 HST:               {f'${totalTax:,.2f}':>10s}")
    print(f"      {carYear} {carMake} {carModel}                -------------------------------------")
    print(f"                                                 Total sales price: {f'${totalPrice:,.2f}':>10s}")
    print("-"*78)
    print(" "*18,"Best used cars at the best prices!")

    print()
    print()
    print()

    print(f" "*31,"Financing     Total         Monthly")
    print(f"       # Years    # Payments       Fee        Price         Payment")
    print("     ","-"*60)
    # Calculate the payments for 4 years

    for year in range(1,5):
        numMonthlyPay = (year * 12)
        financeFee = (39.99 * year)
        totalWFinance = (financeFee + totalPrice)
        monthlyPayment = totalWFinance / numMonthlyPay



        firstPay = (currDate + datetime.timedelta(days = 30))           
        print(f"        {year}            {numMonthlyPay}        {f'${financeFee:,.2f}':>8s}     {f'${totalWFinance:,.2f}':>8s}   {f'${monthlyPayment:,.2f}':>10s}")

    print("      ","-"*60)
    print(f"       Invoice Date: {currDate.strftime('%d-%b-%y')}    First Payment date: {firstPay.strftime('%d-%b-%y')}")


