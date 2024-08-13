import cv2 as cv
import numpy as np

img = cv.imread("images/scene.jpg")  # READ IMAGE
cv.imshow("Scene", img)

# TRANSLATION (-x, -y) -> LEFT, UP | (x, y) -> RIGHT, DOWN

def translateImg(img, x, y):
    translateMat = np.float32([[1, 0, x], [0, 1, y]])  # TRANSLATION MATRIX
    dimensions = (img.shape[1], img.shape[0])  # (WIDTH, HEIGHT)
    return cv.warpAffine(img, translateMat, dimensions)

translated = translateImg(img, 100, -100)
cv.imshow("Translated", translated)

# ROTATION (CLOCKWISE -> POSITIVE, COUNTERCLOCKWISE -> NEGATIVE)
def rotateImg(img, angle, rotPoint=None):
    (height ,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2) # ROTATE ALONG CENTER OF IMAGE
    rotateMat = cv.getRotationMatrix2D(rotPoint, angle, 1)  # LAST PARAMETER -> SCALE FACTOR
    dimensions = (width,height)  
    return cv.warpAffine(img, rotateMat, dimensions)

rotated = rotateImg(img, -45)
cv.imshow("Rotated", rotated)
rotated_rotated = rotateImg(rotated, -45)
cv.imshow("rotated_rotated", rotated_rotated)

# FLIPPING (0 -> VERTICAL FLIP, 1 -> HORIZONTAL FLIP, -1 -> BOTH)
flip = cv.flip(img, -1) 
cv.imshow("Flipped", flip)




cv.waitKey(0)
