# Comment like a pro.

# Constants.

# Main Program.

while True:

    while True:
        cCardNum = input("Enter the credit card number: (16 Digits): ")

        if cCardNum == "":
            print("Error - credit card number cannot be empty.")
        elif len(cCardNum) != 16:
            print("Error - credit card number must be 16 digits.")
        elif not cCardNum.isdigit():
            print("Error - credit card number must be digits.")
        elif cCardNum[0] != "4" and cCardNum[0] != "5":
            print("Error - First digit must be either a 4 or 5.")
        else:
            break

    cCardNum = (
        f"{cCardNum[0:4]}  {cCardNum[4:8]} {cCardNum[8:12]} {cCardNum[12:]}")
    print(cCardNum)


    while True:
        allowed_letters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        allowed_numbers = set("0123456789")
        postal = input("Enter the postal code (L0L0L0):").upper()

        if postal == "":
            print("Error - Postal Code cannot be empty.")
        elif len(postal) != 6:
            print("Error - Postal code must be 6 characters.")
        elif not set(postal[0::2]).issubset(allowed_letters):
            print("Error - First, third and fifth characters must be letters.")
        elif not set(postal[1::2]).issubset(allowed_numbers):
            print("Error - Second, fourth and sixth characters must be digits.")
        else:
            break

    print(postal)

'''
    while True:
        prov = input("Enter the province (LL): ")

        if prov == "":
            print("Error - Province cannot be empty.")
        elif len(prov) != 2:
            print("Error - Province must be only 2 characters.")
        elif prov != "NL" and prov != "NS" and prov != "PE" and prov != "NB":
            print("Error - Province is invalid.")
        else:
            break    
'''

'''
title ="Mr."
custFirst = "john"
custLast = "doe"

fullName = title + " " + custFirst + " " + custLast
print(fullName)


fullName = custFirst[0].title() + ". " + custLast.capitalize()
print(fullName)

fullName = (f"{title} {custFirst[0].capitalize()}. {custLast.title()}")
print(fullName)

fullName = (f"{custLast.capitalize()}, {custFirst.title()}")
print(fullName)

fullName = (f"{custLast.title()}, {custFirst[0].capitalize()}.")
print(fullName)


deptName = "information technology".title()
print(deptName)



curDate = "2023-05-31"
custfirst = "John"
custlast = "Doe"
locCode = "AJRD".upper()    
transitCode = 14974
custCount = 4768


trackNum = (f"{custfirst[0]}{custLast[0]}-{locCode[0:2]}-{str(transitCode)[3:5]}-{curDate[0:4]}{str(custCount)}")
print(trackNum)


while True:

    allowed_upper = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    allowed_lower = set("abcdefghijklmnopqrstuvwxyz")
    allowed_numbers = set("0123456789")

    passWord = input("Enter a password: ")

    numUpper = 0
    numLower = 0 
    numNum = 0 
    numSpec = 0

    for charLet in passWord:
        if not set(charLet).issubset(allowed_upper):
            numUpper += 1
        elif set(charLet).issubset(allowed_lower):
                numLower += 1
        elif set(charLet).issubset(allowed_numbers):
                numNum += 1
        else:
                numSpec += 1

    print(numUpper, numLower, numNum, numSpec)


    if passWord == "":
        print("Error - Password cannot be empty.")
    elif len(passWord) < 7:
        print("Error - Must be at least 7 characters.")
    elif numLower == 0 or numUpper == 0 or numNum == 0 or numSpec == 0:
        print("Error - Password must have 1 uppercase, 1 lowercase, 1 number and  1 special case.")
    else:
        break

print(passWord)
'''
