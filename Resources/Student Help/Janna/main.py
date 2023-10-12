# Program used to print formatted results for St. John's Marina & Yacht Club
# Program written by: Janna Coles
# Program written on: May 26, 2023

# Program inputs

MemName = "Janna ET Coles"  # input member name
StreetAdd = "6 Collegiate Drive"   # input the street address
City = "Roddickton,"  # input the city
Prov = "Nl"    # input("Enter the province (NL, NB, ...)
Postal = "A0K4P0"    # input("Enter the postal code (A1A1A1)
PhoneNum = "7094572814"    # input("Enter the phone number (7094577179): ")
CellNum = "7094577179"   # input("Enter the cell phone number (7094577179): ")
MemType = input("Enter the member type (S for standard, E for executive): ").upper()  # input the member type
SiteNum = input("Enter the site number (1-100): ")  # input the site number
SiteNum = int(SiteNum)  # Convert to an integer
AltMem = input("Enter the number of alternate members: ")  # input the number of alternate members
AltMem = int(AltMem)  # Convert to an integer

SiteClean = input("Enter (Y for yes or N for no) if the member would like to have a weekly site clean: ").upper()
# input Y or N if site is cleaned

VidSur = input("Enter (Y for yes or N for no) if the member would like video surveillance on their site: ").upper()
# input Y or N if site is under video surveillance

# Program Constants
EVEN_NUMBERED_SITES = 80.00  # cost of an even numbered site
ODD_NUMBERED_SITES = 120.00  # cost of an odd numbered site
ALTERNATE_MEMBER_FEE = 5.00  # cost of 1 extra alternate member
SITE_CLEANING_FEE = 50.00  # cost of site clean per month
VIDEO_SURVEILLANCE = 35.00  # cost of video surveillance per month
HST_RATE = .15  # tax rate
STANDARD_MONTHLY_DUES = 75.00  # monthly dues for a standard membership
EXECUTIVE_MONTHLY_DUES = 150.00  # monthly dues for an executive membership
CANCEL_RATE = .60  # cancellation rate
PROCESSING_FEE = 59.99  # processing fee per year

# Program Calculations


if (SiteNum % 2) == 0:
    SiteCharge = EVEN_NUMBERED_SITES          # Calculate site charge on even/odd numbered sites
else:
    SiteCharge = ODD_NUMBERED_SITES


if MemType == "S":
    MonthDues = STANDARD_MONTHLY_DUES
    MemTypeDsp = "Standard"
elif MemType == "E":                         # Calculate the cost of each membership type
    MonthDues = EXECUTIVE_MONTHLY_DUES
    MemType = "Executive"
else:
    MonthDues = 0


if SiteClean == "Y":
    CleanFee = SITE_CLEANING_FEE
    SiteCleanDsp = "Yes"                    # Calculating Cleaning Cost per month
elif SiteClean == "N":
    SiteCleanDsp = "No"
    CleanFee = 0
else:
    CleanFee = 0


if VidSur == "Y":
    VidFee = VIDEO_SURVEILLANCE
    VidSurDsp = "Yes"                        # Calculating Video Surveillance per month
elif VidSur == "N":
    VidSurDsp = "No"
    VidFee = 0
else:
    VidFee = 0

# Program Calculations
TotalAltMemCost = AltMem * ALTERNATE_MEMBER_FEE     # Calculate the total cost of total alt. members

TotalSiteCharge = SiteCharge + TotalAltMemCost      # Calculate the total site charge per month

ExtCharge = CleanFee + VidFee                       # Calculate the total extra charges

SubTot = TotalSiteCharge + ExtCharge                # Calculate the subtotal

SalesTax = SubTot * HST_RATE                        # Calculate the sales tax on subtotal

MonthCharge = SubTot + SalesTax                     # Calculate the total monthly charge

TotMonFee = MonthCharge + MonthDues                 # Calculate the total monthly fee

YearlyFee = TotMonFee * 12                          # Calculate the total yearly fee

MonthPay = (YearlyFee + PROCESSING_FEE) / 12        # Calculate the total monthly payment

YearlySiteFee = TotalSiteCharge * 12                # Calculate the total yearly site fee

CancelFee = YearlySiteFee * CANCEL_RATE             # Calculate the cancellation fee

# Print Program Outputs

print()
print(f"                            St. John's Marina & Yacht Club")
print(f"                                 Yearly Member Receipt    ")
print()
print("                    ---------------------------------------------")
print()
print(f"                    Client Name and Address:")
print()
print(f"                    {MemName:<23s}")
print(f"                    {StreetAdd:<23s}")
print(f"                    {City:<14s}               {Prov:<2s}       {Postal:<6s} ")
print()
print(f"                    Phone:{PhoneNum:>10s} (H)")
print(f"                          {CellNum:>10s} (C)")
print()
print(f"                    Site #: {SiteNum:<3d}    Member type:        {MemTypeDsp:>9s}")

print()
print(f"                    Alternate members:                        {AltMem:>2d}")
print(f"                    Weekly site cleaning:                    {SiteCleanDsp:>3}")
print(f"                    Video surveillance:                      {VidSurDsp:>3}")
print()

TotalSiteChargeDsp = "${:,.2f}" .format(TotalSiteCharge)
print(f"                    Site Charge:                       {TotalSiteChargeDsp:>9s}")

ExtChargeDsp = "${:,.2f}" .format(ExtCharge)
print(f"                    Extra Charges:                        {ExtChargeDsp:>6s}")
print(f"                                                    -------------")
print()

SubTotDsp = "${:,.2f}" .format(SubTot)
print(f"                    Subtotal:                            {SubTotDsp:>6s}")

SalesTaxDsp = "${:,.2f}" .format(SalesTax)
print(f"                    Sales Tax (HST):                     {SalesTaxDsp:>7s}")
print(f"                                                   --------------")
print()

MonthChargeDsp = "${:,.2f}" .format(MonthCharge)
print(f"                    Total Monthly Charges:               {MonthChargeDsp:>6s}")

MonthDueDsp = "${:,.2f}" .format(MonthDues)
print(f"                    Monthly dues:                        {MonthDueDsp:>7s}")
print(f"                                                     ------------")
print()

TotMonFeeDsp = "${:,.2f}" .format(TotMonFee)
print(f"                    Total monthly fees:                  {TotMonFeeDsp:>6s}")

YearlyFeeDsp = "${:,.2f}" .format(YearlyFee)
print(f"                    Total yearly fees:                {YearlyFeeDsp:>10s}")
print()

MonthPayDsp = "${:,.2f}" .format(MonthPay)
print(f"                    Monthly payment:                     {MonthPayDsp:>6s}")
print()
print(f"                   ----------------------------------------------")
print()
print(f"                    Issued: 2023-05-26  ")
print(f"                    HST Reg No: 549-33-5849-4720-9885")
print()

CancelFeeDsp = "${:,.2f}" . format(CancelFee)
print(f"                    Cancellation fee:                  {CancelFeeDsp:>8s}")
print()


















