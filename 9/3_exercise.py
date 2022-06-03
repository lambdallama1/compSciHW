#!/usr/bin/python3
import numpy as np
from scipy.constants import pi, c, hbar, k, sigma

x_min = 0
x_max = 709
bin_width = 1 / 1000
N = int((x_max - x_min) / bin_width)
integral = 0

def func(x):
    if x == 0:
        return 0
    return x ** 3 / (np.exp(x) - 1)

# Calculate the integral via Simpsons Rule
# This first part obviously doesn't do anything, but I may reuse the code
integral += (func(x_max) + func(x_min)) / 2

for i in range(N):
    x_min += bin_width
    integral += func(x_min)

integral *= bin_width
print('(ii)\nSince this is just Simpson\'s rule, \
           \nThe accuracy is just O(deltax ^ 3) ~ %0.1e' %bin_width**3)

# (iii)
print('\n(ii)\nCalculated sigma     = %0.2e' %(integral * k ** 4 / (4 * pi ** 2 * c **    2 * hbar ** 3)))

print('From scipy.constants = %0.2e' %sigma)

