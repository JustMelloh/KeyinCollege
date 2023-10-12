# Input marital status
'''
marStat = input("Enter the marital status: (S, M, W, or D): ").upper()
age = int(input("Enter your age: "))


if marStat == "M":
    marDate = input("Enter the date of marriage: (YYYY/MM/DD): ")
    print("You were married on: ", marDate)

if marStat == "S":
    print("Single.")

elif marStat == "M":
    print("Married.")

elif marStat == "D":
    if age > 40:
        print("Better get into a relationship.")
        print("Divorced af.")

else:
    if age > 40:
        print("Better get into a relationship.")
    print("Widowed.")


studID = input("Enter the student ID: ")
studGrade = int(input("Enter the grade: "))

if studGrade >= 90:
    letterGrade = "A"
elif 80 <= studGrade >= 89:
    letterGrade = "B"
elif 70 <= studGrade >= 79:
    letterGrade = "C"
elif 60 <= studGrade >= 69:
    letterGrade = "D"
else:
    studGrade < 60
    letterGrade = "F"

print("You received a: ", letterGrade)
'''
'''
balDue = float(input("Enter the balance due: "))
credLim = float(input("Enter the credit limit: "))

if balDue < credLim:
    payDue = balDue * .10
    status = "OK"

else:
    payDue = (balDue * .10) + (balDue - credLim)
    status = "OVER"
    if balDue < credLim > 1000.0:
        status += " - CREDIT CHECK"

print(payDue, status)
'''
'''
mortRequest = float(input("Enter the mortgage request: "))

if mortRequest < 25000:
    print(f"The deposit of: {mortRequest} requires 5""%"" of the loan amount.")
elif 25000 < mortRequest < 50000:
    print(f"The deposit of: {mortRequest} requires $1,250 plus 10""%"" of the loan over $25,000.")
else: 
    50000 < mortRequest < 100000
    print(f"The deposit of: {mortRequest} requires $5,000 plus 25""%"" of loan over $50,000")
'''

div = divmod(42,20)

print(div)