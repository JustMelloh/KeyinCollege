# Comment like a pro.
# Import required libraries
import datetime
import FormatValues as FV

CurDate = datetime.datetime.now()

# Before the loop: Print headings, Initialize summary data, Open the file.
print()
print("THE COMPANY NAME")
print(f"OVER LIMIT REPORT AS OF {FV.FDateS(CurDate)}")
print()
print("CUSTOMER      CUSTOMER           PHONE       BALANCE    MINIMUM      DAYS SINCE      CUSTOMER")
print(" NUMBER         NAME             NUMBER        DUE      PAYMENT      LAST PUR         STATUS")
print("="*99)

totCustCtr = 0
TotCustOverCtr = 0
PayDueAcc = 0
minPayAcc = 0
f = open("CustExtra.dat", "r")

for CustDataLine in f:

    # Inside the loop, Read the record, do any calculations, print the detail line.
    CustLine = CustDataLine.split(",")

    # All fields in the list are strings.
    # Numbers and dates must be parsed.
    # Only grab the values from the list that are required.
    CustNum = CustLine[0].strip()
    CustName = CustLine[1].strip()
    PhoneNum = CustLine[2].strip()
    BalDue = float(CustLine[3].strip())
    lastPurDate = float(CustLine[5].strip())
    lastPurDate = datetime.datetime.strptime(lastPurDate, "Y-%m-%d")
    lastPayDate = float(CustLine[7].strip())
    lastPayAmt = float(CustLine[8].strip())
    lastPurDate = datetime.datetime.strptime(lastPayDate, "Y-%m-%d")
    CredLim = float(CustLine[4].strip())
    NextPayDate = CustLine[9].strip()
    NextPayDate = datetime.datetime.strptime(NextPayDate, "%Y-%m-%d")
    
    # For an exception report, place the if statement here.


    # Perform any required calculations here.
    if BalDue <= CredLim:

        MinPay = BalDue * 0.10
    else:
        MinPay = (CredLim * 0.10) + (BalDue - CredLim)

    dayLastPur = (CurDate - lastPurDate).days
    daysLastPay = (CurDate - lastPayDate).days 
    
    if BalDue < CredLim:
        Status = "OK"
    elif BalDue + 200.00 > CredLim:
        Status = "CHECK"
    else: 
        Status = "Over"

    if dayLastPur > 60:
        Status += " - PURCH"
    
    if daysLastPay > 30:
        Status += " - PAY"
    # Print the detail line.
    print(f" {CustNum:>6s} {CustName:<20s} {PhoneNum:<12s}  {FV.FDollar2(CredLim):>9s} {FV.FDollar2(AmountOver):>9s}  {FV.FDateS(NextPayDate):>10s}  {FV.FDollar2(PayDue):>9s}")
    
    # Increment any counters or accumulators.
    TotCustOverCtr += 1
    PayDueAcc += PayDue

# After the loop, close the file, and print the summary data.
f.close()
print("="*85)
print(f"Total customers over limit: {TotCustOverCtr:>3d}                                            {FV.FDollar2(PayDueAcc):>10s}")
print()