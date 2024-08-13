import os
import cv2 as cv
import numpy as np

# AVAILABLE PEOPLE
people = ["babar", "saim"]

# ARRAYS FOR LABELS AND FEATURES
features = []
labels = []

# DIRECTORY PATH
DIR = r"G:\Courses\OpenCvLib\Coding\Faces"

# INCLUDING CASCADE FILE  --> (NOT VERY EFFICIENT --> CHANCES OF ERROR IN COUNTING)
haar_cascade = cv.CascadeClassifier("machine/haar_face.xml")

# CREATE TRAIN FUNCTION
def create_train_func():
    # LOOPING THROUGH PEOPLE
    # counter = 0
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        # LOOPING THROUGH IMAGES
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            # READING IMAGE
            img_array = cv.imread(img_path)
            # cv.imshow(f"Image{counter}", img_array)
            # CONVERTING IMAGE TO GRAYSCALE
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # DETECTING FACES
            face_rectangle = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for (x, y, w, h) in face_rectangle:
                face_roi = gray[y:y+h, x:x+w] # ROI --> REGION OF INTEREST
                features.append(face_roi)
                labels.append(label)


            # counter += 1 
    # print("Counter = ", counter)

# CALLING FUNCTION
create_train_func()

# DISPLAYING THE FEATURES AND LABELS
print(f"Length of the features = {len(features)}")
print(f"Length of the labels = {len(labels)}")

# CONVERTING FEATURES AND LABELS TO NUMPY ARRAYS
features = np.array(features, dtype="object")
labels = np.array(labels)

# TRAINING THE RECOGNIZER ON THE FEATURES AND LABELS
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

# SAVING THE RECOGNIZER
face_recognizer.save("face_trained.yml")
np.save("features.npy", features)
np.save("label.npy", labels)

cv.waitKey(0)