# Comment like a pro.


import datetime

'''
# This is the inputs.
while True:
    try:
        invDate = input("Enter the invoice date (YYYY-MM-DD): ")
        invDate = datetime.datetime.strptime(invDate, "%Y-%m-%d")
    except:
        print("Error - Invalid date format. Enter as YYYY-MM-DD.")
    else:
        break

while True:
    try:
        invAmount = float(input("enter the invoice amount: "))
    except:
        print("Error - Invalid entry for the invoice amount.")
    else:
        break

# These are the calculations.

disDate = (invDate + datetime.timedelta(days = 10))
disAmt = invAmount - (invAmount * 0.02)

invDueDate = (invDate + datetime.timedelta(days = 40))

curDate = datetime.datetime.now()
invAge = (curDate - invDate).days

print(f"Original invoice amount:         ${invAmount:,.2f}")
print(f"Discount Date:                   {disDate.strftime('%Y-%m-%d')}")
print(f"Discounted invoice amount:       ${disAmt:,.2f}")
print(f"Invoice due date:                {invDueDate.strftime('%Y-%m-%d')}")
print(f"Invoice age:                     {invAge}")
'''

while True:
        expDate = input("Enter the expiry date (MM/YY): ")

        try:
            expYear = int(expDate[3:5])
            expMonth = int(expDate[0:2])
            currYear = datetime.datetime.now().year - 2000

        except:
            print("Error - Invalid format, must use MM/YY")
        else:               
            if expDate[2] != "/":
                print("Error - Invalid format ")
            elif expMonth < 1 or expMonth > 12:
                print("Error - invalid month. Must be between 1 and 12")
            elif expYear > currYear + 4:
                print("Error - Invalid year. Must be within 4 years of the current year.")
            elif expYear < currYear:
                print("Error - Card is expired.")
            else:
                break
