
# ------------Title: QAP 3_HONEST HARRY's USED CAR LOT
# Program Description: This program will function as a way to keep track of
# "HARRY'S USED CAR LOT" sales of used vehicles. It will also calculate the cost of
# the car which will include the License Fee and appropriate taxes. It will also include
# the input of Client Data.
#
# Author: Meghan McKinlay & SD9
# Date Written: June 10th, 2023

import datetime

# ----------- Program Constants:
STANDARD_LICENSE_FEE = 75.00
EXEC_LICENSE_FEE = 165.00
HST_RATE = 0.15
LUXURY_TAX = 0.016
MAX_SELL_PRICE = 50000.00

# ----------- PROGRAM FUNCTIONS / CALCULATIONS

# The licence fee is standard rate in NL of $75.00 on cars up to and
# including $5,000.00 and $165.00 on cars over $5,000.00.
def CalcLicFee(Price):
    Fee = 0.00
    if Price <= 5000.00:
        Fee = 75.00
    else:
        Fee = 165.00
    return Fee

# print(f"{LicFee=}")

# The transfer fee 1% of the selling price -
# if the selling price is more than $20,000.00,
# an additional 1.6% luxury tax is calculated on the selling price
# and added to the transfer fee.

def CalcTransFee(Price):
    TransFee = Price * 0.01
    if Price > 20000.00:
       TransFee = TransFee + (Price * LUXURY_TAX)
    return TransFee

while True:

# ------------------- CUSTOMER FIRST NAME
    while True:
        FirstName = input("Enter First Name: ")
        if FirstName == "":
            print("ERROR - FIELD CANNOT BE BLANK")
        else:
            break

# -------------------- CUSTOMER LAST NAME
    while True:
        LastName = input("Enter Last Name: ")
        if LastName == "":
            print("ERROR - FIELD CANNOT BE BLANK")
        else:
            break

# ------------------- PHONE NUMBER
    while True:
        PhoneNum = input("Enter Phone Number (###-###-####): ")
        if PhoneNum == "":
            print("ERROR - FIELD CANNOT BE BLANK.")
        elif len(PhoneNum) != 10:
                print("ERROR - PHONE NUMBER IS INVALID.")
        elif not PhoneNum.isdigit():
                print("ERROR - PHONE NUMBER IS INVALID.")
        else:
                break

# ------------------- LICENSE PLATE NUMBER
    while True:
        allowed_letters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        allowed_numbers = set("0123456789")
        LicPlate = input("Enter License Plate number (AAA999): ").upper()

        if LicPlate == "":
                print("ERROR - FIELD CANNOT BE BLANK.")
        elif len(LicPlate) != 6:
                print("ERROR - ENTER 6 DIGIT PLATE NUMBER.")
        elif not set(LicPlate[0:1:2]).issubset(allowed_letters):
                print("ERROR - PLATE NUMBER MUST BEGIN WITH 3 LETTERS.")
        elif not set(LicPlate[3:4:5]).issubset(allowed_numbers):
                print("ERROR - PLATE NUMBER MUST END WITH 3 NUMBERS.")
        else:
            break

    CarMake = input("Enter Car Make:  ")
    CarModel = input("Enter Car Model: ")
    CarYear = input("Enter Car Year: ")
    while True:
            SellPrice = float(input("Enter Selling Price: "))
            if SellPrice > MAX_SELL_PRICE:
                print("ERROR - PRICE CANNOT EXCEED $50,000.")
            else:
                break

    while True:
            TradeIn = float(input("Enter Trade in Amount: "))
            if TradeIn > SellPrice:
                print("ERROR - TRADE IN AMOUNT CANNOT EXCEED THE SELLING PRICE.")
            else:
                break

    while True:
        prov = input("Enter the province (LL): ").upper()
        if prov == "":
            print("ERROR - FIELD CANNOT BE BLANK.")
        elif len(prov) != 2:
            print("ERROR - PROVINCE SHOULD BE 2 CHARACTERS.")
        else:
            break

    SalesName = input("Enter the Salesperson's Name: ")
    StreetAddress = input("Enter Street Address: ")
    City = input("Enter City: ")
    Prov = input("Enter Province: ")
    PostalCode = input("Enter Postal Code: ")

    PATAmnt = SellPrice - TradeIn   # PAT = Price After Trade amount
    # print(f"{SellPrice} - {TradeIn} = {PATAmnt}")
    LicFee = CalcLicFee(PATAmnt)

    # ----------------- FUNCTIONS
    TransFee = CalcTransFee(SellPrice)
    # print(f"{TransFee=}")
    Subtotal = PATAmnt + LicFee + TransFee
    # print(f"PATAmnt {PATAmnt} + LicFee {LicFee} + TransFee {TransFee} = {Subtotal}")
    HST = Subtotal * HST_RATE
    TotSalesPrice = Subtotal + HST

    # -------------- PROGRAM OUTPUTS
    # The program should create a Receipt ID for the sale in the form XX-XXX-XXXX
    # the first two characters are the customer initials
    ReceiptID = FirstName[0] + LastName[0] + "-"
    # the middle 3 characters are the last 3 digits in the license plate number
    ReceiptID = ReceiptID + LicPlate[3:] + "-"
    # the final 4 characters are the last 4 digits of the phone number
    ReceiptID = ReceiptID + PhoneNum[6:]

    InvoiceDate = datetime.date.today()
    print()

    print("         1         2         3         4         5         6         7")
    print("123456789012345678901234567890123456789012345678901234567890123456789012345678")
    print(f"Honest Harry Car Sales                         Invoice Date: {InvoiceDate}")
    print(f"Used Car Sale and Receipt                      Receipt No:     {ReceiptID}")
    print()
    print(f"                                               Sale Price:${SellPrice:,.2f}")
    print(f"Sold to:                                       Trade Allowance:${TradeIn:,.2f}")
    print("                                               -------------------------------")
    print(f"       {FirstName[0]}. {LastName:<26s}                Price after Trade: ${PATAmnt:,.2f}")
    print(f"       {StreetAddress:<.29s}                          License Fee: ${LicFee:,.2f}")
    print(f"       {City:<.19s},{Prov:<2s} {PostalCode}            Transfer Fee: ${TransFee:,.2f}")
    print(f"                                              -------------------------------")
    print(f"Car Details:                                   Subtotal: ${Subtotal:,.2f}")
    print(f"                                               HST: {HST:,.2f}")
    print(f"        {CarYear:<4s} {CarMake:<13s} {CarModel:<10s}       ---------------------------------")
    print(f"                                               Total Sales Price: {TotSalesPrice:,.2f}")
    print(f"-----------------------------------------------------------------------------------------")
    print(f"                   Best Used Cars at the Best Prices!")










