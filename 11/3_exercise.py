#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# So, I went for doing the animation. Overall, it worked well. 
# Another issue I ran into, is that this program takes forever to 
# run (>10min) when using N = 10,000. So, N was set to 1,000
# for the animation, and the full 10,000 are plotted in a 
# seperate .png. 
#
# This block creates the two sequences of steps with p('d') = 
# p('l') = p('r') = 1/2 p('u')
N = 10000
pos_x = [0] * N
pos_y = [0] * N
i = 0
while i < N - 1:
    n = np.random.randint(5)
    # left
    if n == 0 and pos_x[i] > -50:
        pos_x[i + 1] = pos_x[i] - 1
        pos_y[i + 1] = pos_y[i]
        i           += 1
    # right
    elif n == 1 and pos_x[i] < 50:
        pos_x[i + 1] = pos_x[i] + 1
        pos_y[i + 1] = pos_y[i]
        i           += 1
    # up
    # Bias towards up
    elif (n == 2 or n == 4) and pos_y[i] < 50:
        pos_y[i+1] = pos_y[i] + 1
        pos_x[i+1] = pos_x[i]
        i         += 1
    # down
    elif n == 3 and pos_y[i] > -50:
        pos_y[i + 1] = pos_y[i] - 1
        pos_x[i + 1] = pos_x[i]
        i           += 1

# Plot full path and final position
plt.xlim(-50, 50)
plt.ylim(-50, 50)
plt.plot(pos_x, pos_y, 'r.', linewidth=0.8)
plt.plot(pos_x[-1], pos_y[-1], 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Random Walk on 2D Grid with Bias')
plt.legend(['Position', 'Path'])
plt.savefig('Random_Walk.png')

# Create the animation
# In each step, the current location of the particle is plotted
# using a scatter plot in blue, and all previous values are plotted in red
N = 1000
fig = plt.figure()
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')
def animate(j):
    if j >= 0:
        plt.cla()
        plt.xlim(-50, 50)
        plt.ylim(-50, 50)
        plt.plot(pos_x[:j], pos_y[:j], 'r.', linewidth=0.8)
        plt.scatter(pos_x[j], pos_y[j])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Random Walk on 2D Grid with Bias')
        plt.legend(['Path', 'Position'])
sim = animation.FuncAnimation(fig, animate, frames = N, repeat=False)

# Save animation
writermp4 = animation.FFMpegWriter(fps=30) 
sim.save('Random_Walk.mp4', writer=writermp4)

