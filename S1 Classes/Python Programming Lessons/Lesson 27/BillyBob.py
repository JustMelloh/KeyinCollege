# Comment like a pro
Total = 0
Nums = []
while True:
    Number = int(input("Enter a number (-1 to end): "))
    if Number == -1:
        break
    Nums.append(Number)
    Total += Number

print(Total)
print(Nums)
Nums.sort() # Can I sort in descending order?
print(Nums)


Total2 = sum(Nums)
print(Total2)


# Show the length of the string and numbers inputted.
fName = "Maurice"
stLen = len(fName)
print(stLen)
lstLen = len(Nums)
print(lstLen)

# Find the average
Average = Total2 / len(Nums)
print(Average)

# Find the Max and Min number
maxValue = max(Nums)
print(maxValue)
minValue = min(Nums)
print(minValue)

# Find duplicates
Dupes = []
for i in range(0, maxValue + 1):
    countOcc = Nums.count(i)
    if countOcc >=  2:
        Dupes.append(i)
print(Dupes)