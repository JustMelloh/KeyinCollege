################################################################
# Calculate a new insurance policy insurance for customers,
# containing next policy number, basic premium, discount for additional cars, cost of extra liability, glass coverage, cost for a loaner car.
# Written by Austin Reid
# Written on July 18, 2023
################################################################

# Import libraries
import Validations
import Functions
from datetime import datetime as dt, timedelta
from tqdm import tqdm
import time

# Define default values

currDate = dt.now()

f = open('OSICDef.dat', 'r')
POLICY_NUM = int(f.readline())
BASIC_RATE = float(f.readline())
ADD_DISCOUNT_RATE = float(f.readline())
LIA_PER_CAR_RATE = float(f.readline())
GLASS_COV_RATE = float(f.readline())
LOANER_CAR = float(f.readline())
HST_RATE = float(f.readline())
PROCESS_FEE_RATE = float(f.readline())

f.close()

print(POLICY_NUM, BASIC_RATE, ADD_DISCOUNT_RATE, LIA_PER_CAR_RATE, GLASS_COV_RATE, LOANER_CAR, HST_RATE,PROCESS_FEE_RATE)
# Main Program

# User inputs

while True: 

    custName = input("Please enter first name: ").title()
    custLast = input("Please enter last name: ").title()
    streetAdd = input("Please enter address: ").title()
    City = input("Please enter city: ").title()
    while True:
        Prov = input("Please enter province (LL): ").upper()
        Error = Validations.provVA(Prov)
        if not Error:
            break
    

    while True:
        postCode = input("Please enter postal code (L1L1L1): ").upper()
        Error = Validations.postalVa(postCode)
        if not Error:
            break
        
    while True:
        custPhone = input("Please enter phone number (LLLLLLLLLL): ")
        Error = Validations.phoneVa(custPhone)
        if not Error:
            break

    while True:
        try:
            numCars = int(input("Please enter the number of cars to be insured: "))
        except:
            print("Error: Must inset an integer.")
            continue
        Error = Validations.carVa(numCars)
        if not Error:
            break
    
    while True:
        Liability = input("Extra liability for up to $1,000,000 (Y/N): ").upper()
        Error = Validations.liabilityVa(Liability)
        if not Error:
            break
    
    while True:
        glassCov = input("Optional glass coverage? (Y/N): ").upper()
        Error = Validations.glassCovVa(glassCov)
        if not Error:
            break
    
    while True:
        optLoaner = input("Optional loaner car? (Y/N): )").upper()
        Error = Validations.loanerVa(optLoaner)
        if not Error:
            break

    while True:
        typePay = input("How are they paying? (Full/Monthly): ").title()
        Error = Validations.typePayVa(typePay)
        if not  Error:
            break

# Calculations
    Functions.Calc_insurance(numCars)
    insPremium = Functions.Calc_insurance(numCars)

    Functions.extra_Liability(numCars,Liability)
    totalLiability = Functions.extra_Liability(numCars, Liability)

    Functions.glassCov(numCars,glassCov)
    totalGlassCov = Functions.glassCov(numCars, glassCov)

    Functions.loanCar(numCars,optLoaner)
    loanCarTotal = Functions.loanCar(numCars, optLoaner)

    
    totalExtraCost = totalLiability + totalGlassCov + loanCarTotal
    totalInsurancePremium = insPremium + totalExtraCost
    totalHST = totalInsurancePremium * HST_RATE
    totalCost = totalHST + totalInsurancePremium
    monthlyPay = Functions.insurancePay(totalCost, typePay)
    

    # Add 30 days to the current date then set it to '1' to indicate first day of month.
    invDate = currDate
    nextMonthDate = currDate + timedelta(days=30)
    nextPaymentDate = nextMonthDate.replace(day=1)

    # Return formatted phone number.
    FormPhone = Functions.phoneFormat(custPhone)

    print(f" "*20, "|One Stop Insurance Company|")
    print()
    print(f" "*20, "|--------------------------|")
    print()
    print(f" "*10, f"|Policy #:                                 {POLICY_NUM:<4d}")
    print(f" "*10, f"|Customer Name:                     {custName} {custLast}")

    print()
    print(f" "*10, f"|Address:              {streetAdd:<8s}, {City:<8s}")
    print(f" "*10, f"                                     {postCode:<6s}, {Prov:<2s}")
    print()
    print(f" "*10, f"|Phone Number:                   {FormPhone:<15s}")
    print(f" "*10, "-"*46)
    print()
    print(" "*23, f"Payment Type: {typePay:<7s}")
    print(f" "*23, f"Ex. Liability: {Liability}")
    print(f" "*23, f"Glass Coverage: {glassCov}")
    print(f" "*23, f"Car Loaner: {optLoaner}")
    print()
    print(f" "*10, "-"*46)
    print(f" "*10, f"Number of Cars:                              {numCars}")
    print(f" "*10, f"Insurance Premium:                   {f'${insPremium:,.2f}':>8s}")
    print(f" "*10, f"Ex. Cost:                            {f'${totalExtraCost:,.2f}':>9s}")
    print(f" "*10, f"Sub-total:                           {f'${totalInsurancePremium:,.2f}':>8s}")
    print(f" "*10, f"HST:                                 {f'${totalHST:,.2f}':>9s}")
    print(f" "*10, f"Total:                               {f'${totalCost:,.2f}':>8s}")
    print(f" "*10, "-"*46)
    print(f" "*10, f"Monthly Payment:                     {f'${monthlyPay:,.2f}':<8s}")
    print(f" "*10, f"Next Pay Date:                      {nextPaymentDate.strftime('%Y-%m-%d')}")
    print(f" "*10, f"Invoice Date:                       {invDate.strftime('%Y-%m-%d')}")
    print()

    total_iterations = 100
    for i in tqdm(range(total_iterations), desc="Policy Information process being processed and saved.", ncols=100):
    # Simulate some work being done
        time.sleep(0.1)

    print("Save completed.")




    # House Keeping Code
    POLICY_NUM += 1

    # Add files for future reference.
    f = open('Policies.dat', 'a')
    f.write(f"{POLICY_NUM}, ")
    f.write(f"{custName}, ")
    f.write(f"{custLast}, ")
    f.write(f"{streetAdd}, ")
    f.write(f"{City}, ")
    f.write(f"{postCode}, ")
    f.write(f"{Prov}, ")
    f.write(f"{FormPhone}, ")
    f.write(f"{typePay}, ")
    f.write(f"{Liability}, ")
    f.write(f"{glassCov}, ")
    f.write(f"{optLoaner}, ")
    f.write(f"{totalInsurancePremium}, ")
    f.write(f"{invDate}\n")
    f.close()

    # Write values back to default file

    f = open('OSICDef.dat', 'w')
    f.write(f"{POLICY_NUM}\n")
    f.write(f"{BASIC_RATE}\n")
    f.write(f"{ADD_DISCOUNT_RATE}\n")
    f.write(f"{LIA_PER_CAR_RATE}\n")
    f.write(f"{GLASS_COV_RATE}\n")
    f.write(f"{LOANER_CAR}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{PROCESS_FEE_RATE}\n")
    f.close()