# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:40:11 2021

@author: Muhammad Ilyas Raza
"""

import numpy as np

#digital value for weight 0.5kg
file= open("calibration_futek16.csv")
a= np.loadtxt(file, delimiter=",")
A=a[:,1:]

B=a[:,0]

x, residuals, rank, s= np.linalg.lstsq(A, B, rcond=None)

print(x)

