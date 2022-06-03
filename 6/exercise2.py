#!/usr/bin/python3

# Voltages are clearly strictly between 0V and 5V, 
# so the inital guess is set to (1V, 1V)
# Solution is found with $\epsilon$ = 10 ** -15
from numpy import exp
import scipy.linalg as LA

R1      = 1000
R2      = 4000
R3      = 3000
R4      = 2000
I0      = 3 * 10 ** -9
VT      = 0.05
Vp      = 5
epsilon = 10 ** - 15
counter = 0
V       = [1, 1]

# Applying KCL at V2, we get (V2 - Vp)/R3 + V2/R4 - Id
def f1(V1, V2):
    return (V1 - Vp) / R1 + V1 / R2 + I0 * ( exp((V1 - V2) / VT) - 1)
def f2(V1, V2):
    return (V2 - Vp) / R3 + V2 / R4 - I0 * ( exp((V1 - V2) / VT) - 1)
def f1_1(V1, V2):
    return 1 / R1 + 1/ R2 + I0 * ( exp((V1 - V2) / VT)) / VT
def f2_2(V1, V2):
    return 1 / R3 + 1 / R3 + I0 * ( exp((V1 - V2) / VT)) / VT
def f1_2(V1, V2):
    return -1 * I0 * ( exp((V1 - V2) / VT)) / VT
def f2_1(V1, V2):
    return -1 * I0 * ( exp((V1 - V2) / VT)) / VT

def f(V1, V2):
    return [f1(V1, V2), f2(V1, V2)]

def del_f(V1, V2):
    return [[f1_1(V1, V2), f1_2(V1, V2)], [f2_1(V1, V2), f2_2(V1, V2)]]

while(abs(f( *V )[0]) > epsilon or abs(f( *V )[1]) > epsilon):
        V -= LA.solve(del_f( *V ), f( *V ))
        counter += 1

print("V1 = %0.3fV" %V[0])
print("V2 = %0.3fV" %V[1])
print("Vd = %0.3fV" %(V[0] - V[1]), " ~ 0.6V")

