import cv2
import mediapipe as mp
import time

cam = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)  #手部偵測 hands dectection
mpDraw = mp.solutions.drawing_utils
handLmsStyle = mpDraw.DrawingSpec(color=(0, 0, 255), thickness=3)  #關節點點大小   knuckles dots thickness
handConStyle = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=5)  #點點連結線粗細 line connection thickness
pTime = 0
cTime = 0

while True:
    ret, img = cam.read()
    if ret:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #顏色 colour
        result = hands.process(imgRGB)

        imgHeight = img.shape[0]
        imgWidth = img.shape[1]

        if result.multi_hand_landmarks:                  #手部點點連結  dots with dots connect
            for handLms in result.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS, handLmsStyle, handConStyle)
                for i, lm in enumerate(handLms.landmark):
                    xPos = int(lm.x * imgWidth)
                    yPos = int(lm.y * imgHeight)

        cTime = time.time()
        pTime = cTime

        cv2.imshow('img', img)

    if cv2.waitKey(1) == ord('q'):
        break


    
    