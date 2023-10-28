import cv2 as cv
import numpy as np
from cvzone.FaceDetectionModule import FaceDetector
import time

haar_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
detector = FaceDetector()

capture = cv.VideoCapture(0)


while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    img, bboxs = detector.findFaces(frame, draw = False)
    ws, hs = frame.shape[1], frame.shape[0]
    
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
    if bboxs:
        fx, fy = bboxs[0]["center"][0], bboxs[0]["center"][1]
        pos = [fx, fy]
    
        cv.circle(frame, (fx, fy), 80, (0,0,255), 2)
        cv.putText(frame, str(pos), (fx + 15, fy - 15), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv.line(frame, (0, fy), (ws, fy), (0,0,0), 2)
        cv.line(frame, (fx, hs), (fx, 0), (0,0,0), 2)
        cv.circle(frame, (fx, fy), 15, (0, 0, 255), -1)
        cv.putText(frame, "TARGET LOCKED", (10, 50), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 5)
        
    else:
        cv.putText(frame, "NO TARGET", (10, 50), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
        cv.circle(frame, (ws//2, hs//2), 80, (0, 0, 255), 2)
        cv.circle(frame, (ws//2, hs//2), 15, (0, 0, 255), -1)
        cv.line(frame, (0, hs//2), (ws, hs//2), (0, 0, 0), 2)
        cv.line(frame, (ws//2, hs), (ws//2, 0), (0, 0, 0), 2)
       
    cv.imshow("Video", frame)
    
    if cv.waitKey(20) & 0xFF==ord("d"):
        break

capture.release()
cv.destroyAllWindows()