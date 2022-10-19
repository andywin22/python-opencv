import cv2

cam = cv2.VideoCapture('videotest.mp4')                      #擷取影片 capture video
faceDectector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True :
    retV, frame = cam.read()                                 #讀取影片 input video
    warna = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDectector.detectMultiScale(warna, 1.3, 5)

    for(x, y, w, h) in faces: 
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 2))    
    
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()