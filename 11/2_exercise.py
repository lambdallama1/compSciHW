#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

def p(x):
    return 2 / np.sqrt(2 * np.pi) * np.exp(-x ** 2 / 2)


# (i) plot p(x) in the range [0, 4]
x = np.linspace(0, 4, 100)
plt.plot(x, p(x))
plt.xlabel('x')
plt.ylabel('p(x)')
plt.title('p(x) vs x')
plt.savefig('(i).png')

# (ii) Put p(x) in a box. The y-value of which is just p(0). Since p(x) is 
# decreasing, p(x) <= p(0) for all x
def rect_box(x):
    return p(0)

N = 10000
success = 0
rej = []
for i in range(N):
    x_val = 4 * np.random.rand()
    y_val = p(0) *  np.random.rand()
    if y_val < p(x_val):
        success += 1
        rej.append(x_val)

# Plot the histogram of x-value density along side p(x)
plt.figure()
plt.hist(rej, bins = 20, density=True, alpha=0.5)
plt.xlabel('x')
plt.plot(x, p(x))
plt.title('Naive Rejection Method')
plt.legend(['p(x)', 'Rejection Method'])

plt.savefig('2_(ii).png')

# Return the Efficiency
print('(ii)\nEfficiency = %0.2f' %(success / N))

# (iii) Use a more appropriate cutoff function. 
# Plot it along with p(x) to insure it's always above
def f(x):
    return 2 ** 0.5 * np.exp(-x)

plt.figure()
plt.plot(x, f(x))
plt.plot(x, p(x))
plt.xlabel('x')
plt.legend(['f(x)', 'p(x)'])
plt.title('p(x) vs Cut-Off Function')
plt.savefig('2_(iii).png')

# (iv) Use rejection method again using new funtion. 
# The x-values being created using numpy's exponential 
# distribution. 
success = 0
reject = []
for i in  range(N):
    x_val =  np.random.exponential()
    y_val = f(x_val) *  np.random.rand()
    if y_val < p(x_val):
        success += 1
        reject.append(x_val)

# Plot the histogram of x-value density along side p(x)
plt.figure()
plt.hist(reject, bins = 20, density=True)
plt.plot(x, p(x))
plt.xlabel('x')
plt.title('Rejection Method with comparison function\
           \nf(x) = $\sqrt{2} * e ^{-x}$')
plt.legend(['p(x)', 'Rejection Method'])
plt.savefig('2_(iv).png')

# Return the Efficiency. More than double that of the naive approach.  
print('(iv)\nEfficiency = %0.2f' %(success / N))
plt.show()
