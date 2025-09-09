# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 19:48:07 2025

@author: warlo
"""
from scipy.signal import convolve
import numpy as np
import matplotlib.pyplot as plt
#%% Stress Fibers image loading and convolve
stressFibers = np.loadtxt(r"\\wsl.localhost\Ubuntu\home\dim__sim\workspace\PythonPhysicalModelling\PMLSdata\17stressFibers\stressFibers.csv", delimiter=',')

plt.figure()
plt.imshow(stressFibers)
plt.show()

#%%
# convolution.py
# -------------------------------------------------------------------------
# This script creates an eLoG (elongated Laplacian of Gaussian) filter that
# emphasizes long, vertical lines in a figure.  The effect of the filter is
# demonstrated on a plus sign.
# ------------------------------------------------------------------------- 
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sim

#%% Create a grid of points for the Gaussian filter.
v = np.arange(-25, 26)
X, Y = np.meshgrid(v, v)

#%% Create elongated Gaussian filter, apply Laplacian.
gauss_filter = np.exp(-0.5*(X**2/2 + Y**2/45))
laplace_filter = np.array( [ [0, -1, 0], [-1, 4, -1], [0, -1, 0] ] )
combined_filter = convolve(gauss_filter, laplace_filter, mode='valid')

#%% Create a plus sign '+' to demonstrate effect of filter.
plus = np.zeros((51, 51))
plus[23:28, 25] = 1.0
plus[25, 23:28] = 1.0

plt.figure()
plt.imshow(plus)
plt.gray()

#%% Apply filter to '+' and display resulting image.
#   Use vmin/vmax to emphasize features within a restricted range of intensity.
cplus = sim.convolve(plus, combined_filter)

plt.figure()
plt.imshow(cplus, vmin=0, vmax=0.5*cplus.max())
plt.gray()

plt.show()


fibers_convolved = convolve(stressFibers, combined_filter, mode='valid')
plt.imshow(fibers_convolved,  vmin=0, vmax=0.5*fibers_convolved.max())

#fibers_convolved = convolve(stressFibers, gauss_filter, mode='valid')
#plt.imshow(fibers_convolved,  vmin=0, vmax=0.5*fibers_convolved.max())


#%% Make a surface plot of the resulting filter
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

ax1.plot_surface(X, Y, gauss_filter, cmap='viridis')
ax1.set_title('Gaussian Filter (3D)')

ax2.plot_surface(np.arange(combined_filter.shape[1]), np.arange(combined_filter.shape[0]), combined_filter, cmap='viridis')
ax2.set_title('Combined Filter (3D)')

