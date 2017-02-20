# -*- coding: utf-8 -*-
"""
daily
convlve.py
"""

import numpy as np
import cv2 

#%% convolution 
np.convolve(np.array([0, 1, 0]), np.array([1, 2, 3]))
np.convolve(np.array([0, 1, 0]), np.array([1, 2, 3]), 'same')

#%% covolution 2
img = np.array([0, 1, 0])
mask = np.array([1, 2, 3])
zero = np.zeros(len(img)+2)
zero[1:-1] = img
img = zero 

mask = mask[::-1]
result = np.zeros_like(img)

for x in range(1, len(img)-1):
    result[x] = img[x-1]*mask[0] + img[x]*mask[1] + img[x+1]*mask[2]
         
#%% cv2
cv2.filter2D(img, -1, mask)        


    