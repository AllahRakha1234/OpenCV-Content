import cv2 as cv
import numpy as np

# READ IMAGE
img = cv.imread("images/cat.jpg")  
# cv.imshow("Scene", img)

# CONVERT TO GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# # BLUR => 1ST PARAMETER IS BLUR DEGREE AND 2ND IS SPREAD
# blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)

# EDGES CASCADE 
# canny = cv.Canny(blur, 125, 175) 
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)

# THRESHOLDING (BINARIZING IMAGE)
# ret, thresh = cv.threshold(gray,150, 255, cv.THRESH_BINARY)
# cv.imshow("Thresh: ", thresh)


# FINDING CONTOURS ==> RETR_EXTERNAL -> ONLY EXTERNAL CONTOURS, RETR_LIST -> ALL CONTOURS, RETR_TREE -> ALL HIERERCHICAL CONTOURS; CHAIN_APPROX_NONE -> HOW WE APPROXIMATE CONTOURS ( NONE = SIMPLY ALL CONTOURS, SIMPLE = COMPRESS CONTOURS AND RETURN SIMPLE ONE); HIERARCHIES -> HIERARCHY OF CONTOURS (NESTED ELEMENTS); COUNTORS -> LIST OF CONTOURS
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} contour(s) found!")

# DRAW CONTOURS
# blank = np.zeros((500, 500, 3), dtype="uint8") # OR BELOW ONE
blank = np.zeros(img.shape, dtype="uint8")
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)  # -1 -> DRAW ALL CONTOURS ; 1 -> THICKNESS
cv.imshow("Contours Drawn", blank)

cv.waitKey(0)
