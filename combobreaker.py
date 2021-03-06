#! /usr/bin/python
# Simple script based off of 
# Samy Kamkar's work on cracking Master combo lock

import math

firstLock = int(input("1st locked position: "))
secondLock = int(input("2nd locked position: "))
resistLoc = float(input("Resistant location:  "))
print("\n")

firstDigit = math.floor(resistLoc + 5.76)

possible3rd = set([])
for i in range(0, 40, 10):
    possible3rd.add(firstLock + i)
    possible3rd.add(secondLock + i)

modFour = set([])
possible2nd = []
for x in range(0, 42):
    if (x % 4 == firstDigit % 4):
        modFour.add(x)
        if (x-2 >= 0):
            possible2nd.append(x-2)

possible3rd = possible3rd.intersection(modFour)
print("--------------------------------------------")
print("1st Digit:", firstDigit)
print("2nd Digits:", possible2nd)
print("3rd Digits:", possible3rd)
thirdDigit = int(input("Which 3rd digit has wider gap? "))
print("--------------------------------------------\n\n")

try:
    possible2nd.remove(thirdDigit - 2)
    possible2nd.remove(thirdDigit + 2)
except ValueError:
    if (thirdDigit - 2 < 0):
        if (possible2nd.count(0) == 1):
            possible2nd.remove(0)
        possible2nd.remove(thirdDigit + 2)
    elif (thirdDigit + 2 >= 39):
        possible2nd.remove(thirdDigit + 2 - 40)
        if (possible2nd.count(0) == 1):
            possible2nd.remove(0)

print("*****************<RESULT>******************")
print("1st Digit :", firstDigit)
print("2nd Digits:", possible2nd)
print("3rd Digit :", thirdDigit)
print("<=========================================>")