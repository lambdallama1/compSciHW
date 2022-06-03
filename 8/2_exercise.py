#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as LA
from scipy.optimize import minimize

data = np.loadtxt(open('general_llsq_data(1).dat', 'rb'), delimiter=' ')
x = data[:, 0]
y = data[:, 1]
s = data[:, 2]
b =  y / s

def Yi(x, i):
    return x ** (i )

# (i)
# Create Design Matrix A with Dimensions 4 x 100
A = np.zeros([len(s), 4])
for i in range( len(A)):
    for j in range(4):
        A[i,j] = Yi(x[i], j) / s[i]

# (ii) SVD
# No singular values are removed since the ratio of smallest to largest is only
# of order 10 ^ -4
U, S, Vt = LA.svd(A)
Sigma = np.zeros((4, 100))
for i in range(4):
    Sigma[i, i] = 1/S[i]

print("Ratio of smallest singular value to largest %0.3e" %(min(S) / max(S)))

# (iii) get a_n
a = np.dot(np.dot(Vt.T, Sigma), np.dot(U.T, b))
s_sq = np.zeros((4))
for j in range(len(a)):
    for i in range(len(Vt)):
        s_sq[j] += (Vt[j, i] / S[i]) ** 2
for i in range(len(s_sq)):
    print('a%d          = %0.3f' %(i, a[i]))
    print('Error on a%d = %0.3f' %(i, s_sq[i]))

def a_f(x):
    val = 0
    for i in range(4):
        val += a[i] * Yi(x, i)
    return val
def chisq3(params):
    a, b, c, d = params
    return np.sum((a + b * x + c * x ** 2 + d * x ** 3 - y) ** 2 / s ** 2)

# (iv)
# X ^ 2 / dof is between 0 and 2, which indicates a good fit. 
guess = [ 1, 1, 1, 1]
dof = len(data) - 4
chisq3_min = minimize(chisq3, guess).fun
fit = minimize(chisq3, guess).x

print("Difference Between a_n for both methods")
for i in range(len(a)):
    print("a%d_diff = %0.3e" %(i, (a[i] - fit[i]))) 

print('chi ^ 2 / dof = %0.3f ' %(chisq3_min / dof))

# (v) Plots of orriginal data and fit
plt.plot(x, y)
plt.plot(x, a_f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['Data', 'Least Squares Fit'])
plt.imsave('2_(v).png')
