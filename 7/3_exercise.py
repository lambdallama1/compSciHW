#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# First build an array, X, where each element consists of three random bits
# Then for each element in X, sum the bits and store the result in t
t = []
X = []
for i in range(10000):
    x = ''
    for k in range(3):
        x += str(round(np.random.random()))    

    X += [x]

for x in X: 
    tails = 0
    for elem in list(x):
        tails += elem == '1'

    t += [tails]

# Make histograms of X and t. The values in X are uniform, whereas the values
# in t follow a binomial distribuition. This is becase 3C0 = 3C3 = 1, and 
# 3C1 = 3C2 = 3. The plot therefore approximates a Gaussian. 
plt.hist(X, align = 'left',  bins = range(9), rwidth=0.7)
plt.ylabel("# of occurances ")
plt.title("(i) Occurances of Each Possible Outcome")
plt.savefig('3(i).png')

plt.figure()
plt.hist(t, bins = [0, 1, 2, 3, 4],align='left', rwidth = 0.7)
plt.ylabel("# of occurances ")
plt.xlabel("# of tails")
plt.title("(ii) Number of Tails ")
plt.savefig('3(ii).png')

# The following three loops computes the number of flips till the two sequences
# are found. To do this, we initate the counters to three, since it must take
# atleast three flips, then, for each itteration, the value of the current
# string is compared to the working string, if there is a match, the working
# string is reset (since we're only interested in the first occurance) the
# count is stored, and then we continue. Otherwise, the string is updated, and
# the counter incremented. 
x = ''
for k in range(3):
    x += str(round(np.random.random()))

num_before_A = []
count_A = 3
N_flips = 100000
for i in range(N_flips):
    if x == '010':
        num_before_A += [count_A]
        count_A = 3
        x = ''
        for k in range(3):
            x += str(round(np.random.random()))

    else: 
        x = list(x)[1] + list(x)[2] + str(round(np.random.random()))
        count_A += 1

x = ''
for k in range(3):
    x += str(round(np.random.random()))

num_before_B = []
count_B = 3
for i in range(N_flips):
    if x == '011':
        num_before_B += [count_B]
        count_B = 3 
        x = ''
        for k in range(3):
            x += str(round(np.random.random()))
    
    else:    
        x = list(x)[1] + list(x)[2] + str(round(np.random.random()))
        count_B += 1

ave_A = sum(num_before_A)/len(num_before_A)
ave_B = sum(num_before_B)/len(num_before_B) 
std_A = np.std(num_before_A)
std_B = np.std(num_before_B)

# Output the results. The simulation agrees with Peter Donnelly. 
# The histograms appear as half-Gaussians. Which makes sense, the mean is in
# the range ~10, the standard deviation ~ 5, 
# there is no upper bound for the number of flips required,
# and ofcourse we can't have negative flips. 
print("Average number of flips before  010 occurs: %0.3f" %ave_A)
print("Average number of flips before  011 occurs: %0.3f" %ave_B)
print("Standard Deviation for sequence 010       : %0.3f" %std_A)
print("Standard Deviation for sequence 011       : %0.3f" %std_B)

plt.figure()
plt.hist(num_before_A)
plt.hist(num_before_B)
plt.legend( ['010', '011'])
plt.xlabel("# Flips before Sequence")
plt.ylabel("# of occurances")
plt.title("(iii) Distribution of Number of Flips Needed")
plt.savefig('3(iii).png')

