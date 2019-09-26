import cv2 
import numpy as np 

img = cv2.imread('dave.jpg') 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
edges = cv2.Canny(gray,50,150,apertureSize = 3) 

# Dibuja una línea horizontal verde con un grosor de 5 px
#img = cv2.line(img,(0,255),(255,255),(0,0,255),5)
cv2.arrowedLine(img, (10, 60), (100, 60), (255, 100, 100), 2, cv2.LINE_4)
img = cv2.rectangle(img,(210,360),(300,500),(255,0,0),3)
img = cv2.circle(img,(255,255), 100, (0,0,255), -1)

cv2.imwrite('houghlines3.jpg',img) 