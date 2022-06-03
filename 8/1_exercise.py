#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, curve_fit
from scipy.special import gammaincc
data = np.loadtxt(open('power_law_data(1).csv', 'rb'), delimiter=',')

size = data[:, 0]
time = data[:, 1]
terr = data[:, 2]
guess = [0.5, 2]
log_size = np.log(size)
log_time = np.log(time)
log_terr = abs(terr / time)


# (i) Plots with error bars on regular and log-log scale
plt.figure()
plt.errorbar(size, time, terr)
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Power Law Data')
plt.savefig('1_(i)regular_scale.png')

plt.figure()
plt.errorbar(log_size,log_time, log_terr)
plt.xlabel('ln(size)')
plt.title('Log-Log Plot of Power Law Data')
plt.ylabel('ln(time)')
plt.savefig('1_(i)log-log.png')

# (ii) Linear fit of log-log data
# X ^ 2 / dof ~ 1, so we have a decent fit. 
def chi(params):
    a, b  = params
    return np.sum( ( a + b * log_size - log_time) ** 2 / ( log_terr
        ) ** 2)


dof = len(time) - 2
chi_min = minimize(chi, guess).fun
best = minimize(chi, guess).x
print('(ii)')
print('a = %0.3f' %np.exp(best[0]))
print('b = %0.3f' %best[1])
print("chi/dof = %0.4f" % (chi_min / dof))
print("q = %0.4f" %( gammaincc(dof / 2, chi_min / 2)))

x =np.log( np.linspace(5, 100, len(time)))

# (iii)
# The values match to 5 decimal places
S = np.sum(1 / log_terr ** 2)
Sx = np.sum(log_size / ( log_terr ** 2))
Sy = np.sum( log_time / (log_terr ** 2))
t = (log_size - Sx / S) / log_terr
Stt = np.sum(t ** 2)

b = np.sum( t * log_time / log_terr ) / Stt
a = (Sy - Sx * b) / S

print('\n(iii)')
print('a = %0.3f' %np.exp(a))
print('b = %0.3f' %b)
error_a = np.sqrt((1 + Sx ** 2/ (S*Stt))/S)
error_b = np.sqrt((1 / Stt))
print('Error on a = %0.3f' % error_a)
print('Error on b = %0.3f' % error_b)

# (iv)
lin_fit = a + b * x
plt.figure()
plt.plot(x, lin_fit)
plt.plot(log_size, log_time)
plt.title('Log-Log of Fit and Data')
plt.xlabel('Log(size)')
plt.ylabel('Log(time)')
plt.legend(['Linear Fit','Log of Data'])
plt.savefig('1_(iv).png')

# (v)
def func(x, a, b):
    return a * x ** (b)


popt, pcov = curve_fit(func, size, time, sigma=terr, absolute_sigma=True)
p_err = np.sqrt(np.diag(pcov))
print("\n(v)")
print('Best fit Parameters: %0.4f, %0.4f' %(popt[0], popt[1]))
print('Error on fit Parameters: %0.4f, %0.4f' %(p_err[0], p_err[1]))

# (vi)
a = np.exp(a)
plt.figure()
plt.plot(size, time)
plt.plot(size, a * size ** b, linewidth=3)
plt.plot(size, popt[0] * size ** popt[1])
plt.ylabel('Time')
plt.title('(vi) Data, Linear Fit, Non-Linear-Fit')
plt.xlabel('Size')
plt.legend(['Orriginal', 'Linear-Fit', 'Non-Linear-Fit'])
plt.savefig('1_(vi).png')
