import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# fourcc is a 4 byte code used to specify video codec,i.e., way in which video is played,here XVID
# cv2.VideoWriter_fourcc can be written as (*'XVID') or ('X','V','I','D')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#print(fourcc)

# cv2.VideoWriter(outputfilename, fourcc code, framesPerSec, frameSize)
out = cv2.VideoWriter('output.avi',fourcc,12.0,(640,480))

while True:
    
    # read() returns the next video frame grabbed from the video
    ret, frame = cap.read()

    # cv2.cvtColor(src ,code) returns the image with a different color space
    # src is the input image
    # code is color space
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #out.write(src) writes the next video frame onto out
    out.write(frame)
    
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
