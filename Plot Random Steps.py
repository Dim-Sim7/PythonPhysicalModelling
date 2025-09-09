# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 15:57:37 2024

@author: DIMITRIJE SIMIC
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng() # create a random number generator object
rand = rng.random


num_steps = 500

x_step = rand((num_steps, 1))
y_step = rand((num_steps, 1))


x_trajectory = np.zeros(len(x_step))

for x in range(len(x_step)):
    walk_x = x_step[x] < 0.5
    if walk_x == True:
        x_trajectory[x] = -1
    else:
        x_trajectory[x] = 1
        
   
y_trajectory = np.zeros(len(y_step))

for y in range(len(y_step)):
    walk_y = y_step[y] < 0.5
    if walk_y == True:
        y_trajectory[y] = -1
    else:
        y_trajectory[y] = 1
        


walk_x = np.cumsum(x_trajectory, 0)
walk_y = np.cumsum(y_trajectory, 0)

plt.plot(walk_x, walk_y)
