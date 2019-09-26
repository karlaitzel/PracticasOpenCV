import numpy as np 
import cv2 

#Cv2 para leer una imagen
img = cv2.imread('/Users/karlaitzel/Desktop/LENGUAJE NATURAL/nube.jpg',0)
#Mostrar una imagen
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: #Espera a que salga la tecla ESC
  cv2.destroyAllWindows()
elif k == ord('s'): #Espera la tecla 's' para guardar y salir
  cv2.imwrite('deepgray.jpg',img)
  cv2.destroyAllWindows()