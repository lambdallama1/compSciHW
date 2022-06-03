#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# define the system parameters

L = 5       # size of lattice in each direction
J = 1       # interaction parameter
h = 0       # magnetic field
T = 1       # temperature
beta = 1/T  # set k_B = 1

# define the state of the system: LxL grid with (initially) a random spin in each cell
config = 2*np.random.randint(2, size=(L,L))-1

# energy of a given state
def energy():  
    # elegant way of writing the sum over all nearest neighbors in the grid
    interaction = -J*( np.sum(config[0:L-1,:]*config[1:L,:]) +     # contributions of top/bottom neighbors
                       np.sum(config[:,0:L-1]*config[:,1:L]))     # contributions of left/right neighbors
    
    magnetic = -h*np.sum(config)
    return interaction + magnetic

current_energy = energy()

# magnetization of a given state
def magnetization():
    return np.sum(config)/L/L

# Monte Carlo update using Metropolis algorithm
def update():
    
    global config, current_energy    # we want to be able to change the configuration
    
    # choose a random cell in the grid
    cell = np.random.randint(L, size=2)
    i = cell[0]
    j = cell[1]
    
    # calculate the current contribution of this cell to the total energy
    energy_cell = 0
    # be careful with the boundary
    if i != 0:   energy_cell += config[i-1, j]   # left neighbor
    if i != L-1: energy_cell += config[i+1, j]   # right neighbor
    if j != 0:   energy_cell += config[i, j-1]   # top neighbor
    if j != L-1: energy_cell += config[i, j+1]   # bottom neighbor
        
    # the current contribution to the interaction energy is: -J*energy_cell*config[i,j]
    # if we flip the spin, i.e. change config[i,j] to -config[i,j], the new contribution will also change sign
    # this means that overall:
    
    energy_difference = 2*J*energy_cell*config[i,j]
    
    # additional contribution due to the magnetic field
    energy_difference += 2*h*config[i,j]
    
    # check if update is accepted
    accept = False
    if energy_difference<0: 
        accept = True    # always accept updates that decrease the energy
    else:
        prob = np.exp(-beta*energy_difference)
        # standard to calculate event given a probability (see example biasedCoin() in Section 3.1.3)
        rand = np.random.rand()
        if rand<prob:
            accept = True
            
    # if update is accepted we flip the spin
    if accept == True:
        config[i, j] = -config[i, j]
        current_energy += energy_difference
    
    # keep track of the acceptance probability
    return accept

# run the simulation
steps = int(1e6)
magnetization_results = []
energy_results = []
accept_results = []
accept_counter = 0

print('(i)')
for T in [1, 10]:
    for counter in range(steps):
    
        accept_counter += update()
        # keep track of acceptance rates in blocks of 100 steps
        if counter > 10 ** 6 - 10 ** 4:
            accept_results.append(accept_counter)
            accept_counter=0
        
            energy_results.append(current_energy)
            magnetization_results.append(magnetization())
        
    print('Average Magnetization for T = %d: %0.3f' %(T, sum(magnetization_results)
        / len(magnetization_results)))


# (ii)
# Monte Carlo update using Metropolis algorithm
def update2():
    
    global config, current_energy    # we want to be able to change the configuration
    
    # choose a random cell in the grid
    cell = np.random.randint(L, size=2)
    i = cell[0]
    j = cell[1]
    
    # calculate the current contribution of this cell to the total energy
    energy_cell = 0
    # be careful with the boundary
    if i != 0:   energy_cell += config[i-1, j]   # left neighbor
    if i != L-1: energy_cell += config[i+1, j]   # right neighbor
    if j != 0:   energy_cell += config[i, j-1]   # top neighbor
    if j != L-1: energy_cell += config[i, j+1]   # bottom neighbor
    if i == 0:   energy_cell += config[L-1, j]   # left neighbor
    if i == L-1: energy_cell += config[0, j]   # right neighbor
    if j == 0:   energy_cell += config[i, L-1]   # top neighbor
    if j == L-1: energy_cell += config[i, 0]   # bottom neighbor
        
    # the current contribution to the interaction energy is: -J*energy_cell*config[i,j]
    # if we flip the spin, i.e. change config[i,j] to -config[i,j], the new contribution will also change sign
    # this means that overall:
    
    energy_difference = 2*J*energy_cell*config[i,j]
    
    # additional contribution due to the magnetic field
    energy_difference += 2*h*config[i,j]
    
    # check if update is accepted
    accept = False
    if energy_difference<0: 
        accept = True    # always accept updates that decrease the energy
    else:
        prob = np.exp(-beta*energy_difference)
        # standard to calculate event given a probability (see example biasedCoin() in Section 3.1.3)
        rand = np.random.rand()
        if rand<prob:
            accept = True
            
    # if update is accepted we flip the spin
    if accept == True:
        config[i, j] = -config[i, j]
        current_energy += energy_difference
    
    # keep track of the acceptance probability
    return accept

print('(ii)')
for T in [1, 10]:
    for counter in range(steps):
    
        accept_counter += update2()
        # keep track of acceptance rates in blocks of 100 steps
        if counter > 10 ** 6 - 10 ** 4:
            accept_results.append(accept_counter)
            accept_counter=0
        
            energy_results.append(current_energy)
            magnetization_results.append(magnetization())
        
    print('Average Magnetization for T = %d: %0.3f' %(T, sum(magnetization_results)
        / len(magnetization_results)))


