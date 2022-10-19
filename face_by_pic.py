import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #呼叫資料庫 input library
img = cv2.imread('testing.jpg')                                             #照片名稱 photo's name
img = cv2.resize(img,(370, 470))                                            #控制照片大小 edit size
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                #畫面顏色 show display colour
faces = face_cascade.detectMultiScale(gray, 1.1, 4)                         #臉部偵測  face detection
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)     #畫面調整(應該...) display size(suppose so...) 
cv2.imshow('img', img)                                                      #顯示畫面 show display
cv2.waitKey()

