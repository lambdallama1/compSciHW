#!/usr/bin/python3
from scipy.constants import c, h, k 
import numpy as np
import matplotlib.pyplot as plt

def f(x): 
    return 5 * np.exp( -1 * x) + x - 5

def get_root(f, a, b, epsilon = 10 ** -6):
    mid = (a + b) / 2
    while(abs(f(mid)) > epsilon):
        if(np.sign(f(mid)) == np.sign(f(a))):
            a = mid

        else:
            b = mid
        
        mid = ( a + b ) / 2
    
    return  mid


# First root is x = 0, which since lambda and and b are inversely proportional
# to x, would imply that they're infinite. Therefore, the physical root is
# about x = 4.965
x = np.linspace(-1, 7, 100)
im = plt.plot(x, f(x), [0, 4.965], [0,0], 'o')
plt.xlabel('x')
plt.ylabel('5e^-x + x - 5')
plt.savefig('plot1.png')

mid = get_root(f, a = 2,b = 6)
b = h * c / (k * mid)

print("x0 value               = %0.3f" %mid )
print("Displacement Constant  = %0.4f" %b)
print("Temperature of the sun = %0.0fk" % (b / ( 502 * 10 ** -9)))
print("Displacement Constant  = %0.4f" %b)

