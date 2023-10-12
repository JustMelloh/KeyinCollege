# Comment like a pro.
import datetime
# Import included libraries.

# Define constants / default values
f = open('Defaults.dat', 'r')
NEXT_CONF_NUM = int(f.readline())
HST_RATE = float(f.readline())
COST_SMALL = float(f.readline())
COST_MED = float(f.readline())
COST_LARGE = float(f.readline())
COST_BREAKFAST = float(f.readline())
COST_LUNCH = float(f.readline())
COST_SUPPER = float(f.readline())
COST_COFFEE = float(f.readline())

f.close()

print(NEXT_CONF_NUM)
print(HST_RATE)
print(COST_SMALL)
print(COST_MED)
print(COST_LARGE)
print(COST_BREAKFAST)
print(COST_LUNCH)
print(COST_SUPPER)
print(COST_COFFEE)

# Define required functions

# Main Program

while True:
    ClientName = input("Enter the client name (END to quit): ").title()
    if ClientName == "End":
        break
    confTitle = input("Enter the conference title: ").title()
    startDate = input("Enter the start date (YYYY/MM/DD): ")
    startDate = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    numAtt = int(input("Enter the number of attendees: "))
    numDays = int(input("Enter the number of days: "))
    numBreakfast = int(input("Enter the number of breakfasts: "))
    numLunch = int(input("Enter the number of lunches: "))
    numSupper = int(input("Enter the number of suppers: "))
    numCoffee = int(input("Enter the number of coffee breaks: "))

    if numAtt <= 30:
        costRoom = numDays * COST_SMALL

    elif numAtt <= 100:
        costRoom = numDays * COST_MED
    else:
        costRoom = numDays * COST_LARGE

    costBreakfast = 0
    if numBreakfast > 0:
        costBreak = numAtt * COST_BREAKFAST

    costLunch = 0
    if numLunch > 0:
        costLunch = numAtt * COST_LUNCH

    costSupper = 0
    if costSupper > 0:
        costSupper = numAtt * COST_SUPPER

    costCoffee = 0
    if costSupper > 0:
        costCoffee = numAtt * COST_COFFEE

    confCost = costRoom + costBreak + costSupper + costCoffee
    HST = confCost * HST_RATE
    confTotal = confCost + HST 
    costPerAtt = confTotal / numAtt

    print(costRoom)
    print(costBreak)
    print(costLunch)
    print(costSupper)
    print(confCost)
    print(HST)
    print(confTotal)
    print(costPerAtt)
    

    print()
    print("Saving conference data...")

    # Add a progress bar or reasonable option here.

    # Write the values to a file for future reference.
    #
    f = open('Stuff.dat', 'a')
    f.write(f"{NEXT_CONF_NUM}, ")
    f.write(f"{ClientName}, ")
    f.write(f"{confTitle}")
    f.write(f"{numAtt}, ")
    f.write(f"{confTotal}, ")
    print("Conference data successfully saved...")

    # Update and default values.
    NEXT_CONF_NUM += 1



# Housekeeping


    # Write the current calues back to the dault file. Note the use of "w" to overwrite
    # and the use of \n breaks the lines.
f = open('Defaults.dat', 'w')
f.write(f"{NEXT_CONF_NUM}\n")
f.write(f"{HST_RATE}\n")
f.write(f"{COST_SMALL}\n")
f.write(f"{COST_MED}\n")
f.write(f"{COST_LARGE}\n")
f.write(f"{COST_BREAKFAST}\n")
f.write(f"{COST_LUNCH}\n")
f.write(f"{COST_SUPPER}\n")
f.write(f"{COST_COFFEE}\n")
f.close()


# Housekeeping