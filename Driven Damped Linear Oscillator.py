# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:56:38 2025

@author: warlo
"""

import numpy as np

import matplotlib.pyplot as plt

#Graphing a driven damped linear oscillator

#Initialise variables

t0 = 0
w = 2*np.pi
w0 = 5*w
w1 = w0
b = w0/20
f0 = 1000
m = 1
# Compute steady state amplitude based on f0

A = f0/(m*np.sqrt(w0**2 - w**2)**2 + (2*b*w)**2)
#State starting variables


A0 = A/2 #Amplitude of second term (damped)
s = 0 #Phase offset driving
s0 = 0 #Phase offset damped

t = np.linspace(t0, 5, 1000) #between t0 = 0 and 5 seconds, take 1000 slices of t values


def x(t):
    
    return A*np.cos(w*t - s) + A0*np.exp(-b*t) * np.cos(w1*t - s0)

plt.plot(t, x(t), label=r'$x(t) = A \cos(wt - \sigma) + A_{\text{tr}} e^{-\beta t} \cos(w_1 t - \sigma_{\text{tr}})$')
plt.xlabel('Time(s)')
plt.ylabel("Displacement (x)")
plt.title('First Five Cycles of Oscillatory Motion with Damping and Driving Force')
plt.legend()
plt.grid(True)
plt.show()

