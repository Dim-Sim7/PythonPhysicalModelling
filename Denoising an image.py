# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 19:21:28 2025

@author: DIMITRIJE SIMIC
"""

# 9.2 denoising an image LAB 3

from scipy.signal import convolve
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps
from mpl_toolkits.mplot3d import Axes3D 

tif_file = r"\\wsl.localhost\Ubuntu\home\dim__sim\workspace\PythonPhysicalModelling\PMLSdata\16catphoto\bwCat.tif"

photo = plt.imread(tif_file)

#initialise the filters
small_square_filter = np.ones((5,5)) / 9
big_square_filter = np.ones((15,15)) / 3
gauss_filter = np.loadtxt(r"C:\Users\warlo\Documents\Spyder Working Directory\PMLSdata\16catphoto\gauss_filter.csv", delimiter=",")

#create random number between 0 and 1 with shape of photo array using photo.shape

random_number = np.random.uniform(0, 1, photo.shape)

#Multiply photo array with number to make it noisy

scaled_photo_array = photo * random_number

# Ensure the scaled values remain within the valid range for an image
scaled_photo_array = np.clip(scaled_photo_array, 0, 255).astype(np.uint8)

#apply each filter to noisy image
small_noisy = convolve(scaled_photo_array, small_square_filter, mode='same')
big_noisy = convolve(scaled_photo_array, big_square_filter, mode='same')
gaussian_noisy = convolve(scaled_photo_array, gauss_filter, mode='same')

fig, ax = plt.subplots(2, 2, figsize=(12, 12))
ax[0,0].imshow(scaled_photo_array, cmap='gray')
ax[0,0].set_title('Noisy')
ax[0,1].imshow(small_noisy, cmap='gray')
ax[0,1].set_title('Small')
ax[1,0].imshow(big_noisy, cmap='gray')
ax[1,0].set_title('Big')
ax[1,1].imshow(gaussian_noisy, cmap='gray')
ax[1,1].set_title('Gauss')
plt.show()
plt.tight_layout()

zoom_region = (slice(40, 60), slice(40, 60))  # Define zoom area
fig, zoom_axes = plt.subplots(1, 4, figsize=(16, 4))

zoom_axes[0].imshow(scaled_photo_array[zoom_region], cmap='gray')
zoom_axes[0].set_title("Noisy (Zoomed)")
zoom_axes[0].axis('off')

zoom_axes[1].imshow(small_noisy[zoom_region], cmap='gray')
zoom_axes[1].set_title("Small Square (Zoomed)")
zoom_axes[1].axis('off')

zoom_axes[2].imshow(big_noisy[zoom_region], cmap='gray')
zoom_axes[2].set_title("Big Square (Zoomed)")
zoom_axes[2].axis('off')

zoom_axes[3].imshow(gaussian_noisy[zoom_region], cmap='gray')
zoom_axes[3].set_title("Gaussian (Zoomed)")
zoom_axes[3].axis('off')

plt.tight_layout()
plt.show()
