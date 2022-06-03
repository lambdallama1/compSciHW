#!/usr/bin/python3
import numpy as np

def integrand(x):
    return x ** (3/2) * np.exp(-x)

def p1(x):
    return np.exp(-x)

def p2(x):
    return  np.exp(-x**2 / 2)/(2 * np.pi) ** 0.5 
N = 10000
integral = 0
for i in range(N):
    x_val = np.random.exponential()
    integral += integrand(x_val) / p1(x_val)

integral /= N
val = 3 * np.pi ** 0.5 / 4
print('(i)')
print('Result from integration: %0.4f' %integral)
print('True value             : %0.4f' %val)
print('Percent error          : '+'{:.3%}'.format(abs(val - integral) / val))

# (ii)
N = 10000 
interval = 10
integral = 0
for i in range(N):
    x_val = np.random.normal()
    integral += integrand(abs(x_val)) / p2(abs(x_val))
integral *= 1/(2*N)
val = 3 * np.pi ** 0.5 / 4

print('(ii)')
print('Result from integration: %0.4f' %integral)
print('True value             : %0.4f' %val)
print('Percent error          : '+'{:.3%}'.format(abs(val - integral) / val))

# (iii)
N = 10000 
integral = 0
interval = 100
x_val = interval / 2
for i in range(N):
    xchange = np.random.rand() * interval/10 - interval / 20
    xnew = x_val + xchange
    if xnew < 0: xnew += interval 
    if xnew > interval: xnew -= interval / 10 
    if p1(xnew) / p1(x_val) >= 1:
        x_val = xnew
    else:
        c = np.random.rand() 
        if c <= p1(xnew)/p1(x_val):
            x_val = xnew
            
    integral += integrand(x_val) / p1(x_val)

norm = 1 - np.exp(-interval)
integral *=  norm /N
print(integral)
val = 3 * np.pi ** 0.5 / 4

print('(ii)')
print('Result from integration: %0.4f' %integral)
print('True value             : %0.4f' %val)
print('Percent error          : '+'{:.3%}'.format(abs(val - integral) / val))


