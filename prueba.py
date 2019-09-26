import numpy as np
import cv2

# Crea una imagen en negro
img = np.zeros((512,512,3), np.uint8)

# Dibuja una línea horizontal verde con un grosor de 4 px
img = cv2.line(img,(0,255),(511,255),(0,255,0),4)

# Dibuja un rectangulo 
img = cv2.rectangle(img,(210,360),(300,500),(255,0,0),3)

#Dibuja un circulo 
img = cv2.circle(img,(255,255), 100, (0,0,255), -1)

#Dibuja un eclipse 
img = cv2.ellipse(img,(255,105),(100,50),0,0,180,255,-1)

