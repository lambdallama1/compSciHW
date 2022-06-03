#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# So, I went for doing the animation. Overall, it worked well. 
# However, when I tried to use the alias ~, I kept getting errors, 
# so I had to use the full path name on my GalliumOS distrubution. 
# Another issue I ran into, is that this program takes forever to 
# run (~10min) when using N = 10,000. 
#
# This block creates the two sequences of steps with p('d') = 
# p('l') = p('r') = 1/2 p('u')
pos_x = [0]
pos_y = [0]
N = 100
i = 0
j = -1
while i < N:
    n = np.random.randint(4)
    if n == 0 and abs(pos_x[i]) <50 :
        pos_x += [pos_x[i] - 1]
        pos_y += [pos_y[i]]
        j = i
        i += 1
    elif n == 1 and abs(pos_x[i]) < 50:
        pos_x += [pos_x[i] + 1]
        pos_y += [pos_y[i]]
        j = i
        i+= 1
    elif (n == 2) and abs(pos_y[i]) < 50:
        pos_y += [pos_y[i] + 1]
        pos_x += [pos_x[i]]
        j = i
        i += 1
    elif n == 3 and abs(pos_y[i]) < 50:
        pos_y += [pos_y[i] - 1]
        pos_x += [pos_x[i]]
        j = i
        i += 1
    else:
        pos_y += [pos_y[i]]
        pos_x += [pos_x[i]]
        i += 1
    print(i)

# Create the animation
fig = plt.figure()
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')

def animate(j):
    if j >= 0:
        plt.cla()
        plt.xlim(-50, 50)
        plt.ylim(-50, 50)
        plt.scatter(pos_x[j], pos_y[j])
        print(j)
        if j > 0:
            plt.plot(pos_x[:j], pos_y[:j], 'r.', linewidth=0.5)
        plt.xlabel('x')
        plt.ylabel('y')

        plt.title('Random Walk on 2D Grid with Bias')
sim = animation.FuncAnimation(fig, animate, frames = N, repeat=False)

# Save to home directory
f = r"/home/lambdallama/randomWalk.mp4" 
writermp4 = animation.FFMpegWriter(fps=60) 
sim.save(f, writer=writermp4)

