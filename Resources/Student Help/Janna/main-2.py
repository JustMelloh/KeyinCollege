# Program used to print formatted results for St. John's Marina & Yacht Club
# Program written by: Janna Coles
# Program written on: May 26, 2023

# Program inputs
MemName = "Janna Coles"
StreetAdd = "6 Collegiate Drive"
City = "Roddickton"
Prov = "Nl"    # input("Enter the province (NL, NB, ...): ").upper()
Postal = "A0K4P0"    # input("Enter the postal code (A1A1A1):").upper()
PhoneNum = "7094572814"    # input("Enter the phone number (7094577179): ")
CellNum = "7094577179"   # input("Enter the cell phone number (7094577179): ")
MemType = input("Enter the member type (S for standard, E for executive): ").upper()
SiteNum = input("Enter the site number (1-100): ")
SiteNum = int(SiteNum)
AltMem = input("Enter the number of alternate members: ")
AltMem = int(AltMem)
SiteClean = input("Enter (Y for yes or N for no) if the member would like to have a weekly site clean: ").upper()
VidSur = input("Enter (Y for yes or N for no) if the member would like video surveillance on their site: ").upper()


# Program Constants
EVEN_NUMBERED_SITES = 80.00
ODD_NUMBERED_SITES = 120.00
ALTERNATE_MEMBER_FEE = 5.00
SITE_CLEANING_FEE = 50.00
VIDEO_SURVEILLANCE = 35.00
HST_RATE = .15
STANDARD_MONTHLY_DUES = 75.00
EXECUTIVE_MONTHLY_DUES = 150.00
CANCEL_RATE = .60
PROCESSING_FEE = 59.99

# Program Calculations

# Calculate even numbered sites
if (SiteNum % 2) == 0:
    SiteCharge = EVEN_NUMBERED_SITES
else:
    SiteCharge = ODD_NUMBERED_SITES


if MemType == "S":
    MonthDues = STANDARD_MONTHLY_DUES
    MemTypeDsp = "Standard"
elif MemType == "E":
    MonthDues = EXECUTIVE_MONTHLY_DUES
    MemTypeDsp = "Executive"
else:
    MonthDues = 0


if SiteClean == "Y":
    CleanFee = SITE_CLEANING_FEE
    SiteCleanDsp = "Yes"
elif SiteClean == "N":
    SiteCleanDsp = "No"
    CleanFee = 0
else:
    CleanFee = 0

if VidSur == "Y":
    VidFee = VIDEO_SURVEILLANCE
    VidSurDsp = "Yes"
elif VidSur == "N":
    VidSurDsp = "No"
    VidFee = 0
else:
    VidFee = 0

TotalAltMemCost = AltMem * ALTERNATE_MEMBER_FEE

TotalSiteCharge = SiteCharge + TotalAltMemCost

ExtCharge = CleanFee + VidFee

SubTot = TotalSiteCharge + ExtCharge

SalesTax = SubTot * HST_RATE

MonthCharge = SubTot + SalesTax

TotMonFee = MonthCharge + MonthDues

YearlyFee = TotMonFee * 12

MonthPay = (YearlyFee + PROCESSING_FEE) / 12

YearlySiteFee = SiteCharge * 12

CancelFee = YearlySiteFee * CANCEL_RATE

# Print Outputs
print()
print(f"      St. John's Marina & Yacht Club")
print(f"           Yearly Member Receipt    ")
print()
print("   -----------------------------------------")
print()
print(f"Client Name and Address:")
print()
print(f"{MemName:<23s}")
print(f"{StreetAdd:<23s}")
print(f"{City:e<14s}  {Prov:<2s}  {Postal:<6s} ")
print()
print(f" Phone:          {PhoneNum:<10s} (H)")
print(f"                 {CellNum:<10s} (C)")
print()
print(f" Site #:{SiteNum:>3d}            Member type: {MemTypeDsp:>9s}")

print()
print(f" Alternate members:          {AltMem:>2d}")
print(f"Weekly site cleaning:        {SiteCleanDsp:>3} ")
print(f"Video surveillance:           {VidSurDsp:>3}")
print()

TotalSiteChargeDsp = "${:,.2f}" .format(TotalSiteCharge)
print(f"Site Charge:       {TotalSiteChargeDsp:>9s}")

ExtChargeDsp = "${:,.2f}" .format(ExtCharge)
print(f"Extra Charges:        {ExtChargeDsp:>6s}")
print(f"                            ------------")
print()

SubTotDsp = "${:,.2f}" .format(SubTot)
print(f"Subtotal:     {SubTotDsp:>6s}")

SalesTaxDsp = "${:,.2f}" .format(SalesTax)
print(f"Sales Tax (HST):      {SalesTaxDsp:>6s}")
print(f"                          ------------")
print()

MonthChargeDsp = "${:,.2f}" .format(MonthCharge)
print(f"Total Monthly Charges:       {MonthChargeDsp:>6s}")

MonthDueDsp = "${:,.2f}" .format(MonthDues)
print(f"Monthly dues:     {MonthDueDsp:>6s}")
print(f"                        ------------")
print()

TotMonFeeDsp = "${:,.2f}" .format(TotMonFee)
print(f"Total monthly fees:     {TotMonFeeDsp:>6s}")

YearlyFeeDsp = "${:,.2f}" .format(YearlyFee)
print(f"Total yearly fees:    {YearlyFeeDsp:>9s}")
print()

MonthPayDsp = "${:,.2f}" .format(MonthPay)
print(f"Monthly payment:     {MonthPayDsp:>6s}")
print()
print(f"-----------------------------------------------")
print()
print(f"Issued: 2023-05-26  ")
print(f"HST Reg No: 549-33-5849-4720-9885")
print()

CancelFeeDsp = "${:,.2f}" . format(CancelFee)
print(f"Cancellation fee:     {CancelFeeDsp:>6s}")
print()


















