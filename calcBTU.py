# Let's see if I can calculate the overall BTUs needed to heat a building.

print("I'll help you calculate the overall BTUs needed to heat the home.\n")
print("We need a few different values.")

#print("Input the R-value of the walls: ")
#rValue=input()

rValue = float(input("Input the total R-value of the walls: "))

# insert check to make sure not empty value - or break out.

print("Cool.  I have the value as: ", rValue)
print("\nYou'll need to supply the following values.")
wallArea = float(input("Value of the wall area: "))
windowArea = float(input("Window area: "))
vertArea = wallArea - windowArea
outTemp = float(input("Outside air temperature: "))
targetTemp = float(input("Target indoor temperature: "))
dTemp = abs(outTemp - targetTemp)
q1 = vertArea*dTemp/rValue
print("The first q is", q1)

print("\n********* q Success! Moving on. ****************\n")

uValWindow = float(input("Give me that uValue of the windows: "))
q2 = uValWindow*windowArea*dTemp
print("q2 is", q2)

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
print("q3 is", q3)

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
print("q4 is", q4)

print("\n********* q4 Success! Moving on. ****************\n")

# May need to change
cFM = float(input("What is the CFM reading at 50 pascals?: "))
q5 = 1.074*cFM*dTemp
print("q5 is", q5)

print("\n********* q5 Success! Moving on. ****************\n")

wattage = float(input("What is the wattage from the house?"))
q6 = 3.42*wattage*condInsideArea
print("q6 is", q6)

print("\n********* q6 Success! Moving on. ****************\n")

numPeeps = int(input("How many people live in the home? "))
q7 = numPeeps*200
print("q7 is", q7)

print("\n********* q7 Success! Moving on. ****************\n")

grandTotalBTU = q1+q2+q3+q4+q5+q6+q7
print("The total BTUs needed to heat this particular structure is:")
print("You ready?", grandTotalBTU, "BTUs per hour.")


