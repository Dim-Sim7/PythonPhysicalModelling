# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:39:02 2025

@author: warlo
"""

import numpy as np
import math


def J(m, x, N=1000): #to calculate area under a function (integral)
    if N % 2 == 1:
        raise ValueError("Simpson's rule requires an even number of intervals (N must be odd).")

    a, b = 0, math.pi
    h = (b - a) / N  # Step size
    
    theta = np.linspace(a, b, N+1)
    f_theta = np.cos(m*theta - x * np.sin(theta))
    
    #integral takes the sum of f_theta from theta values derived from the limites of 0 to pi using linspace (slices the limits)
    integral = (h / 3) * (f_theta[0] + f_theta[-1] +  #first and last values
                      4 * np.sum(f_theta[1:-1:2]) + # sum of odd indexed terms
                      2 * np.sum(f_theta[2:-2:2]))# sum of even indexed values

    return integral / math.pi  # Final J_m(x) value


J0 = J(0, 20)