import cv2

faceCascade = cv2.CascadeClassifier("/Users/sajaalqahtani/PycharmProjects/Facedetection/haarcascade_frontalface_default.xml")

img = cv2.imread("/Users/sajaalqahtani/Desktop/image.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)


cv2.imshow("Result", img)
cv2.waitKey(0)
