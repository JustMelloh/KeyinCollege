# Comment like a pro

INT_RATE = .065

while True:
    loanAmount = float(input("Enter loan amount: "))
    reason = input("Enter the reason for loan: ")

    print()

    print(f"Loan Options for 10 Years on ${f'{loanAmount:,.2f}':<}")
    print()
    print("    Years   Interest  Total Amt  Mon Payment")
    print("    ----------------------------------------")




    for years in range(1,11):
        interest = (loanAmount * INT_RATE * years)
        totAmt = loanAmount + interest
        monthlyPayment = totAmt / (years * 12)

        print(f"      {years:<2d}  {f'${interest:,.2f}':>9s}   {f'${totAmt:,.2f}':>9s}   {f'${monthlyPayment:,.2f}':>9s}")


    print("    ----------------------------------------")
    print()
    Continue = input("Do you want to process another loan? (Y/N): ").upper()   
    
    if Continue == "N":
           break