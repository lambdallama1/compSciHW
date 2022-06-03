#!/usr/bin/python3

import numpy as np
from math import pi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def integrand(x, m, theta):
    return np.cos(m * theta - x * np.sin(theta))

def J(m, x):
    n_steps = 1000
    bin_width = pi / n_steps
    integral = integrand(x, m, 0) + integrand(x, m, pi)
    xn = 0
    for i in range(n_steps - 1):
        xn += bin_width
        if i % 2 == 1:
            integral += 4 * integrand(x, m, xn)

        else:
            integral += 2 * integrand(x, m, xn)

    return bin_width * integral / pi


# Plot the first three Bessel Functions
x = np.linspace(0, 20, 100)
for i in range(3):
    plt.plot(x, J(i, x))
plt.legend(['J0', 'J1', 'J2'])
plt.xlabel('x')
plt.title("First Few Bessel Functions")
plt.savefig('2_(i).png')

# (ii) 
def I(x, y):
    r = (x ** 2 + y ** 2) ** 0.5
    lamb = 500 * 10 ** -9
    k = 2 * pi / lamb
    return (J(1, k * r) / (k * r)) ** 2

plt.figure()
x = np.linspace(-1e-6, 1e-6, 1000)
y = np.linspace(-1e-6, 1e-6, 1000)
X, Y = np.meshgrid(x, y)
I = I(X, Y)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.imshow(I, interpolation='nearest', cmap='plasma', origin='lower')
plt.colorbar(shrink=.92, label='I(r)')
plt.title('Diffraction Intensity')
plt.xticks(())
plt.yticks(())
plt.savefig('2_(ii).png')
