#!/bin/python3
from scipy.constants import pi, h, m_e

width = float(input("Enter the width in meters: "))

n = float(input("Enter the quantum energy numer: "))

print("The energy level is: ",str( n ** 2 * (h / (2 * pi )) ** 2  * pi ** 2 / ( 2 * m_e * width ** 2)) + "J")
