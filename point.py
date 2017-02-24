# -*- coding: utf-8 -*-
# points extraction

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('point.tif', 0)

w = np.ones((3,3), np.uint8)*-1
w[1,1] = 8

g = cv2.filter2D(img, -1, w)
_, th = cv2.threshold(g, 50, 255, 0)

cv2.imshow('filt', th)
cv2.waitKey(0)
