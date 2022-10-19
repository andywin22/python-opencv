import cv2

cam = cv2.VideoCapture(0)
faceDectector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  #呼叫資料庫 input library

while True :
    retV, frame = cam.read()
    warna = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                           #畫面顏色 show display colour
    faces = faceDectector.detectMultiScale(warna, 1.3, 5)                     #臉部偵測 face detection

    for (x, y, w, h) in faces :
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,63), 2)  #畫面調整(應該...) display size(suppose so...) 
    cv2.imshow('cam', frame)                                                  #顯示畫面 show display                       
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()