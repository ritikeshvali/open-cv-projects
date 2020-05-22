import numpy as np 
import cv2

#the 2nd parameter denotes the imreadmodes:16 means greyscale,reduced to 1/2 size
# imread(filename, flags=None) returns the image after applying the flag
# filename is the name of input image with proper extension
# flags is takes a value of cv::imreadmodes
# cv::imreadmodes specifies the way the image is read,i.e., color,greyscale,reduced size,etc
img = cv2.imread('dog.jpg',16)

# imshow(winname, mat)
# winname is title or name of window
# img is the image to be shown
cv2.imshow('Image',img)

#wait.Key(delay) waits for a key to be pressed for delay time in milliseconds
#delay=0 means forever
# 0xFF is the entered key in its ascii value
# ord('char') returns the ascii value of char, if we simply enter a number,eg ord(27),then ord(27)=27
# 27 is ascii value of escape key
k = cv2.waitKey(0) & 0xFF

if k==27 :
    cv2.destroyAllWindows()

elif k==ord('s'):
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
