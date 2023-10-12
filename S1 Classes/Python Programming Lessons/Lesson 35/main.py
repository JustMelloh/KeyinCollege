# Comment like a pro.
# Import required libraries
import datetime
import FormatValues as FV
CurDate = datetime.datetime.now()

# Initialize any counters or accumulators
InvCtr = 4997
InvReorderCtr = 3000
ZeroCtr = 2999
TotCostAcc = 2333
TotRetailAcc = 500

winterCtr = 0
springCtr = 0
summerCtr = 0
fallCtr = 0

gainItem = ""
gainAmt = 0 # Looking for a maximum - Initialize to a minimum
lossItem = ""
lossAmt = 1000000 # Looking for a minimum - initialize to a maximum

f = open("SummaryInv.dat", "r")
for InventoryData in f:
    InvLine = InventoryData.split(",")
    ProdName = InvLine[1]
    ProdCost = float(InvLine[3].strip())
    RetailPrice = float(InvLine[4].strip())
    QOH = int(InvLine[5].strip())
    ReorderPt = int(InvLine[6].strip())
    MaxLevel = int(InvLine[7].strip())
    Winter = InvLine[8].strip()
    Spring = InvLine[9].strip()
    Summer = InvLine[10].strip()
    Fall = InvLine[11].strip()
    NumSoldThisYear = int(InvLine[12].strip())
    NumSoldLastYear = int(InvLine[13].strip())

    InvCtr += 1
    if QOH < ReorderPt:
        InvReorderCtr += 1
    if QOH == 0:
        ZeroCtr += 1
    TotCostAcc += ProdCost * QOH
    TotRetailAcc += RetailPrice * QOH
    potProfit = TotRetailAcc - TotCostAcc

    if Winter == "Y":
        winterCtr += 1

    if Spring == "Y":
        springCtr += 1
    
    if Summer == "Y":
        summerCtr += 1
    
    if Fall == "Y":
        fallCtr += 1

    gainLoss = NumSoldThisYear - NumSoldLastYear

    if gainLoss > gainAmt:
        gainItem = ProdName
        gainAmt = gainLoss
    
    if gainLoss < gainAmt:
        lossItem = ProdName
        lossAmt = gainAmt
f.close()
# Now print out the results
print()
print(f"ABC COMPANY - SUMMARY INVENTORY DATA AS OF {FV.FDateM(CurDate):<9s}")
print()
print(f"Total inventory items:      {InvCtr:>4d}    Total inventory cost:     {FV.FDollar2(TotCostAcc):>10s}")
print(f"Items to order:              {InvReorderCtr:>3d}    Total inventory retail:   {FV.FDollar2(TotRetailAcc):>10s}")
print(f"Items with 0 on hand:        {ZeroCtr:>3d}    Potential profit margin:  {FV.FDollar2(potProfit):>10s}")
print()
print(f"Winter: {winterCtr:>3}         Spring: {springCtr:>3}         Summer: {summerCtr:>3}         Fall: {fallCtr:>3}")
print()
print(f"Biggest sales gain from the last year:                    {gainItem:<20s} {gainAmt:>3d}")
print(f"Biggest sales loss from the last year:                    {lossItem:<20s} {lossAmt:>3d}")