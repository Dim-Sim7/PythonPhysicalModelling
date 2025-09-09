# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 20:37:57 2024

@author: DIMITRIJE SIMIC
"""

import numpy as np
import matplotlib.pyplot as plt

bacteria_data = np.loadtxt(r"\\wsl.localhost\Ubuntu\home\dim__sim\workspace\PythonPhysicalModelling\PMLSdata\15novick\g149novickB.csv", delimiter=',')

beta_activity = bacteria_data[:, 1]
time_in_hours = bacteria_data[:, 0]

time_in_hours = [x for x in time_in_hours if x < 10] #remove all items greater than 10
time_in_hours = np.array(time_in_hours)                 # make array into float

N = np.size(time_in_hours, 0)        #get size of new time in hours array
beta_activity = np.resize(beta_activity, N) #resize beta activity array to be same size


def W(A, t, T):
    return A*(np.exp(-T/t) - 1 + (T/t))

def V(t, T):
    return 1 - np.exp(-T/t)
    
A = 1
t = 1
T = time_in_hours

W1 = W(1, 3, T)
W2 = W(0.25, 8, T)
W3 = W(0.92, 4, T)

V1 = V(3.2, T)
V2 = V(154, T)
V3 = V(0.23, T)

plt.plot(W1, T, ".", label="W1")
plt.plot(W2, T, ":", label="W2")
plt.plot(W3, T, ",", label="W3")
plt.plot(beta_activity, time_in_hours, "+", label="Exp Data")

plt.xlabel("E.coli Bacteria")
plt.ylabel("Time")
plt.title("beta galactosidase in E. coli bacteria after introducing an inducer molecule "
"called TMG")

plt.legend()



plt.plot(beta_activity, time_in_hours, '.')
