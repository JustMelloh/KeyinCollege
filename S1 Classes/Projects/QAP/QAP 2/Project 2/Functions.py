# Functions

# print()

# input()

# int()

# float()

# Adate.strptime()

# Adate.strftime()




# Comment like a pro.





# Import any required libraries

#import datetime

#import math




# Define program constants.

ALL_CAPS_RATE = 0.30




# Define any required functions.




def celcToFahr():

    # Function that will convert a temperature from Celcius to Fahrenheit.




    celcTemp = float(input("Enter a temperature in Celcius: "))

    fahrTemp = 9 / 5 * (celcTemp + 32)




    print(f" A Celsius temperature of {celcTemp} is {fahrTemp} in Fahrenheit")




def calcTHR():

    pass





def calcDaysXmas():

    pass





def calcInvoiceAge():

    pass





def playGuessingGame():

    pass





# Main Program.

while True:




    print()

    print("Mo's quick problems - Main Menu")

    print()

    print("1. Convert Celsius to Fahrenheit.")

    print("2. Determine Training Heart Rate.")

    print("3. How many days to Christmas.")

    print("4. How old is an invoice?")

    print("5. Play my guessing game.")

    print("6. Quit.")

    print()




    while True:

        try:

            userChoice = int(input("     Enter choice (1-6): "))

        except:

            print("Error: Choice is not a valid entry.")

        else:

            if userChoice < 1 or userChoice > 6:

                print("Error: Choice must be between 1 and 6.")

            else:

                break




    if userChoice == 1:

        celcToFahr()

    elif userChoice == 2:

        calcTHR()

    elif userChoice == 3:

        calcDaysXmas()

    elif userChoice == 4:

        calcInvoiceAge()

    elif userChoice == 5:

        playGuessingGame()

    else:

        break




print()

print("Thanks for using Mo's Quick Problems.")

print("Come and visit again soon.")