#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

# (i)
dow = np.loadtxt('dow.txt', float)
t = np.linspace(2006, 2011, len(dow))
plt.plot(t, dow)
plt.xlabel('Year')
plt.savefig('dow.jpg')

# (ii)
DOW = fft(dow)
DOW_MOD = DOW
DOW_MOD[51:973] = 0
dow_mod = ifft(DOW_MOD)
plt.figure()
plt.plot(t, dow_mod)
plt.xlabel('Year')
plt.plot(t, dow)
plt.legend(['Smoothed DOW', 'DOW'])
plt.savefig('dow_plus_smoothing.jpg')

# (iii) Noise, in general, is high frequency. So, removing those frequencies
# (setting the values of the Fourier transform to zero and tranforming back)
# removes all the roughness and irregularities. 
DOW = fft(dow)
DOW_MOD = DOW
DOW_MOD[10:1014] = 0
dow_mod2 = ifft(DOW_MOD)
plt.figure()
plt.plot(t, dow_mod2)
plt.xlabel('Year')
plt.plot(t, dow)
plt.plot(t, dow_mod)
plt.legend(['DOW 2\%', 'DOW', 'DOW 10\%'])
plt.savefig('dow_plus_extra_smoothing.jpg')
plt.show()

