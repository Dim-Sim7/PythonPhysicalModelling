# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 22:51:30 2024

@author: warlo
"""

import numpy as np
import matplotlib.pyplot as plt


num_steps = 4000
num_walks = 1000

def get_trajectory_vectorized(num_walks, num_steps):
    """
    

    Parameters
    ----------
    num_steps : int
    
    Generate a random walk trajectory with the given number of steps

    Returns
    -------
    tuple: containing the x and y coordinates of the random walker

    """
    x_step = np.random.choice([-1, 1], size=(num_walks, num_steps))
    y_step = np.random.choice([-1, 1], size=(num_walks, num_steps))
    
    x_positions = np.cumsum(x_step, axis=1)    
    y_positions = np.cumsum(y_step, axis=1)

    return x_positions, y_positions

def get_walks(num_walks, num_steps):
    
    all_x, all_y = get_trajectory_vectorized(num_walks, num_steps)
    x_final = all_x[:, -1]
    y_final = all_y[:, -1]
    displacement = np.sqrt(x_final**2 + y_final**2)
    
    plt.figure(figsize=(12, 12))
    
    #for i in range(num_walks):
       # plt.scatter(all_x[i], all_y[i], label=f'Walk {i+1}')
        
    plt.hist(displacement**2, bins=20, edgecolor='black')
    plt.figure(figsize=(8, 6))
    plt.loglog(x_final, displacement, marker='o', linestyle='None')
    
    plt.title('Random Walks (All 1000 Walks)', fontsize=16)
    plt.xlabel('Walk', fontsize=12)
    plt.ylabel('Displacement', fontsize=12)
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
   #plt.axvline(0, color='gray', linestyle='--', linewidth=0.8)
    plt.grid(True)
    plt.show()

    return x_final, y_final, displacement

    
x_final, y_final, displacement = get_walks(num_walks, num_steps)   
    
plt.scatter(x_final, y_final,s=10)    
plt.xlabel('Delta x')
plt.ylabel("Delta y")

plt.grid(True)    
mean_walk = np.mean(displacement**2)