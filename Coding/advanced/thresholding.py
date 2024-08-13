import cv2 as cv
import numpy as np

# LOAD THE IMAGE
img = cv.imread("images/building.jpg")
# cv.imshow("Building", img)

# CONVERT TO GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# SIMPLE THRESHOLDING ((pixels below threshold_value become 0, and above become 255)
# threshold_value = 100
# threshold, thresh = cv.threshold(gray, threshold_value, 255, cv.THRESH_BINARY)
# cv.imshow("Simple Thresholded", thresh)

# INVERSE THRESHOLDING ((pixels below threshold_value become 0, and above become 255) (Detail page)
# threshold_value = 100
# threshold, thresh_inv = cv.threshold(gray, threshold_value, 255, cv.THRESH_BINARY_INV)
# cv.imshow("Inverse Thresholded", thresh_inv)

# ADAPTIVE THRESHOLDING (TO FIND THE LOCAL THRESHOLD VALUE FOR EACH PIXEL AUTOMATICALLY) (11 HERE IS KERNAL SIZE TO CALC THE NEIGHBOURHOOD PIXELS STRENGTH TO FIND THE THRESHVALUE --> SHOULD BE ODD) (3 SUBTRACTS FROM THE MEAN VALUE TO FIND THE THRESHOLD VALUE) (255 IS THE MAX VALUE)
# TO FIND ADAPTIVE THRESHOLD FOR INVERSE JUST CHANGE THE LAST PARAMETER TO cv.THRESH_BINARY_INV
# cv.ADAPTIVE_THRESH_MEAN_C ==> CAN ALSO cv.ADAPTIVE_THRESH_GAUSSIAN_C => USES GAUSSIAN WEIGHTED SUM OF NEIGHBOURHOOD PIXELS
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3) 
cv.imshow("Adaptive Thresholded", adaptive_thresh)

cv.waitKey(0)