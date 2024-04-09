import os
import cv2
import numpy as np
from PIL import Image
import openpyxl
import pandas
class Photo:
    def __init__(self,id):
        self.id = id
    def getFace(self):
        cur_dir = os.path.abspath(".")
        file2 = cur_dir + "\Code\Camera\dataset"
        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cam.set(3, 640)
        cam.set(4, 480)
        face_Detector =cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        face_id =self.id
        face_id = face_id.replace("KH","")
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
            if count >= 30:
                break
    
        cam.release()
        cv2.destroyAllWindows()

def trainFace():
    cur_dir = os.path.abspath(".")
    path = cur_dir + "\Code\Camera\dataset"
    path2 = cur_dir + "\Code\Camera\\trainer\\traier.yml"
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def getLabel(path):
        imagePaths =[os.path.join(path,f) for f in os.listdir(path)]
        faceSamples =[]
        ids=[]

        for imagePath in imagePaths:
            Pil_img =Image.open(imagePath).convert('L')
            img_numpy =np.array(Pil_img,'uint8')

            id =int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)

            for (x,y,w,h) in faces :
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)

        return faceSamples,ids
    faces,ids = getLabel(path)
    recognizer.train(faces, np.array(ids))

    recognizer.write(path2)
def recog():
    file= pandas.read_excel(('data/data.xlsx'),sheet_name='khach') 
    file=file.fillna("")
    mylist=file.values.tolist()
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    
    names = []
    for i in mylist:
        s = i[3].replace("KH","")
        s = int(s)
        names.append([i[0],s])
    cur_dir = os.path.abspath(".")
    path2 = cur_dir + "\Code\Camera\\trainer\\traier.yml"
    recognizer.read(path2)

    faceCascade =cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    font =cv2.FONT_HERSHEY_TRIPLEX

    id =0
    cam = cv2.VideoCapture(0)
    cam.set(3, 1640)
    cam.set(4, 1480)

    minW =0.1*cam.get(3)
    minH =0.1*cam.get(4)

    while True:

        ret,img = cam.read()
        img = cv2.flip(img, 1)

        gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces =faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors =5,
            minSize=(int(minW), int(minH)),
        )
        for(x ,y ,w ,h) in faces:
            cv2.rectangle(img, (x,y),(x+w, y+ h),(0,255,0),2)
            id,confidence = recognizer.predict(gray[y:y+h,x:x +w])
            
            if(confidence < 100) :
                for i in names:
                    if id == i[1]:
                        id = i[0]
                        
                confidence =" {0}%".format(round(100 -confidence))
            else:
                id="Khach la"
                confidence =" {0}%".format(round(100 -confidence))

            cv2.putText(img ,str(id),(x +5 ,y -5),font,1 ,(255,255,255),2)
            cv2.putText(img,str(confidence),(x+5,y+h -5),font,1,(255,255,0),1)
        cv2.imshow("Nhan dien Khuon mat ",img)

        k= cv2.waitKey(10)& 0xff
        if k==27:
            break
    cam.release()
    cv2.destroyAllWindows()  
