import cv2
import mediapipe as mp

cam = cv2.VideoCapture(0)   #擷取攝影

while True:
    rec, img = cam.read()  #讀取攝影機
    if rec:
        cv2.imshow('img', img)  #輸出攝影機

    if cv2.waitKey(1) == ord('q'): #按q關閉視窗
        break





    