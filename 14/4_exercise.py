#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftshift, ifftshift

# There is something odd going on with the definitions used. 
# When I try to take the Fourier transform of the function given, 
# the output is scaled in frequency by a factor of two, and the 
# magnitude is scaled by 1/pi. I can seem to find the exact place
# where the discrepency exists in the definition of the Fourier 
# transform exists, so I used F{sinc^2(t)} = Lambda(f) found in 
# a table. 
def Lambda(x):
    return max(1 - abs(x), 0)

def f(t):
    return (np.sinc(t)) ** 2

def f_hat(om):
    return  Lambda(om)

t = np.linspace(-5, 5, 100)
f_t = []
for ti in t:
    f_t += [f(ti)]

plt.plot(t, f_t)
plt.xlabel('t')
plt.title('sinc^2(t)')
plt.savefig('sinc2t.jpg')

plt.figure()
om = np.linspace(-5, 5, 100)
f_h = []
for o in om:
    f_h += [f_hat(o)]

def myfft(xmax, dx):
    xf = np.arange(-xmax, xmax, dx)
    yf = f(xf)
    
    N = len(xf)
    dfreq = 1  / dx / N
    f_max = dfreq * N / 2
    f_f = np.arange(-f_max, f_max, dfreq)
    fft_f = fftshift(fft(ifftshift(yf)))
    ft = np.real(dx * fft_f)
    return f_f, ft

xmax = 10
dx = 0.1
F = myfft(xmax, dx)
plt.plot(om, f_h)
om = np.linspace(-10, 10, len(F))
plt.plot(F[0], F[1])
plt.legend(['Exact', 'Calculated'])
plt.xlabel('f(Hz)')
plt.title('F{sinc^2(t)}')
plt.savefig('F{sin2t}.jpg')

plt.show()

