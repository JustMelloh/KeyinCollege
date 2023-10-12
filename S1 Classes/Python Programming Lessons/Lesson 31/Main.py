# Comment like a pro

# Import Libraries

import datetime as dt
currDate = dt.datetime.now()


# Define the defaults file and reads the values into variables

f = open('def.dat', 'r')

movieNum = int(f.readline())
HSTRate = float(f.readline())
newRelDays = int(f.readline())
obsWeeks = int(f.readline())
f.close()

print(movieNum)
print(HSTRate)
print(newRelDays)
print(obsWeeks)

# Define required functions

# Main program
while True:
    movieName = input("Enter the movie name (Type END to quit): ").title()
    if movieName == "End":
        break
    movieType = input("Enter the movie type (D, C , M, H): ").upper()
    movieRating = input("Enter the movie rating (G, P, R): ").upper()
    rentalCost = float(input("Enter the rental cost (1.99 - 8.99): "))

    #Add any calculations.



    # Display the claim receipt on screen.

    print(movieNum)
    print(movieName)
    print(movieType)
    print(movieRating)
    print(rentalCost)


    print()

    #Write the current values
    print("Saving movie data for " + movieName + ", Please wait...")
    f = open("Movies.dat", "a")
    f.write(f"{str(movieNum)}\n")
    f.write(f"{movieName}\n")
    f.write(f"{movieType}\n")
    f.write(f"{movieRating}\n")
    f.write(f"{str(rentalCost)}\n")
    f.close()

    print()
    print("Movie information has been successfully saved.")
    movieNum += 1
    # Write current values back to the default file.

    f = open ('Def.dat', 'w')
    f.write(f"{str(movieNum)}\n")
    f.write(f"{str(HSTRate)}\n")
    f.write(f"{str(newRelDays)}\n")
    f.write(f"{str(obsWeeks)}\n")
    f.close()