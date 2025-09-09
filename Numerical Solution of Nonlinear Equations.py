# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 19:08:49 2024

@author: DIMITRIJE SIMIC
"""

from scipy import optimize
from scipy.optimize import fsolve
from numpy.random import random as rand
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg
from scipy.integrate import quad
from scipy.integrate import odeint

from simple_oscillator import F



#Create array of time values to study
t_min=0; t_max=10; dt=0.1
t = np.arange(t_min, t_max+dt, dt)

# Provide two sets of initial conditions:

initial_conditions = [ (1.0, 0.0), (0.0, 1.0) ]

plt.figure() # create figure add plots later

for y0 in initial_conditions:
    y = odeint(F, y0, t)
    plt.plot(t, y[:, 0], linewidth=2)
    
skip = 5
t_test = t[::skip]
plt.plot(t_test, np.cos(t_test), 'bo') # Exact solution for y0 = (1,0)
plt.plot(t_test, np.sin(t_test), 'ro') # Exact solution for y0 = (0,1)
