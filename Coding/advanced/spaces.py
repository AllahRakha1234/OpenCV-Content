import cv2 as cv
import matplotlib.pyplot as plt
# >>>>>>>>>>>>>>> BGR IS IN OPENCV WHILE RGB IN MATPLOTLIB (INVERSE OF COLORS)  <<<<<<<<<<<<<<<<<<<<<<
# >>>>>>>>>>>>>>> CANNOT BE COVERT DIRECTLY GRAYSCALE TO HSV ETC  <<<<<<<<<<<<<<<<<<<<<<

# READING IMAGES 
img = cv.imread("images/home.jpg")  # SMALL RESOLUTION IMAGE
cv.imshow("Scene",img)

# BGR TO GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# BGR TO HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("HSV",hsv)

# BGR TO LAB (L (Lightness); a (Green-Red); b (Blue-Yellow)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow("LAB",lab)

# BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow("RGB",rgb)

# plt.imshow(rgb) # MATPLOTLIB DISPLAYS RGB IMAGE WHICH WILL BE INVERSE OF OPENCV
# plt.show()

# HSV TO BGR 
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow("hsv_bgr",hsv_bgr)

# LAB TO BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
# cv.imshow("lab_bgr",lab_bgr)

# GRAY TO BGR (POSSIBLE BUT RESULT IMAGE WILL BE GRAYSCALE) => DONE USING MATPLOTLIB COLOR MAPS
# gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR) # WILL NOT WORK AS GRAYSCALE HAS ONLY ONE CHANNEL
# cv.imshow("gray_bgr",gray_bgr)
# cv.imshow("gray_bgr_lab",cv.cvtColor(gray_bgr, cv.COLOR_BGR2LAB))
# COLORMAPS PROVIDED BY MATPLOTLIB, SUCH AS 'JET', 'VIRIDIS', 'CIVIDIS', 'PLASMA', 'INFERNO', AND MANY MORE.
# plt.imshow(gray, cmap='jet')
# plt.colorbar()  
# plt.show()

cv.waitKey(0) 
# >>>>>>>>>>>>>>>>>>>>>>>>> ENDED <<<<<<<<<<<<<<<<<<<<<<<<<<
#  >>>> MATPLOTLIB DISPLAYS RGB IMAGES WHILE OPENCV DISPLAYS BGR IMAGES <<<<
# plt.imshow(img)
# plt.show()
# >>>>>>>>>>>>>>>>>>>>>>>>> ENDED <<<<<<<<<<<<<<<<<<<<<<<<<<
