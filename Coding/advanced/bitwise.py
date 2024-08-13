import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')
# cv.imshow("Blank",blank)

# DRAWING A RECTANGLE (cv2.rectangle(image, start_point(x, y), end_point(x, y), color(BGR), thickness))
rectangle = cv.rectangle(blank.copy(), (30, 30),(370, 370), 255, cv.FILLED)
cv.imshow("Rectangle",rectangle)

# DRAWING A CIRCLE (cv2.circle(image, center(CENTRAL POINT), radius, color, thickness))
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
cv.imshow("Circle",circle)


# BITWISE AND OPERATION --> ONLY INTERSECTED/COMMON REGIONS
# This operation will produce a new image (bitwise_and) where the pixel values will be 1 (white) only in the regions where both the rectangle and the circle overlap (common regions). In areas where they do not overlap, the pixel values will be 0 (black).
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise AND",bitwise_and)

# BITWISE OR OPERATION --> INTERSECTED/COMMON & NON-INTERSECTED/NOTCOMMON REGIONS
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR",bitwise_or)

# BITWISE NOT OPERATION --> INVERSE OF THE IMAGE
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("Bitwise NOT",bitwise_not)

# BITWISE XOR OPERATION --> ONLY NOT INTERSECTED/NOTCOMMON REGIONS --> OR - AND
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise XOR",bitwise_xor)

cv.waitKey(0) 


