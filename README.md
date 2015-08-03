# CalcBTU

This is a simple Python program to calculate the total amount of BTUs needed to heat a home.  It asks for various user defined inputs and calculates a BTU value.

We needed a simple way to calculate BTUs in scenarios when certain values needed to be manually defined.  For example, if inputs were not given for type of insulation used in the wall, we made assumptions, on known factors by calculating the BTU value of the 2x4 studs and type of siding. This method took some time to do on a calculator, so I wrote this program to help the process.

This should run on any machine that has Python3 installed.

You may run into issues when running it as an executable if your computer is running Python 2 (as many computers are) as its default.

I have the following in my bash profile: alias python='python3'.  In order to run the program, at the prompt I type "python calcBTU.py".

:-)   
