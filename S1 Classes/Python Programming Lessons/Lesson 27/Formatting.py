# Formatting for RealEstate program

# Validate Listing number


allowed_digits = "0123456789"
allowed_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def listingNum(lstNum):
    
    while True:   
            if len(lstNum) != 9:
                print("Listing number needs to be exactly 9 digits.")
            elif len(lstNum) == 9 and set(lstNum).issubset(allowed_letters):
                print("Listing number must be digits only.")  
            else:
                return True