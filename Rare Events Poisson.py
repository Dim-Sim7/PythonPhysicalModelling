# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:24:55 2025

@author: DIMITRIJE SIMIC
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as scp
import random

flips = 1000
trials = 1000
threshold = 0.08 # 8% Chance

N = 1000 # for poisson
l_array = np.arange(0, 100, 1, dtype = float) # for poisson

def get_heads (trials, flips):
    
    flips = np.random.choice([0, 1], size = (trials, flips), p = (0.08, 1-0.08))
    heads = np.sum(flips == 0, axis = 1)
    return flips, heads
    
   
    
def waiting_time (flips): # gets waiting time between heads i.e. count of 1s before a 0 occurs + 1
    
    head_pos = np.nonzero(flips[0, :] == 0)[0] + 1 #[0] turns it into an array
    waiting_times = []
    print(head_pos)
    if len(head_pos) > 0:
        if head_pos[0] > 0:
            waiting_times.append(head_pos[0])
    
    waiting_times.extend(np.diff(head_pos))
    
    return waiting_times



    
flips, heads = get_heads(trials, flips)

   
waiting_times = waiting_time(flips)
avg_time = sum(waiting_times) / len(waiting_times)


def Poisson (l, N):
    p = N*((np.exp(-8)*8**l)/scp.factorial(l))
    
    return p

p = Poisson(l_array, N)


bins = np.arange(0, max(heads) + 2) - 0.5
#hist_values, bin_edges, _ = plt.hist(heads, bins=bins, density=False, alpha=0.6, color='blue', label='Histogram')

#plt.plot(l_array, p, 'ro-', label='Poisson × N') # plot poisson
#heads = np.array((np.exp(-8) * 8**flips) / scp.factorial(flips) , size = (trials, flips), dtype = float)

plt.hist(waiting_times, bins=range(1, max(waiting_times)+2), edgecolor='black', alpha=0.7)


plt.xlabel('Event Count (N)')
plt.ylabel('Frequency')
plt.title('Scaled Poisson Distribution')
plt.legend()
plt.grid(True)
plt.show()



