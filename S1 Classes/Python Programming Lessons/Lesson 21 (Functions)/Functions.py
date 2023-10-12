# Comment like a pro - Program description, Author and Date.
# Import any required libraries
import datetime
import math
import random
# Define program constants.
ALL_CAPS_RATE = .30
# Define a required functions.
def CelcToFahr():
    # Function that convert a temperature from celsius to Farhenheit.
    print()
    CelcTemp = float(input("Enter a temperature in Celsius: "))
    FahrTemp = 9 / 5 * CelcTemp + 32
    CelcTempDsp = "{:.1f}".format(CelcTemp)
    FahrTempDsp = "{:.1f}".format(FahrTemp)
    print(f"A celsius temperature of {CelcTempDsp} is {FahrTempDsp} in Fahrenheit.")
    print()
    Wait = input("Press any key ...")
    print()

def CalcTHR():
    # This calculates and returns the Training heart rate of a person.
    age = int(input("Enter age"))
    rhr = int(input("Enter the persons resting heart rate: "))

    firstStep = (220 - age)
    secondStep = (rhr - firstStep)
    thr = (secondStep * .60) + rhr

    print(f"The training heart rate is {thr}")

    print()
    Wait = input("Press any key ...")
    print()

def CalcDaysXMas():
    pass

def CalcInvAge():
    # Calculate the age and status off an invoice.

    compName = input("Enter the company name: ")
    invDate = input("Enter the invoice date (YYYY-MM-DD): ")
    invDate = datetime.datetime.strptime(invDate, "%Y-%m-%d")
    invAmt = float(input("enter the invoice amount: "))

    curDate = datetime.datetime.now()

    invAge = (curDate - invDate).days
    if invAge <= 30:
        status = "OK"
    elif invAge >= 31 and invAge <= 60:
        status = "Better think of paying."
    else:
        status = "This one could be in trouble."

    print(f"Invoice age: {invAge}")
    print(f"Invoice Status: {status}")

    print()
    Wait = input("Press any key to continue...")
    print()

def MoGuessGame():
    # Play a guessing game for numbers between 1 and 100.
    while True:
        number = random.randint(1, 101)
        
        numGuess = 0

        while True:

            userNum = int(input("Enter your guess between 1-100: "))
            numGuess += 1
            if userNum < number:
                print("Oops, you chose a number that's lower than the answer.")
            elif userNum > number:
                print("Oops, you chose a number that is greater than the answer.")
            else:
                print("Awesome! You got it correct!")
                print(f"It took you {numGuess} guesses to get the answer correct.")
                break
        
        choice = input("Would you like to play again? (Y/N): ").upper()
        if choice == "N":
            break
    
    print()
    Wait = input("Press the enter key to continue...")
    print()



# Main program.
while True:
    print()
    print("Mo\'s quick problems - Main Menu")
    print()
    print("1. Convert Celsius to Fahrenheit.")
    print("2. Determine Training Heart Rate.")
    print("3. How many days to Christmas?")
    print("4. How old is an invoice?")
    print("5. Play my guessing game.")
    print("6. Quit")
    print()
    while True:
        try:
            Choice = int(input("   Enter choice (1-6): "))
        except:
            print("Error - choice is not a valid entry.")
        else:
            if Choice < 1 or Choice > 6:
                print("Error - Choice must be between 1 and 6.")
            else:
                break
    if Choice == 1:
        CelcToFahr()
    elif Choice == 2:
        CalcTHR()
    elif Choice == 3:
        CalcDaysXMas()
    elif Choice == 4:
        CalcInvAge()
    elif Choice == 5:
        MoGuessGame()
    else:
        break
# Housekeeping
print()
print("Thanks for using Mo's Quick Problems.")
print("Come and visit again soon.")