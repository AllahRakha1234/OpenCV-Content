import cv2 as cv

# FUNCTION TO RESCALE FRAMES (FOR IMAGES, VIDEOS AND LIVE VIDEOS(WEBCAM/EXTERNAL CAMERA)))
def rescaleFrames(frame, scale = 0.40):
    height = frame.shape[0] * scale    # frame.shape[0] ==> height
    width = frame.shape[1] * scale     # frame.shape[1] ==> width
    dimensions = (int(width), int(height))
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)
# FUNCTION TO CHANGE RESOLUTIOIN  (ONLY FOR LIVE VIDEOS)
def changeRes(capture, width, height):
    capture.set(3, width) # 3 ==> WIDTH
    capture.set(4, height) # 4 ==> HEIGHT , 10 ==> BRIGHTNESS

# ((((((((( RESCALING IMAGES )))))))))))))
# img = cv.imread("images/scene.jpg") 
# resized_img = rescaleFrames(img)
# cv.imshow("Scene",img)
# cv.imshow("ResizedScene",resized_img)
# cv.waitKey(0) 

# ((((((( RESCALING VIDEO )))))))))))

video = cv.VideoCapture("videos/dog.mp4")
# PRINTING THE VIDEO RESOLUTION
while True:
    
    isTrue, frame = video.read()  # RETURNS FRAMES AND BOOLEAN VALUE TRUE IF THERE ARE FRAMES

    cv.imshow("VideoOriginal", frame)  # DISPLAY THE ORIGINAL FRAME
    risized_frame = rescaleFrames(frame,scale=0.75)
    cv.imshow("VideoResize", risized_frame)  # DISPLAY THE RESIZED FRAME

    # EXIT THE LOOP WHEN 'Q' IS PRESSED (cv.waitKey(10) ==> 10ms DELAY IN EACH FRAME PLAYED) (& BITWISE OPERATION)
    if cv.waitKey(10) & 0xFF == ord('q'): # 0xFF IS A MASK TO GET THE LAST 8 BITS AND INSIDE ORD() CAN BE ANY CHAR
        break

video.release()  # RELEASE THE VIDEO CAPTURE OBJECT
cv.destroyAllWindows()  # CLOSE ALL OPENCV WINDOWS







