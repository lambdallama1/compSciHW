#!/usr/bin/python3

from scipy.linalg import lu, solve 
import numpy as np

A = np.array([[1, 2, 3], [3, 8, 7], [2, 0, 7]])

p, l, u = lu(A)

print("Permutation matrix P=")
for i in range(3):
    print('| %0.2f %0.2f %0.2f |' % (*p[i], ))

print("Lower matrix L=")
for i in range(3):
    print('| %0.2f %0.2f %0.2f |' % (*l[i], ))

print("Upper matrix U=")
for i in range(3):
    print('| %0.2f %0.2f %0.2f |' % (*u[i], ))


b = np.array([1, 2, 3])
x = solve(A, b); 

print("Ax=b => x = (%0.2f, %0.2f, %0.2f)"  % (*x, ))
