import cv2

# Cargamos la imagen del disco duro
imagen = cv2.imread("logo.jpg",1)

cv2.imwrite('dibujo.jpg', imagen)
cv2.imshow('window image', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

imagen = cv2.line(imagen, (0,0), (255,255), (0,0,255), 5)
