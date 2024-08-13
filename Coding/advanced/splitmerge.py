import cv2 as cv
import numpy as np

img = cv.imread("images/building.jpg") 
cv.imshow("Scene",img)

# SPLITTING THE IMAGE INTO ITS RESPECTIVE CHANNELS 
b, g, r = cv.split(img) # HERE EACH SPLLITED COLOR WILL BE A GRAYSCALE IMAGE AND MARKED AS WHITE COLOR
# cv.imshow("Blue",b)
# cv.imshow("Green",g)
# cv.imshow("Red",r)

# MERGING THE SPLIITED CHANNELS INTO A SINGLE IMAGE
merged = cv.merge([b,g,r])
cv.imshow("Merged",merged)

# PRINTING NUMBER OF CHANNELS IN EACH CHANNEL ARRAY 
print(img.shape) # 3 CHANNELS (BGR)
print(b.shape)   # 1 CHANNEL (GRAYSCALE)
print(g.shape)   # 1 CHANNEL (GRAYSCALE)
print(r.shape)   # 1 CHANNEL (GRAYSCALE)

# DISPLAYING THE ONLY SPLIITED CHANNELS IN DIFFERENT COLORS USING NUMPY (CANNOT MERGE ONLY COLORS)
blank = np.zeros(img.shape[:2], dtype='uint8') # CREATING A BLANK IMAGE OF SAME SIZE AS ORIGINAL IMAGE
blue = cv.merge([b, blank, blank]) # MERGING THE BLUE CHANNEL WITH BLANK IMAGE
green = cv.merge([blank, g, blank]) # MERGING THE GREEN CHANNEL WITH BLANK IMAGE
red = cv.merge([blank, blank, r]) # MERGING THE RED CHANNEL WITH BLANK IMAGE
cv.imshow("Only Blue",blue)
cv.imshow("Only Green",green)
cv.imshow("Only Red",red)




cv.waitKey(0)