#!/usr/bin/env python
# This calculates the overall BTUs needed to heat a building.
# Document what the values are, for ex, where does 1.074 in q5 come frome? ***
import time
print("\nHi! This is a little program to calculate the overall BTUs needed to heat a structure.\n")

print('You will need to enter a few different values.\n')
time.sleep(2)
rValue = float(input('Input the total R-value of the walls: '))

wallArea = float(input("Value of the wall area: "))
windowArea = float(input("Window area: "))
vertArea = wallArea - windowArea
outTemp = float(input("Outside air temperature: "))
targetTemp = float(input("Target indoor temperature: "))
dTemp = abs(outTemp - targetTemp)
q1 = vertArea*dTemp/rValue
print('\nThe first section has a BTU value of ' + str(q1))

print("\n********* BTU Success! Moving on. ****************\n")

# This was changed to take multiple u and area values, instead of just one
# There needs to be a u1, u2, u3, u4, etc
# Then take the values and add them (the sum of the u1-5, then that's the value of q2)
# OLD - first change this to accept user input to list the different uValues and respective areas for the equation = q = uValue*areaWinow*dTemp, then all the q's would be added to calculate q2.
helper = str(input('How many windows are in the home?: '))
print('\nBecause you said there are * ' + helper + ' * windows in the home, you should enter * ' + helper + ' * items \nfor the uValues and area for the windows.')
time.sleep(3)
print('\nFor example, if there is a double-pane window with a reflective coating,\nyou will need to find the uValue and area, for that window, as well as for each type of window.')
time.sleep(5)
# The following was done, then found out that the equation was incorrect, but keeping it just in case
# uValues_List = [int(i) for i in uValues_All.split()]
# areaInd_Wind = [int(k) for k in areaInd_windows.split()]
print('\nYou will need to do some searching for the following values depending \non the type of windows you have.')
# input('Press "enter" to continue')
time.sleep(3)
uValues = input('\n*** When ready, enter the uValues for ' + str(helper) + ' different windows, separated by a space: ')
areaInd_windows = input('Enter the area values for ' + str(helper) + ' different windows, separated by a space: ')

valuesUValues = map(float, uValues.split())
# print('Here are the values you entered for uValue:' + str(valuesUValues))
area_windows = map(float, areaInd_windows.split())
# print('Here are the values you entered for area:' + str(area_windows))
# This multiplies the first value in the first list with the first value in the second list
# Then creates a new list that will be used to multiply each value with the difference in temp, dTemp
mult = [a*b for a, b in zip(valuesUValues, area_windows)]
print('The first values have been multiplied by the respective second values')
print(mult)
for (i, v) in enumerate(mult):
    mult[i] = v*dTemp
print('Here, the previously multiplied values are multiplied by deltaTemp')
print(mult)
q2 = sum(mult)
# sumU = sum(valuesUValues)
# sumA = sum(area_windows)
# sumAreaInd_Wind = sum(areaInd_Wind)
# print('The numbers: ' + str(valuesUValues) + ' have a sum of: ' + str(sumU))
# print('The numbers: ' + str(area_windows) + ' have a sum of: ' + str(sumA))
# q2 = (sumU*dTemp)+(sumA*dTemp)
# uValWindow = float(input("Give me that uValue of the windows: "))
# q2 = uValWindow*windowArea*dTemp
print('\nThe second section has a BTU value of ' + str(q2))
print("\n********* q2 Success! Moving on. ****************\n")

# get total area of each window for each side of the house
print('For the following values, to get the shading coefficient, you can go to:\nhttp://www.ced.berkeley.edu/~crisc/oldstuff_Aarch140_11/Readings/Files/appendix.pdf')
shadeCoEf = float(input("What is the shading coefficient? (Hint: This number ranges from 0 to 1.) \nEnter 1 if shading is a factor: "))
print("\nFor the following calcs, you need to go to \nwww.portal.hud.gov/hubportal/documents/huddoc?id=doc_10603.pdf")
print("Find table 3.25 on page 91 to get the values for the next section.\n")
# windowsEW = int(input("How many windows are facing the east and west? "))
# windowsS = int(input("How many windows are facing the south? "))
# windowsN = int(input("How many windows are facing the north? "))
# the area needs to be multiplied by the number of windows - this is more precise
aWindowsE = float(input("What is the total area of all the windows facing the east: "))
aWindowsW = float(input("What is the total area of all the windows facing the west: "))
aWindowsS = float(input("What is the total area of all the windows facing the south: "))
aWindowsN = float(input("What is the total area of all the windows facing the north: "))

solCoolE = float(input("\nWhat is the solar cooling load for east-facing windows: "))
solCoolW = float(input("Solar cooling load for the west-facing windows: "))
solCoolN = float(input("Shading coefficient for north-facing windows: "))
solCoolS = float(input("Finally, how about the south-facing windows: "))
solCoolLoad = float(aWindowsE*solCoolE) + float(aWindowsW*solCoolW) + float(aWindowsS*solCoolS) + float(aWindowsN*solCoolN)
q3 = shadeCoEf*solCoolLoad
print('\nThe third section has a BTU value of ' + str(q3))

print("\n********* q3 Success! Moving on. ****************\n")

uValue = float(input("What is the uValue of the roof? "))
aRoof = float(input("What is the area of the roof? "))
uCeiling = float(input("What is the uValue of the ceiling? "))
aCeiling = float(input("What is the area of the ceiling? "))
atticTemp = float(uValue*aRoof*outTemp) + float(uCeiling*aCeiling*targetTemp)
atticTempP2 = float(uValue*aRoof) + float(uCeiling*aCeiling)
atticTotal = atticTemp / atticTempP2

print("\nHere's the temperature of the attic: " + str(atticTotal))

condInsideArea = float(input("\nWhat is the area of the indoor, conditioned space? "))
nextTemp = targetTemp - atticTotal
q4 = abs(uCeiling*condInsideArea*nextTemp)
print('\nThe fourth section has a BTU value of ' + str(q4))

print("\n********* q4 Success! Moving on. ****************\n")

# May need to change
cFM = float(input("What is the CFM reading at 50 pascals?: "))
nFactor = float(input("\nWhat is the N Factor? \nDo a search to find your specfic N Factor and enter it here: "))
cFMNatural = cFM/nFactor
q5 = 1.074*cFMNatural*dTemp
print('\nThe fifth section has a BTU value of ' + str(q5))

print("\n********* q5 Success! Moving on. ****************\n")

wattage = float(input("What is the wattage from the house? "))
q6 = 3.42*wattage*condInsideArea
print('\nThe sixth section has a BTU value of ' + str(q6))

print("\n********* q6 Success! Almost there! ****************\n")

numPeeps = int(input("How many people live in the home? "))
q7 = numPeeps*200
print('\nThe seventh section has a BTU value of ' + str(q7))

print("\n********* q7 Success! We're done!  Yesssss! ****************\n")

grandTotalBTU = q1+q2+q3+q4+q5+q6+q7
print("The total BTUs needed to heat this particular structure is...")
print("You ready?!\n")
time.sleep(1)
print("It's " + str(grandTotalBTU) + " BTUs per hour.\n")
