# Simple script based off of Samy Kamkar's work on cracking combo lock
# Made to be used on a terminal

import math

firstLock = int(input("1st Lock position: "))
secondLock = int(input("2nd Lock position: "))
resistLoc = float(input("Resistance location: "))
print("\n")

firstDigit = math.floor(resistLoc + 5.76)

possible3rd = set([])
for i in range(0, 40, 10):
    possible3rd.add(firstLock + i)
    possible3rd.add(secondLock + i)

modFour = set([])
possible2nd = []
for x in range(0, 40):
    if (x % 4 == firstDigit % 4):
        modFour.add(x)
        if (x-2 > 0):
            possible2nd.append(x-2)

possible3rd = possible3rd.intersection(modFour)
print("-----------------------------------")
print("1st Digit:", firstDigit)
print("2nd Digits:", possible2nd)
print("3rd Digits:", possible3rd)
thirdDigit = int(input("Which 3rd digit has wider gap? "))
print("-----------------------------------\n\n")

try:
    possible2nd.remove(thirdDigit - 2)
    possible2nd.remove(thirdDigit + 2)
except ValueError:
    if (thirdDigit - 2 < 0):
        if (possible2nd.count(0) == 1):
            possible2nd.remove(0)
        possible2nd.remove(thirdDigit + 2)
    elif (thirdDigit + 2 > 39):
        if (possible2nd.count(0) == 1):
            possible2nd.remove(0)
        possible2nd.remove(thirdDigit - 2)

print("*****************<RESULT>******************")
print("1st Digit:", firstDigit)
print("2nd Digits:", possible2nd)
print("3rd Digits:", thirdDigit)
print("<=========================================>")

