import cv2
import os
cur_dir = os.path.abspath(".")
print (cur_dir)
file2 = cur_dir + "\Code\Camera\dataset"
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 640)
cam.set(4, 480)
face_Detector =cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face_id =input('Nhap ID khuong mat ==>')
face_id = face_id.replace("KH","")
print("\n [INFO] Khoi Tao Camera ..")

count =0 
while(True):
    ret,img = cam.read()
    img = cv2.flip(img, 1) 
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_Detector.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:
        cv2.rectangle( img ,(x,y),(x+w,y+h),(255,0,0),2)
        count +=1
        s= file2 + "\\User." + str(face_id)+ '.' +str(count) + ".jpg"
        cv2.imwrite(s, gray[y:y+h,x:x+w])
        cv2.imshow('image',img)

    
    k= cv2.waitKey(100) & 0xff

    if k== 27:
        break
    if count >= 10:
        break
print("\n [INFO] thoat")
cam.release()
cv2.destroyAllWindows()

