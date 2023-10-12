################################################################
# Program Description: Create a program that tracks the amount of yachts docked, how much to charge, and if the members paid there bill.
# Program Author: Austin Reid
# Program Date: 2023/05/24
################################################################
# Imports

import re

# Constants

EVEN_NUMBER_SITE_RATE = 80.00
ODD_NUMBER_SITE_RATE = 120.00
STANDARD_MEMBER_RATE = 75.00
EXECUTIVE_MEMBER_RATE = 150.00
ALT_MEMBER_RATE = 5.00
WEEKLY_SITE_CLEANER_RATE = 50.00
VIDEO_SURVEILLANCE_RATE = 35.00
TAX_RATE = 0.15

# User inputs

siteNumber = int(input("Enter the site number: "))
memberName = input("Enter the name of the member: ")
streetAdd = input("Enter the street address: ")
city = input("Enter the city: ")
province = input("Enter the province: ")
postalCode = input("Enter the postal code: ").upper()
cellNumber = input("Enter the cell number: ")
phoneNumber = input("Enter the phone number: ")
membershipType = input("Enter the membership type (S) or (E): ").upper()
altNumMembers = int(input("Enter the number of alternate members: "))
wSiteCleaner = input("Is there a site cleaner (Y) or (N): ").upper()
videoSurv = input("Is there a video surveillance (Y) or (N): ").upper()


# Calculations

# Remove non-digits from phone number using define function
def format_phone_number(phoneNumber):
    phoneDigits = re.sub(r'\D', '', phoneNumber)

    #Format the phone number

    formattedPhoneNumber = re.sub(r'^(\d{1})(\d{3})(\d{3})(\d{4})$', r'+\1 (\2) \3-\4', phoneDigits)

    return formattedPhoneNumber

def format_cell_number(cellNumber):
    cellDigits = re.sub(r'\D', '', cellNumber)

    #Format the cell number

    formattedcellNumber = re.sub(r'^(\d{1})(\d{3})(\d{3})(\d{4})$', r'+\1 (\2) \3-\4', cellDigits)
    return formattedcellNumber

formatted_Phone = format_phone_number(phoneNumber)
formatted_Cell = format_cell_number(cellNumber)




# Determine what extra charges to add

if wSiteCleaner == "Y":
    cleanFee = WEEKLY_SITE_CLEANER_RATE
    wSiteCleanerDSP = "Yes"
    
elif wSiteCleaner == "N":
        cleanFee = 0
        wSiteCleanerDSP = "No"

if videoSurv == "Y":
    videoFee = VIDEO_SURVEILLANCE_RATE
    videoSurvDSP = "Yes"
elif videoSurv == "N":
    videoSurvDSP = "No"
    videoFee = 0


#  If the siteNumber is even
altMemCost = altNumMembers * ALT_MEMBER_RATE

siteNumberMod = siteNumber % 2

if siteNumberMod <= 0:

    siteCharges = EVEN_NUMBER_SITE_RATE + altMemCost

elif siteNumberMod > 0:
    siteCharges = ODD_NUMBER_SITE_RATE + altMemCost

extraCharges = cleanFee + videoFee 
subTotal = siteCharges + extraCharges


salesTax = (subTotal * TAX_RATE)
monthlyCharge = (subTotal + salesTax)

if membershipType == "S":
        monthlyDues = STANDARD_MEMBER_RATE
        memType = "Standard"
elif membershipType == "E":
        monthlyDues = EXECUTIVE_MEMBER_RATE
        memType = "Executive"


# calculate the total charge and monthly dues to get Total Monthly Fees

totalMonthlyFees = monthlyCharge + monthlyDues

# Calculate yearly fees

yearlyFees = totalMonthlyFees * 12
monthlyPay = (yearlyFees + 59.99) / 12
cancelFee = yearlyFees * 0.6

# Outputs

print("    St.John's Marina & Yacht Club")
print("         Yearly Member Recipt")
print("-"*36)
print("Client Name and Address:")
print()
print(memberName)
print(streetAdd,",", city)
print(province,",", postalCode)
print()
print("Home Phone: ", formatted_Phone, "(H)")
print("Cell Phone: ", formatted_Cell, "(C)")
print()
print("Site#: ", siteNumber, f"Member Type:   {memType:>9s}")
print()

print(f"Alternate Members:               {altNumMembers:>3d}")
print(f"Weekly Site Cleaning:            {wSiteCleanerDSP:>3s}")
print(f"Video Surveillance:              {videoSurvDSP:>3s}", )
print()

print("Site Charges:                 " f"{f'${siteCharges:.2f}':<9}")
print("Extra Charges:               ", f"{f'${extraCharges:.2f}':<9}")
print(" "*26, "-"*9)
print("Subtotal:                   ", f"{f'${subTotal:.2f}':<9}")
print("Sales tax (HST):             ", f"{f'${salesTax:.2f}':<9}")
print(" "*26, "-"*9)
print("Total monthly charges:      ", f"{f'${monthlyCharge:.2f}':<9}")
print("Total Monthly dues:         ", f"{f'${monthlyDues:.2f}':<9}")
print(" "*26, "-"*9)
print("Total monthly fees:         ", f"{f'${totalMonthlyFees:.2f}':<9}")
print("Total yearly fees:         ", f"{f'${yearlyFees:.2f}':<9}")
print()
print("Monthly Payments:          ", f"{f'${monthlyPay:.2f}':<9}")
print("-"*36)
print()
print("Issues: 2023-05-24")
print("HST Reg No: 549-33-5849-4720-9885")
print()
print("Cancellation Fee:          ", f"{f'${cancelFee:.2f}':>8}")