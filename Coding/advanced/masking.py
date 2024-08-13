import cv2 as cv
import numpy as np

# LOAD THE IMAGE
img = cv.imread("images/cat.jpg")
cv.imshow("Cat", img)

# CREATE A BLANK MASK WITH THE SAME SIZE AS THE IMAGE
blank = np.zeros(img.shape[:2], dtype=np.uint8)
# cv.imshow("Blank", blank)


# DEFINE THE DIMENSIONS OF THE RECTANGULAR MASK (ADJUST AS NEEDED)
rect_width = img.shape[1] // 2  # HALF THE WIDTH OF THE IMAGE
rect_height = img.shape[0] // 2  # HALF THE HEIGHT OF THE IMAGE

# CALCULATE THE TOP-LEFT AND BOTTOM-RIGHT COORDINATES OF THE RECTANGLE
top_left = ((img.shape[1] - rect_width) // 2, (img.shape[0] - rect_height) // 2)
bottom_right = (top_left[0] + rect_width, top_left[1] + rect_height) 
# HERE top_left[0] = x-coordinate = horizontal dist or width & top_left[1] = y-coordinate = vertical dist.

# CREATE THE CIRCLEULAR MASK (FILLED WITH WHITE)
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2) ,200, 255, -1)
# cv.imshow("Circle", circle)
# APPLY THE RECTANGULAR MASK TO THE IMAGE
# circular_masked_image = cv.bitwise_and(img, img, mask=circle)
# cv.imshow("Circular Masked Image", circular_masked_image)

# CREATE THE RECTANGULAR MASK (FILLED WITH WHITE)
rectangle = cv.rectangle(blank, top_left, bottom_right, (255, 255, 255), thickness=cv.FILLED)
# cv.imshow("Rectangle", rectangle)
# APPLY THE CIRCLEULAR MASK TO THE IMAGE
# rectangular_masked_image = cv.bitwise_and(img, img, mask=rectangle)
# cv.imshow("Rectangular Masked Image", rectangular_masked_image)

# CREATE THE WEIRED MASK (FILLED WITH WHITE)
weired_shape = cv.bitwise_and(rectangle, circle)
cv.imshow("Weired Shape ", weired_shape)
# APPLY THE WEIRED MASK TO THE IMAGE
weired_masked_image = cv.bitwise_and(img, img, mask=weired_shape)
cv.imshow("Weired Masked Image", weired_masked_image)

cv.waitKey(0)
cv.destroyAllWindows()
