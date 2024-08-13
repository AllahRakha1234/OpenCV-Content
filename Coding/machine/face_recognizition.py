import cv2 as cv
import numpy as np

# AVAILABLE PEOPLE
people = ["babar", "saim"]

# LOADING THE FEATURES AND LABELS ARRAY
# features = np.load("machine/features.npy", allow_pickle=True)
# labels = np.load("machine/labels.npy")

# INCLUDING CASCADE FILE 
haar_cascade = cv.CascadeClassifier("machine/haar_face.xml")

# FACE RECOGNIZER
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("machine/face_trained.yml")

# LOADING THE IMAGE
img = cv.imread("Faces/saim/saim1.jpeg")

# CONVERTING IMAGE TO GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# DETECTING FACES
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

# RECOGNIZING THE FACES
for (x,y,w,h) in faces_rect:

    face_roi  = gray[y:y+h, x:x+w]
    # PREDICTING THE FACE
    label, confidence = face_recognizer.predict(face_roi)

    print(f"Label = {people[label]} with a confidence of {confidence}")
    cv.putText(img, str(people[label]), (60,30), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), thickness=2)

# DISPLAYING THE IMAGE
cv.imshow("Detected Faces", img)

cv.waitKey(0)