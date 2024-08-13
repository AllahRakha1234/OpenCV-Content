import cv2 as cv

# (((((((((((((((( READING IMAGES ))))))))))))))))))

img = cv.imread("images/scene.jpg")  # SMALL RESOLUTION IMAGE
cv.imshow("Scene",img)
cv.waitKey(0) 

# img = cv.imread("images/lion.jpg")  # LARGE RESOLUTION IMAGE
# cv.imshow("Lion",img)
# cv.waitKey(0) 

# ((((((( READING VIDEO )))))))))))

video = cv.VideoCapture("videos/dog.mp4")
# PRINTING THE VIDEO RESOLUTION
# while True:
#     isTrue, frame = video.read()  # RETURNS FRAMES AND BOOLEAN VALUE TRUE IF THERE ARE FRAMES

#     if not isTrue:
#         break  # BREAK THE LOOP IF THERE ARE NO MORE FRAMES

#     cv.imshow("Video", frame)  # DISPLAY THE FRAME

#     # EXIT THE LOOP WHEN 'Q' IS PRESSED (cv.waitKey(10) ==> 10ms DELAY IN EACH FRAME PLAYED) (& BITWISE OPERATION)
#     if cv.waitKey(10) & 0xFF == ord('q'): # 0xFF IS A MASK TO GET THE LAST 8 BITS AND INSIDE ORD() CAN BE ANY CHAR
#         break

# video.release()  # RELEASE THE VIDEO CAPTURE OBJECT
# cv.destroyAllWindows()  # CLOSE ALL OPENCV WINDOWS







