import cv2 as cv
import numpy as np

# LOAD THE IMAGE
# img = cv.imread("images/man.jpeg")
# img = cv.imread("images/group1.jpeg")
# img = cv.imread("images/group2.jpeg")
img = cv.imread("images/group3.jpeg")

# CONVERT TO GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# INCLUDING CASCADE FILE  --> (NOT VERY EFFICIENT --> CHANCES OF ERROR IN COUNTING)
haar_cascade = cv.CascadeClassifier("machine/haar_face.xml")

# DETECTING FACES
face_rectangle = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

# PRINTING THE NUMBER OF FACES
print(f"Number of faces found = {len(face_rectangle)}")

# DRAWING RECTANGLES AROUND THE FACES
for (x, y, w, h) in face_rectangle:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow("Detected Faces", img)

cv.waitKey(0)