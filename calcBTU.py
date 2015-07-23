#!/usr/bin/python
# Let's see if I can calculate the overall BTUs needed to heat a building.

print("I'll help you calculate the overall BTUs needed to heat the home.\n")
print('We need a few different values.\n')

#print("Input the R-value of the walls: ")
#rValue=input()

rValue = float(input('Input the total R-value of the walls: '))

# insert check to make sure not empty value - or break out.

print('Cool.  I have the value as: ', rValue)
print("\nYou'll need to supply the following values.")
wallArea = float(input("Value of the wall area: "))
windowArea = float(input("Window area: "))
vertArea = wallArea - windowArea
outTemp = float(input("Outside air temperature: "))
targetTemp = float(input("Target indoor temperature: "))
dTemp = abs(outTemp - targetTemp)
q1 = vertArea*dTemp/rValue
print('\nThe first section has a BTU value of', q1)

print("\n********* BTU Success! Moving on. ****************\n")
# change this to accept user input to list the different uValues and respective areas for the equation = q = uValue*areaWinow*dTemp, then all the q's would be added to calculate q2.
helper = str(input('How many windows are there in the home? :'))
print('\nBecause you said there are * ' + helper + ' * windows in the home, you should enter * ' + helper + ' * items for the uValues and area for the windows.')
uValues = raw_input('Enter the uValues for the different windows, separted by spaces: ')
areaInd_windows = raw_input('Enter the area values for the different windows, separated by spaces: ')
#uValues_List = [int(i) for i in uValues_All.split()]
#areaInd_Wind = [int(k) for k in areaInd_windows.split()]
valuesUValues = map(int, uValues.split())
#print(valuesUValues)
area_windows = map(int, areaInd_windows.split())
sumU = sum(valuesUValues)
sumA = sum(area_windows)
#sumAreaInd_Wind = sum(areaInd_Wind)
print('The numbers: ' + str(valuesUValues) + ' have a sum of: ' + str(sumU))
print('The numbers: ' + str(area_windows) + ' have a sum of: ' + str(sumA))
q2 = sumU*sumA*dTemp

#uValWindow = float(input("Give me that uValue of the windows: "))
#q2 = uValWindow*windowArea*dTemp
print('\nThe second section has a BTU value of', q2)

print("\n********* q2 Success! Moving on. ****************\n")

# get total area of each window for each side of the house
shadeCoEf = float(input("What is the shading coefficient? (Hint: Enter a 1 for no sun):"))
print("\nFor the following calcs, you need to go to \nwww.portal.hud.gov/hubportal/documents/huddoc?id=doc_10603.pdf")
print("It's table 3.25 page 91\n")
# windowsEW = int(input("How many windows are facing the east and west? "))
# windowsS = int(input("How many windows are facing the south? "))
#windowsN = int(input("How many windows are facing the north? "))
# the area needs to be multiplied by the number of windows - this is more precise
aWindowsE = float(input("What is the total area of all the windows facing the east:"))
aWindowsW = float(input("What is the total area of all the windows facing the west:"))
aWindowsS = float(input("What is the total area of all the windows facing the south:"))
aWindowsN = float(input("What is the total area of all the windows facing the north: "))

solCoolE = float(input("\nWhat is the value for east-facing windows: "))
solCoolW = float(input("What is the value for west-facing windows: "))
solCoolN = float(input("What is the value for north-facing windows: "))
solCoolS = float(input("What is the value for south-facing windows: "))
solCoolLoad = float(aWindowsE*solCoolE) + float(aWindowsW*solCoolW) + float(aWindowsS*solCoolS) + float(aWindowsN*solCoolN)
q3 = shadeCoEf*solCoolLoad
print('\nThe third section has a BTU value of', q3)

print("\n********* q3 Success! Moving on. ****************\n")

uValue = float(input("What is the uValue of the roof? "))
aRoof = float(input("What is the area of the roof? "))
uCeiling = float(input("What is the uValue of the ceiling? "))
aCeiling = float(input("What is the area of the ceiling? "))
atticTemp = float(uValue*aRoof*outTemp) + float(uCeiling*aCeiling*targetTemp)
atticTempP2 = float(uValue*aRoof) + float(uCeiling*aCeiling)
atticTotal = atticTemp / atticTempP2

print("\nHere's the temperature of the attic: ", atticTotal)

condInsideArea = float(input("\nWhat is the area of the indoor, conditioned space? "))
nextTemp = outTemp - atticTotal
q4 = abs(uCeiling*condInsideArea*nextTemp)
print('\nThe fourth section has a BTU value of', q4)

print("\n********* q4 Success! Moving on. ****************\n")

# May need to change
cFM = float(input("What is the CFM reading at 50 pascals?: "))
nFactor = float(input("What is the N Factor? Do a search to find your specfic N Factor."))
cFMNatural = cFM/nFactor
q5 = 1.074*cFMNatural*dTemp
print('\nThe fifth section has a BTU value of', q5)

print("\n********* q5 Success! Moving on. ****************\n")

wattage = float(input("What is the wattage from the house?"))
q6 = 3.42*wattage*condInsideArea
print('\nThe sixth section has a BTU value of', q6)

print("\n********* q6 Success! Moving on. ****************\n")

numPeeps = int(input("How many people live in the home? "))
q7 = numPeeps*200
print('\nThe first section has a BTU value of', q7)

print("\n********* q7 Success! Moving on. ****************\n")

grandTotalBTU = q1+q2+q3+q4+q5+q6+q7
print("The total BTUs needed to heat this particular structure is:")
print("You ready?", grandTotalBTU, "BTUs per hour.")
