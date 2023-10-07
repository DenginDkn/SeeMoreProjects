
import cv2
import numpy as np

face_levels=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_levels=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
videocatch=cv2.VideoCapture(0)
while True:
    ret, comePictureToVideo = videocatch.read()
    grey = cv2.cvtColor(comePictureToVideo, cv2.COLOR_BGR2GRAY)
    facepictures = face_levels.detectMultiScale(grey,1.1,6)
    for(x,y,w,h) in facepictures:
        cv2.rectangle(
            comePictureToVideo,(x,y),(x+w,y+h),(255,0,0),2)
        roi_grey = grey[y:y+h,x:x+w]
        roi_colorfull = comePictureToVideo[y:y+h,x:x+w]
        eyes = eye_levels.detectMultiScale(roi_grey)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_colorfull,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow("img",comePictureToVideo)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
videocatch.release()
cv2.destroyAllWindows()