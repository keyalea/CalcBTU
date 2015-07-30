#!/usr/bin/env python
# This calculates the overall BTUs needed to heat a building.
# It uses different calculations to define q-values, representing BTUs

import time

print("\nHi! This is a little program to calculate the overall BTUs needed to heat a structure.\n")
print('You will need to enter a few different values. In this first section,\nwe will calculate the BTU value for heat conducted through the walls.')
time.sleep(2)
rValue = float(input('\nInput the total R-value of the walls: '))

wallArea = float(input("Value of the wall area: "))
windowArea = float(input("Window area: "))
vertArea = wallArea - windowArea
outTemp = float(input("Outside air temperature: "))
targetTemp = float(input("Target indoor temperature: "))
dTemp = abs(outTemp - targetTemp)
q1 = vertArea*dTemp/rValue
#round(q1, 2)
print('\nThe first section has a BTU value of ' + str("%.2f" % q1))

print("\n********* BTU Success! Moving on. ****************\n")

# This was changed to take multiple u and area values 
# Take the product of the u and area values and add them. The sum is the value of q2
# In order to do this I'm getting two lists from the user, then multiplying respective values
# I first tried key: values in a dictionary, but similar values would not be repeated.  Instead, text
#  to guide the user is added.
print('\nThis next section will calculate heat conducted through the windows of the structure.\n')
helper = str(input('How many windows are in the home?: '))
print('\nBecause you said there are * ' + helper + ' * windows in the home, you should enter * ' + helper + ' * items \nfor the uValues and area for the windows.')
time.sleep(3)
print('\nFor example, if there is a double-pane window with a reflective coating,\nyou will need to find the uValue, and the area, for that window,\nas well as for each type of window in the home.')
time.sleep(5)
# uValues_List = [int(i) for i in uValues_All.split()]
# areaInd_Wind = [int(k) for k in areaInd_windows.split()]
print('\nYou may need to do some searching for the following values depending \non the type of windows you have.')
time.sleep(3)
uValues = input('\n*** When ready, enter the uValues for ' + str(helper) + ' different windows, separated by a space: ')
areaInd_windows = input('Enter the area values for ' + str(helper) + ' different windows, separated by a space: ')

valuesUValues = map(float, uValues.split())
area_windows = map(float, areaInd_windows.split())
# This multiplies the first value in the first list with the first value in the second list
#  then creates a new list that will be used to multiply each value with the difference in temp, dTemp
mult = [a*b for a, b in zip(valuesUValues, area_windows)]
time.sleep(2)
print('\nThe first values have been multiplied by the similarly indexed value in the second list')
print(mult)
for (i, v) in enumerate(mult):
    mult[i] = v*dTemp
print('\nThe previous products were multiplied by deltaTemp, then summed to get the second BTU value.')
q2 = sum(mult)
time.sleep(1)
print('\nThe second section has a BTU value of ' + str("%.2f" % q2))
print("\n********* q2 Success! Moving on. ****************\n")

# This calculates the BTUs coming through windows
print('The next section calculates the solar radiant heat gain from the windows.\n')
print('For the following values, to get the shading coefficient, you can go to:\nhttp://www.ced.berkeley.edu/~crisc/oldstuff_Aarch140_11/Readings/Files/appendix.pdf')
shadeCoEf = float(input("\nWhat is the shading coefficient? (Hint: This number ranges from 0 to 1.) \nEnter 1 if shading is a factor: "))
print("\nFor the following calcs, you need to go to \nwww.portal.hud.gov/hubportal/documents/huddoc?id=doc_10603.pdf")
print("Find table 3.25 on page 91 to get the values for the next section.\n")
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
print('\nThe third section has a BTU value of ' + str("%.2f" % q3))

print("\n********* q3 Success! Moving on. ****************\n")

print('\nThis next section calculates the heat gain from the attic space.\n')
uValue = float(input("What is the uValue of the roof? "))
aRoof = float(input("What is the area of the roof? "))
uCeiling = float(input("What is the uValue of the ceiling? "))
aCeiling = float(input("What is the area of the ceiling? "))
atticTemp = float(uValue*aRoof*outTemp) + float(uCeiling*aCeiling*targetTemp)
atticTempP2 = float(uValue*aRoof) + float(uCeiling*aCeiling)
atticTotal = atticTemp / atticTempP2

print("\nHere's the temperature of the attic: " + str(atticTotal) + " (Reality check)")

condInsideArea = float(input("\nWhat is the area of the indoor, conditioned space? "))
nextTemp = targetTemp - atticTotal
q4 = abs(uCeiling*condInsideArea*nextTemp)
print('\nThe fourth section has a BTU value of ' + str("%.2f" % q4))

print("\n********* q4 Success! Moving on. ****************\n")

print('\nThis section calculates the sensible (dry) heat gain in the home.\n') 
cFM = float(input("What is the CFM reading at 50 pascals?: "))
nFactor = float(input("\nWhat is the N Factor? \nDo a search to find your specfic N Factor and enter it here: "))
cFMNatural = cFM/nFactor
q5 = 1.074*cFMNatural*dTemp
print('\nThe fifth section has a BTU value of ' + str("%.2f" % q5))

print("\n********* q5 Success! Moving on. ****************\n")

print('This next section calculates the heat gain from electrical appliances and lights.\n')
wattage = float(input("What is the wattage from the house? "))
q6 = 3.42*wattage*condInsideArea
print('\nThe sixth section has a BTU value of ' + str("%.2f" % q6))

print("\n********* q6 Success! Almost there! ****************\n")

print('This next section calculates the heat gain from people in the home.\n')
numPeeps = int(input("How many people live in the home? "))
q7 = numPeeps*200
print('\nThe seventh section has a BTU value of ' + str("%.2f" % q7))

print("\n********* q7 Success! We're done!  Yesssss! ****************\n")

grandTotalBTU = q1+q2+q3+q4+q5+q6+q7
print("The total BTUs needed to heat this particular structure is...")
print("You ready?!\n")
time.sleep(1)
print("It's " + str("%.2f" % grandTotalBTU) + " BTUs per hour.\n")
