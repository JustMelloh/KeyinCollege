'''
for i in range(1, 11):
    print(i)


i = 1
while i <= 10:
    print(i)

    i = (i + 1)


for i in range(1, 11):
    square = (i ** 2)
    cube = (i ** 3)
    print(i, square, cube)

'''

while True:

    print("       Temperatre Conversion Chart")
    
    print("     Celcius Farenheit Kelvin          Message        ") 
    print("-"*70)

    for celcTemp in range(-10, 11):

        kelTemp = celcTemp + 273.15
        farenForm =  9 / 5 * celcTemp + 32

        message = ""
        if celcTemp == -90:
            message = "Lowest Recorded Temperature."

        elif celcTemp == 0:
            message = "Freezing point of water."

        elif celcTemp == 20:
            message = "Average Room Temperature."

        elif celcTemp == 100:
            message = "Boiling point of water."
    
    
        print(f"     {f'{celcTemp}':>4}     {f'{farenForm:,.1f}':>5s}     {f'{kelTemp:,.1f}':>5}  {message:<27}")

    print("-"*70)

    print()

    conTinue = input("Do you want to continue? (y/n): ").upper()

    if conTinue == "N":
        break

print()
print("Thank you for using the temperature conversion program.")
print("                  Have a great day!")