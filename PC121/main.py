import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import mediapipe as mp
import os

import cv2
img = cv2.imread('beach.jpeg')
img = cv2.resize(img, (640,480))
cv2.imwrite("5.jpeg", img)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()

imgBg = cv2.imread("5.jpeg")

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, imgBg, threshold=0.8)

    cv2.imshow("image", imgOut)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break