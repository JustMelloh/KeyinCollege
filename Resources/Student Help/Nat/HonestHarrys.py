# Program description: This program for The St. John's Marina &
#                      Yacht Club is to track yachts docked at the
#                      club and member fees for entering appropriate
#                      information and prepare a receipt.
# Written by:          Jillian Chiarot
# Date written:        May 29 - May 31 - 2023

# Define program constants.
# All upper case - words separated with _
LICENCE_FEE_RATE = 75.00
LICENCE_FEE_OVER_RATE = 5000.00
TRANSFER_FEE_RATE = .01
LUX_TAX_RATE = 0.016
HST_RATE_RATE = .15
FINANCING_FEE_RATE = 39.99

# Set program inputs.
StAdd = "44 Newfoundland Drive"
City = "St. John's"
Province = "Newfoundland"
PostalCode = "A1A2B2"

# Main program.
while True:

    while True:
        CustFirstName = input("Enter the customer's first name (enter END to stop program): ").title()

        if CustFirstName == "":
                print("Error - Customer's first name must be entered.")
        elif CustFirstName == " ":
                print("Error - Customer's first name must be valid characters.")

        else:
             break

    while True:
        CustLastName = input("Enter the customer's last name: ").title()

        if CustLastName == "":
            print("Error - Customer's last name must be entered.")
        else:
            break

    while True:
        PhoneNum = input("Enter the phone number (1112223333): ")
        if PhoneNum == "":
                print("Error - Phone number cannot be blank.")
        elif len(PhoneNum) != 10:
                print("Error - Phone number must be 10 digits.")
        else:
                break

    while True:
        allowed_letters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        allowed_numbers = set("0123456789")
        PlateNum = input("Enter the licence plate number (AAA111): ").upper()

        if PlateNum == "":
                print("Error - Licence plate number cannot be blank.")
        elif len(PlateNum) != 6:
                print("Error - Licence plate number must be 6 characters.")
        elif not set(PlateNum[0:3]).issubset(allowed_letters):
                print("Error - Licence plate number must be typed (AAA111).")
        elif not set(PlateNum[4:7]).issubset(allowed_numbers):
                print("Error - Licence plate number must be typed (AAA111).")
        else:
                break

        CarMake = input("Enter the car make (ie: Toyota): ")
        CarModel = input("Enter the car model (ie Corolla): ")
        CarYear = input("Enter the car year (YYYY): ")

    while True:
        SellPrice = float(input("Enter the selling price: "))
        if SellPrice > 50000.00:
                print("Error - Sale price must not exceed $50,000.00.")
        else:
                break
    while True:
        TradeInAmt = float(input("Enter the amount of the trade in: "))
        if TradeInAmt > SellPrice:
                print("Error - The amount of trade in must not exceed the selling price.")
        else:
            break

    SalesPersonsName = input("Enter the sales persons name: ")

# Calculations.

    print(CustFirstName)
    print(CustLastName)
    print(StAdd)
    print(City)
    print(Province)
    print(PostalCode)
    print(PlateNum)
    print(CarMake)
    print(CarYear)
    print(SellPrice)
    print(TradeInAmt)
    print(SalesPersonsName)