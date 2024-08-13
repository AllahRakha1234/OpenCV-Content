import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# LOAD THE IMAGE
img = cv.imread("images/scene.jpg")
# cv.imshow("Scene", img)

# BGR TO GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# CREATING A HISTOGRAM ----> (cv.calcHist(images, channels, mask(portion for histogram, None = All), histSize(number of bins), ranges[no. of pixels])) ----> EACH PARAMETER IS GIVEN IN SQUARE BRACKETS [] ----> BINS REPRESENT THE INTERVAL OF INTENSITY LEVEL
# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("No. of pixels")
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# CALCULATING HISTOGRAM FOR SPECIFIC PORTION (MASKED PORTION)
# blank = np.zeros(img.shape[:2], dtype='uint8')
# circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 150, 255, -1)

# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow("Mask", mask)

# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])
# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("No. of pixels")
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# COLORED HISTOGRAM

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 150, 255, -1)
 
color = ('b', 'g', 'r')

plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("No. of pixels")

for i,col in enumerate(color):
    print(i, col)
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()


cv.waitKey(0)