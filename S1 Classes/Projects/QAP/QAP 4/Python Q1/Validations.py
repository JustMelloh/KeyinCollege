
allowed_letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
allowed_numbers = set("0123456789")
# Provinical Validation


def provVA(Prov):
    if Prov not in ["AB", "BC", "NL", "ON", "NB", "PE", "QC", "SK", "YT", "NU","NS", "NT", "MB"]:
        print("Error: Invalid Province")
        return True
    elif not set(Prov).issubset(allowed_letters):
        print("Error: Must provide letters.")
        return True
        
            
    elif Prov == "":
        print("Error: Must provide entry.")
        return True
    else:
        return False
        
def phoneVa(custPhone):
    if custPhone == "":
        print("Error - Phone number cannot be blank.")
        return True
    elif not len(custPhone) == 10:
        print("Error - Phone number must be 10 characters.")
        return True
    else:
        return False
    
def postalVa(postCode):
    if postCode == "":
        print("Error: Must provide entry.")
        return True
    elif not len(postCode) == 6:
        print("Error: Must be 6 characters.")
        return True
    elif postCode[0] not in allowed_letters or postCode[2] not in allowed_letters or postCode[4] not in allowed_letters:
        print("Error: Invalid format entry must be (L1L1L1)")
        return True
    elif postCode[1] not in allowed_numbers or postCode[3] not in allowed_numbers or postCode[5] not in allowed_numbers:
        print("Error: Invalid format entry must be (L1L1L1)")
        return True
    else:
        return False
    
def carVa(numCars):
    if numCars == "":
        print("Error: Must provide entry.")
        return True
    else:
        return False

def liabilityVa(Liability):
    if Liability == "":
        print("Error: Must provide entry.")
        return True
    elif Liability != "Y" and Liability != "N":
        print("Error: Must be (Y/N)")
        return True
    elif Liability == "Y" and Liability == "N":
        return True
    else:
        return False
    
def glassCovVa(glassCov):
    if glassCov == "":
        print("Error: Must provide entry.")
        return True
    elif glassCov != "Y" and glassCov != "N":
        print("Error: Must be (Y/N)")
        return True
    elif glassCov == "Y" and glassCov == "N":
        return True
    else:
        return False
    
def loanerVa(optLoaner):
    if optLoaner == "":
        print("Error: Must provide entry.")
        return True
    elif optLoaner != "Y" and optLoaner != "N":
        print("Error: Must be (Y/N)")
        return True
    elif optLoaner == "Y" and optLoaner == "N":
        return True
    else:
        return False

payLst = ["Full", "Monthly"]
def typePayVa(typePay):
    if typePay == "":
        print("Error: Must provide entry.")
        return True
    elif typePay not in payLst:
        print("Error: Must provide either Full or Monthly Pay")
        return True
    else:
        return False
