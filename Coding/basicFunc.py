import cv2 as cv
# LOADING IMAGE
img = cv.imread("images/scene.jpg")  # READ IMAGE
cv.imshow("Scene", img)

# CONVERT TO GRAYSCALE
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", grayImg)

# BLUR (9, 9) => PARAMETERS (KERNAL SIZE) SHOULD ODD => 1ST PARAMETER IS BLUR DEGREE AND 2ND IS SPREAD
blurImg = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
blurImg1 = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)
cv.imshow("Blur Image", blurImg)
cv.imshow("Blur Image1", blurImg1)

# EDGES CASCADE (BLUR IMAGE HAS LESS EDGES THAN ORIGINAL IMAGE)
canny = cv.Canny(img, 125, 175)  # 125 AND 175 ARE THRESHOLD VALUES
cannyBlurImg = cv.Canny(blurImg, 125, 175)
cv.imshow("Canny Edges", canny)
cv.imshow("Canny Edges Blur Image", cannyBlurImg)

# DILATING THE IMAGE (INCREASE THE THICKNESS OF EDGES)
dilated = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow("Dilated", dilated)

# ERODING (OPPOSITE OF DILATING)
erooded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow("Erorded", erooded)

# RESIZE (INTER_AREA IS BEST FOR SHRINKING, INTER_LINEAR IS BEST FOR ENLARGING, INTER_CUBIC IS SLOW BUT BEST FOR ENLARGING)
resized = cv.resize(img, (600, 700), interpolation=cv.INTER_AREA)
cv.imshow("ResizedArea", resized)
resized = cv.resize(img, (600, 700), interpolation=cv.INTER_LINEAR)
cv.imshow("ResizedLinear", resized)
resized = cv.resize(img, (600, 700), interpolation=cv.INTER_CUBIC)
cv.imshow("ResizedCubic", resized)

# CROPPING
# [start_row:end_row, start_column:end_column]
cropped = img[200:500, 100:800]
cv.imshow("Cropped", cropped)


cv.waitKey(0)
