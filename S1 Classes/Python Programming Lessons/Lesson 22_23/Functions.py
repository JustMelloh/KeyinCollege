# Comment like a pro.

# Import required libraries.

# Define program constants.

# Here comes the functions.

def findIdealAge():
    # Determine the ideal age of a spouse according to Plato.

    idealSpouseAge = (age / 2) + 7

    return idealSpouseAge

def findLetterGrade(studGrade):

    if studGrade >= 80:
        letterGrade = "A"
    elif studGrade >= 70 and studGrade <= 79:
        letterGrade = "B"
    elif studGrade >= 60 and studGrade <= 69:
        letterGrade = "C"
    elif 50 <= studGrade <= 59:
        letterGrade = "D"
    else: 
        letterGrade = "F"

    return letterGrade

def findGrossPay(hours, payRate):
    # Determine the gross pay of an employee.

    if hours <= 40:
        grossPay = hours * payRate
    else:
        regPay = 40 * payRate
        OTRate = payRate * 1.5
        OTHours = hours - 40
        OTPay = OTRate * OTHours
        grossPay = regPay + OTPay

    return grossPay


# Main program.

while True:
    myAge = int(input("Enter your age: "))
    idealSpouseAge = findIdealAge()
    print(idealSpouseAge)

    studGrade = float(input("Enter the students grade:"))
    lGrade = findLetterGrade(studGrade)
    print(lGrade)

    empName = input("Enter the employee name: ")
    hoursWorked = float(input("Enter the hours worked: "))
    hourlyPayRate = float(input("Enter the hourly pay rate: "))
    grossPay = findGrossPay(hoursWorked, hourlyPayRate)
    print(empName)
    print(grossPay)
# Housekeeping