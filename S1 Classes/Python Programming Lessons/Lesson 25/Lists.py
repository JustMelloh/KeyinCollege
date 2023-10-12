
'''
toDoLst = [] # This will create an empty list.
toDoLst2 = ["Buy this Tea", "Study hard", "Buy da wife some flowers","Write a Python Program"]
otherLST = [1, 3, 5, 46, 143, 6, 8]

print(toDoLst2)

jobNum = 1
for Job in toDoLst2:
    print(f" {jobNum}. {Job}")
    jobNum += 1
print()


newItem = input("Enter new job for the ToDo list: ")
toDoLst2.append(newItem)

jobNum = 1
for Job in toDoLst2:
    print(f" {jobNum}. {Job}")
    jobNum += 1
print()

delItem = int(input("Enter the list item to delete: "))
toDoLst2.__delitem__(delItem-1)

jobNum = 1
for Job in toDoLst2:
    print(f" {jobNum}. {Job}")
    jobNum += 1
print()


numberLst = []
while True:
    number = int(input("Enter a number (-1 to end): "))

    if number == -1:
        break


    numberLst.append(number)

print(numberLst)
'''
provLst = ["NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT"]
while True:
    prov = input("Enter the province (LL): ").upper()

    if prov == "":
        print("Error - Province cannot be blank")
    if len(prov) != 2:
        print("Error - Use the abbreviation for the province.")
    elif prov not in provLst:
        print("Error - Not a valid province.")
    else: 
        break