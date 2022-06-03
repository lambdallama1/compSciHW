#!/bin/python3
Fahren = float(input("Enter the temperture in Fahrenheit: "))
C = (Fahren - 32) * 5 / 9

if C < - 273.15:
	print("ERROR: Below absolute zero")
else:
	print("%0.2fF is %0.2fC " %( Fahren, C))

