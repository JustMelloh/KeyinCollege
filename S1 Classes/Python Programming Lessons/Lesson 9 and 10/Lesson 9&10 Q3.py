#######################################################################
# Program description: Rental company charges rentals based on daily
# and kilometer rental rates.
# Written by: Austin Reid
# Date created: May 16th,2023
########################################################################

#Constants

RENT_PER_DAY = 35.00
COST_PER_KILO = 0.10

#Inputs

rentDays = int("How many days was the car rented?: ")
startOdo = float("What is the starting Odometer?: ")
endOdo = float("What is the ending Odometer?: ")

#Calculations

dailyCharge = rentDays * RENT_PER_DAY
kiloCharge = (endOdo - startOdo) * COST_PER_KILO



