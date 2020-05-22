import numpy as np
import cv2

img = cv2.imread('dog.jpg', 1)

px = img[100,100]
print(px)

img[100,100] = [255,255,255]
px = img[100,100]
print(px)

px = img[200:400,100:350]
#print(px)
#img[200:400,100:350] = [255,255,255]
print(px.shape)

print(img.shape)
print(img.size)
print(img.dtype)

face = img[200:400,100:350]
img[0:200,0:250] = face
cv2.imshow('Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
