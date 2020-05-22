import numpy as numpy
import cv2

#cap is the captured video
#VideoCapture(num) captures video from camera number 'num',here , 0
cap = cv2.VideoCapture(0)

#this while loop processes the captured video, img by img
while(True):

    #read() reads only 1 frame/img of the captured video
    #ret is true/false if an image is grabbed or not
    #frame is the image that has been grabbed
    ret, frame = cap.read() 

    #cvtColor(src, code) changes the color of any image (input)/or converts image from one colorspace to another
    #src,here frame, is the input image
    #gray is the output of the func,i.e.,the image convted to greyscale
    #code,here cv2.color_bgr2gray, is the code for the output img's color
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    #imshow shows the img
    #frame is the name/title of the window
    #gray is the name of input img
    cv2.imshow('frame',gray) #the greyscale img is displayed
    
    #imwrite(filename, img, params=None) saves the img
    #filename is the new file where the image is being saved
    #img is the image being saved
    cv2.imwrite('webcam-opencv-trial.jpg',gray)

    #wait.Key(delay) waits for a key to be pressed for delay time in milliseconds
    #delay=0 means forever
    # 0xFF is the entered key in its ascii value
    # ord('char') returns the ascii value of char, if we simply enter a number,eg ord(27),then ord(27)=27
    # 27 is ascii value of escape key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#deallocates memory, it's a destructor
cap.release()

#destroys/closes all the gui windows
cv2.destroyAllWindows()