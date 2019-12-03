import cv2
import numpy as np


def detect_faces(img,
                haar_scale_factor=1.1,
                haar_min_neighbors=4,
                show=False):

    face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            )
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,
                                          haar_scale_factor,
                                          haar_min_neighbors)
    for (x, y, w, h) in faces:
        if show:
            cv2.imshow("Face", img[y:y+h,x:x+w])

            if cv2.waitKey(0) & 0xff == 27:
                cv2.destroyAllWindows()
    return faces