import numpy as np
import cv2

img = cv2.imread('dog.jpg',1)

# cv2.line(img, pt1, pt2, color, thickness)
# img is the image on which the line is drawn
# pt1 is the starting point of the line
# pt2 is the end point of the line
# color is the color of the line in bgr
# thickness of the line in int
cv2.line(img, (0,0), (400,400), (0,0,255), 20)

cv2.imshow('Image',img)

# cv2.circle(img, center, radius, color, thickness)
# img is the image on which the circle is drawn
# center is the center of the circle
# radius is the radius of the circle
# color of the circle in bgr
# if thickness=-1, then the circle is filled
cv2.circle(img, (400,400), 100, (255,0,0), -1)

cv2.imshow('Image',img)

cv2.rectangle(img, (15,25), (600,600), (0,255,0), 20)

cv2.imshow('Image',img)

pts =np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)

# cv2.polylines(img, pts, isClosed, color, thickness)
# img is the image on which the circle is drawn
# pts is the array of points to be drawn
# isClosed is True/False specifies if the points are to be joined
# color of the polylines
# thickness of lines
cv2.polylines(img, [pts], True, (0,255,255), 3)

#the font of the sentence
font = cv2.FONT_HERSHEY_SIMPLEX

# to write a sentence on the image
# use cv2.putText(img, text, org, fontface, fontscale, color, thickness, linetype, bottomleftorigin)
# img is the image to be displayed
# text is the text displayed
# org is the point denoting botton-left corner of the text
# fontface is the font of the text
# fontscale is the font size of the text
# color of the text in bgr
# thickness of the line used to write the text :DEFAULT->NONE
# linetype denotes the line type, :DEFAULT->NONE
# eg cv2.LINE_AA is antialiased ,i.e., not like the weird lines on ms paint which show distinct pixels
# bottomleftorigin takes True/False, if true,then the upside-down mirror-image is shown :DEFAULT->NONE
cv2.putText(img, 'Ritikesh, here.', (0,130), font, 1, (200,255,155), 2, cv2.LINE_AA)

cv2.imshow('Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
