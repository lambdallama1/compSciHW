#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# (i)
L = 20
temp = 10
cooltime = 1e4
mintemp = 1e-4
G = np.zeros((L, L))
def cool(temp):
    return temp * np.exp(-1/cooltime)

def energy(grid):
    energy = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i, j] != 0:
                energy += 1
    return -energy / 2

def make_points():
    # Pick the fisrt point randomly on the grid
    x1 = np.random.randint(L)
    y1 = np.random.randint(L)
    
    # The simplist way I could think of picking the next point
    # was to create a matrix with all the adjacent steps, and then
    # removing steps if the first point is on a boundary
    directions = [[x1 + 1, y1], [x1 - 1, y1], [x1, y1 + 1], [x1, y1 -1 ]] 
    if x1 == 0:
        directions.remove([x1 - 1, y1])
    if x1 == L-1:
        directions.remove([x1 + 1, y1])
    if y1 == 0:
        directions.remove([x1, y1 -1])
    if y1 == L -1:
        directions.remove([x1, y1 +1])

    n = np.random.randint(len(directions))
    choice = directions[n]
    return [[x1, y1], choice]

pair_locations = []
# Main loop with simulated annealing
while temp > mintemp:
    # Cool the system, get the points, and assign a random 
    # number to the new point, if its to be accepted. 
    temp = cool(temp)
    p1, p2 = make_points()
    val = np.random.normal()

    # If the spot is empty, fill it with the random number
    if G[p1[0], p1[1]] == 0 and G[p2[0], p2[1]] == 0:  
        G[p1[0], p1[1]] = val
        G[p2[0], p2[1]] = val
        pair_locations.append([p1, p2])
    # if there is a dimmer there, remove it according to p
    elif G[p1[0], p1[1]] == G[p2[0], p2[1]]:
        if np.random.rand() < np.exp(-1 / temp):
            if [p1, p2] in pair_locations:
                pair_locations.remove([p1, p2])
            else: 
                pair_locations.remove([p2, p1])

            G[p1[0], p1[1]] = 0
            G[p2[0], p2[1]] = 0

print('Energy for tau = 1e5:', energy(G))

# I couldn't figure out how you plotted them, so i just made a heat map, which
# is not ideal. 
fig, ax = plt.subplots()
im = ax.imshow(G)
ax.set_xticks(np.arange(L))
ax.set_yticks(np.arange(L))
fig.tight_layout()
plt.title('tau = 1e5')
plt.savefig('1e5.jpg')
# (ii) tau = 10 ** 2
L = 20
temp = 10
mintemp = 1e-4
G = np.zeros((L, L))
cooltime = 1e2
pair_locations = []
# Main loop with simulated annealing
while temp > mintemp:
    # Cool the system, get the points, and assign a random 
    # number to the new point, if its to be accepted. 
    temp = cool(temp)
    p1, p2 = make_points()
    val = np.random.normal()

    # If the spot is empty, fill it with the random number
    if G[p1[0], p1[1]] == 0 and G[p2[0], p2[1]] == 0:  
        G[p1[0], p1[1]] = val
        G[p2[0], p2[1]] = val
        pair_locations.append([p1, p2])
    # if there is a dimmer there, remove it according to p
    elif G[p1[0], p1[1]] == G[p2[0], p2[1]]:
        if np.random.rand() < np.exp(-1 / temp):
            if [p1, p2] in pair_locations:
                pair_locations.remove([p1, p2])
            else: 
                pair_locations.remove([p2, p1])

            G[p1[0], p1[1]] = 0
            G[p2[0], p2[1]] = 0

print('Energy for tau = 1e2:', energy(G))

fig2, ax2 = plt.subplots()
im2 = ax2.imshow(G)
ax2.set_xticks(np.arange(L))
ax2.set_yticks(np.arange(L))
fig2.tight_layout()
plt.title('tau = 1e2')
plt.savefig('1e2.jpg')
