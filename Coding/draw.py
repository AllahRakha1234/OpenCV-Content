import cv2 as cv
import numpy as np
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> COLOR === BGR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# CREAING A BLANK IMAGE (REAL IMAGE CAN ALSO BE USE TO DRAW)
blank = np.zeros((500,500,3),dtype = 'uint8') # 500x500 SIZE,3 CHANNELS (BRG), uint8 IS UNSIGNED INTEGER 8 BIT
# cv.imshow("Blank",blank)

# PAINT THE IMAGE A CERTAIN COLOUR
# blank[:] = 0,255,0 # GREEN COLOR  | [:] ==> ALL PIXELS
# blank[100:500] = 0,0,255 # RED COLOR | [100:500] ==> FROM 100 TO 500 PIXELS
# cv.imshow("Red",blank)
# blank[100:101, 100:200] = 255,0,0 # BLUE COLOR | FORMATE IS [y1:y2, x1:x2]
# cv.imshow("Blue",blank)

# DRAW A RECTANGLE
# cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=2) # -1/cv.FILLED ==> FILLED
# cv.rectangle(blank, (0,0), (200,300), (0,255,0), thickness=2) # -1/cv.FILLED ==> FILLED
# cv.imshow("Rectangle",blank)

# DRAW A CIRCLE
# cv.circle(blank, (100,100), 50, (0,255,0), thickness=13) # 40 IS RADIUS, (100,100) IS CENTER OF CIRCLE
# cv.imshow("Circle",blank)
# cv.circle(blank, (100,100), 40, (255,0,0), thickness=cv.FILLED)
# cv.imshow("Circle",blank)

# DRAW A LINE
# cv.line(blank, (100,100), (200,200), (255,255,255), thickness=4) # 40 IS RADIUS, (100,100) IS CENTER OF CIRCLE
# cv.imshow("Line",blank)

# WRITE TEXT ON IMAGE
cv.putText(blank, "Opencv Course", (100,100), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow("Text",blank)

cv.waitKey(0)

 