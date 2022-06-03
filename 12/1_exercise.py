#!/usr/bin/python3
import numpy as np

# Because we're only looking at the positive section, 
# at the end we need to multiply by 2 ^ d
def ball(r):
    s = 0
    for x in r:
        s += x ** 2
    return s ** 0.5

N = int(1e6)
integrand = 0
for i in range(N):
    x = np.random.rand(10)
    if ball(x) <= 1:
        integrand += 1

integrand *= 2 ** 10 / N
value = np.pi ** 5 / 120
print('Result from integration: %0.4f' %integrand)
print('True value             : %0.4f' %value)
print('Percent error          : '+'{:.3%}'.format(abs(value - integrand) / value))
