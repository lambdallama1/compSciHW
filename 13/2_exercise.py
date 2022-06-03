#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp as solve
# Calculate Earth's Orbit Directly by turning the 2nd order
G = 6.6738 * 10 ** -11
M = 1.9891 * 10 ** 30
m = 5.9722e24

def rad(x, y):
    return ( x ** 2 + y ** 2) ** 0.5
def f(r, t):
    x = r[0]
    y = r[1]
    v_x = r[2]
    v_y = r[3]
    dv_x = -G * M * x / rad(x, y) ** 3
    dv_y = -G * M * y / rad(x, y) ** 3
    return np.array([v_x, v_y, dv_x, dv_y], float)

def a_y(x, y):
    return -G * M * y / rad(x, y) ** 3
def a_x(x, y):
    return  -G * M * x / rad(x, y) ** 3


start = 0
end = 2 * 365.25 * 24 * 3600 
N_steps = 100000
stepSize = (end - start) / N_steps
t_points = np.linspace(start, end, N_steps)
x_points = []
y_points = []
p_points = []
v_points = []
e_points = []
u_points = []
r1 = [1.471 * 10 ** 11, 0, 0, 3.0287e4]
t_points = np.linspace(start, end, N_steps)
r = np.array(r1, float)
def U(r):
    return -G *  M / rad(r[0], r[1])
def p(r):   
    return 1/2 *  rad(r[2], r[3]) ** 2

def energy(r):
    return U(r) + p(r)

for t in t_points:
    x_points.append(r[0])
    y_points.append(r[1])
    p_points.append(p(r))
    u_points.append(U(r))
    e_points.append(energy(r))
    v_points.append([r[2], r[3]])
    r[2] += a_x(r[0],r[1]) * stepSize / 2
    r[3] += a_y(r[0],r[1]) * stepSize / 2
    r[0] += r[2] * stepSize
    r[1] += r[3] * stepSize
    r[2] += a_x(r[0],r[1]) * stepSize / 2
    r[3] += a_y(r[0],r[1]) * stepSize / 2


# (i)
plt.plot(x_points, y_points)
plt.plot(0, 0, 'o', c='C1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Earth\'s Orbit', 'Sun'])
plt.title('Earth\'s Orbit')
plt.savefig('Earth\'sOrbit.jpg')

# (ii)
plt.figure()
plt.plot(t_points, p_points)
plt.plot(t_points, u_points)
plt.plot(t_points, e_points)
plt.xlabel('Time')
plt.ylabel('Energy')
plt.legend(['Kinetic', 'Potential', 'Total'])
plt.savefig('energy.jpg')
# (iii)
plt.figure()
plt.plot(t_points, e_points)
plt.xlabel('Time')
plt.ylabel('Total Energy')
plt.title('Total Energy vs Time')
plt.savefig('total_energy.jpg')

