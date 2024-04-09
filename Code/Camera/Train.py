import cv2
import numpy as np
from PIL import Image
import os

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
print("\n [INFO] Dang train du lieu....")
faces,ids = getLabel(path)
recognizer.train(faces, np.array(ids))

recognizer.write(path2)

print("\n [INFO] {0} Khuon mat da duoc nhan dien .Thoat[]".format(len(np.unique(ids))))

