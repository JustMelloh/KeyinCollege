# Comments

# Import Libraries
import matplotlib as plt
import datetime as dt

# Define Constants

# Main Program

while True:
        # Set up required user inputs.

    listingNum = input("Enter the listing number (XXXXXXXXX): ")

    if listingNum == "":
            print("Error - Listing number cannot be blank.")
    elif len(listingNum) != 9:
            print("Error- listing number must be 9 characters.")
    elif listingNum.isdigit():
            print("Error - Listing number must be 9 digits")
    else:
            break


    stAdd = input("Enter the street address: ")
    while True:
        try:
            numBed = int(input("Enter the number of bedrooms: "))
        except:
            print("Error - Number of bedrooms must be a valid number.")
        else: 
            break
    numBath = int(input("Enter the number of bathrooms: "))
    totSqFt = int(input("Enter the total square footage: "))

    priceLst = []
    dateLst = []
while True:
        listingPrice = float(input("Enter the listing price (-1 to end): "))
        if listingPrice == -1:
                    break
        while True:
            try:
                listingDate = input("Enter the listing date (YYYY-MM-DD): ")
                listingDate = dt.strptime(listingDate, "%Y-%m-%d")
            except:
                    print("Error - Listing price not a valid date.")
            else:
                break

priceLst.append(listingPrice)
dateLst.append(listingDate)

statusLst = ["Open", "Offer Pending", "Sold"]
while True:

    Status = input("Enter the home stats (Open, Offer Pending or Sold.): ").title()
        
    if Status == "":
                print("Error - Status cannot be blank.")
    elif Status not in statusLst:
                print("Error - Must be either (Open, Offer Pending or Sold.)")
    else:
        break
# Calculations if there are any.


# Display Results


    print(f"Listing number:                       {listingNum}")
    print(f"Street Address:                       {stAdd}")
    print(f"Number of bedrooms:                   {numBed}")
    print(f"Number of bathrooms:                  {numBath}")
    print(f"Total Square footage:                 {totSqFt}")
    print()



