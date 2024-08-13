import cv2 as cv
import numpy as np

# LOAD THE IMAGE
img = cv.imread("images/building.jpg")
# cv.imshow("Building", img)

# CONVERT TO GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# LAPLACIAN GRADIENT (TO FIND THE EDGES)
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
# cv.imshow("Laplacian", lap)

# SOBEL GRADIENT (TO FIND THE EDGES IN X AND Y DIRECTIONS)
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
# cv.imshow("Sobel X", sobel_x)
# cv.imshow("Sobel Y", sobel_y)

# COMBINE BOTH SOBEL X AND Y
combined_sobel = cv.bitwise_or(sobel_x, sobel_y)
# cv.imshow("Combined Sobel", combined_sobel)

# CANNY EDGE DETECTION (TO FIND THE EDGES) --> IS MORE ACCURATE THAN LAPLACIAN AND SOBEL -> USES GRADIENTS
# cv2.Canny(image, threshold1, threshold2, apertureSize) --> DETAIL PAGE
canny1 = cv.Canny(gray, 150, 175, 5)
canny2 = cv.Canny(gray, 150, 175, 3)
cv.imshow("Canny1", canny1)
cv.imshow("Canny3", canny2)



cv.waitKey(0)