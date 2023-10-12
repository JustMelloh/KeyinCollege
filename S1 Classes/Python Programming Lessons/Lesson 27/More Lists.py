# Comments

# Import Libraries

# Constants

BONUS_RATE = .01

def calcBonus(totalSales):
# Calculate the bonues and the status and return both values as a Tuple.

    Bonus = totalSales * BONUS_RATE
    if totalSales < 5000.00:
        Bonus -= (5000.00 - totalSales) * .17
        Status = "Under"
    elif totalSales > 100000.00:
        Bonus += 500.00
        Status = "Extraordinary"
    else:
        Status = "Normal"

    return Bonus, Status

# Main Program

totalSales = 8000
bonStat = calcBonus(totalSales)

print(bonStat)
print(bonStat[0])
print(bonStat[1])

# To access a list use LstName(index)
# To access a tuple use TupleName[index]

