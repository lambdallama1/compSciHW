#!/usr/bin/python3

from scipy.linalg import lu, solve
import numpy as np 

A = np. array([[3, -1, -1, 0], [-1, 4, -1, -1], [-1, -1, 4, -1], [0, -1, -1,
    3]])

b = np.array([5, 5, 0, 0])

V = solve(A, b)

for i in range(4):
    print("V%d = %0.2fV" %(i + 1, V[i]))
