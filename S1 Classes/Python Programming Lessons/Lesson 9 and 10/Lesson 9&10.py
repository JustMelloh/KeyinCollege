''' 
age = int(input("Enter a persons age: "))

 if age >= 19:
    print("You are eligible to vote")

 else:
  print("You are not eligible to vote") # Comparisons operators can be >, <, >=, <=,!=, etc


hourlyPayRate = float(input("Enter the hourly pay rate:"))
hoursWorked = int(input("Enter the number of hours worked:"))

# Calculate the gross pay

if hoursWorked <= 40:
    grossPay = hourlyPayRate * hoursWorked
else:
    regPay = 40 * hourlyPayRate
    payOT = (hourlyPayRate * 1.5) * (hoursWorked - 40)
    grossPay = regPay + payOT

print(f"The gross pay is ${grossPay:.2f}")


marStatus = input("Enter your marital status (S, M, W or O): ").upper()

if marStatus == "S":
    print("You are a virgin")

elif marStatus == "M":
    print("You are whipped af.")

elif marStatus == "W":
    print("You ate your husband.")

elif marStatus == "O":
    print("Its complicated.")


balDue = float(input("Enter the balance due:"))
credLim = float(input("Enter the credit limit:"))

if balDue <= credLim:
    payDue = (balDue * .10)

else:
    payDue = (balDue *.10) + (balDue - credLim)

print(f"The payment due is ${payDue:.2f}")

'''

first = int(input("Enter the first number:"))
second = int(input("Enter the second number:"))

sum = first + second
diff = first - second
prod = first * second

if second !=0:
    quot = first / second
else:
    message = "cannot divide by 0"

if first % 2 == 0:
    firstEO = "Even"
else:
    firstEO = "Odd"

if second % 2 == 0:
    secondEO = "Even"
else:
    secondEO = "Odd"


print(firstEO)
print(secondEO)
print(sum)
print(diff)
print(prod)

if second != 0:
    print(quot)
else:
    print("cannot divide by 0")
