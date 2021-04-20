import cv2
import numpy as np
import matplotlib as plt
from time import sleep
#%matplotlib inline
import cv2
import os
def load_images(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

folder="/home/sharan/Desktop/DSC_Verzeo/major project/Phase_3/input_images_P3"
images = []
images = load_images(folder)
# faces = []
dirr = '/home/sharan/Desktop/DSC_Verzeo/major project/Phase_3/output_images_P3'
k=1
print('classifying ...')
for img in images :
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    try:
        face = face_cascade.detectMultiScale(grey_img, scaleFactor=1.05, minNeighbors=5 )
    except:
        continue
    print(face)
    for x,y,w,h in face:
        img = cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 1)
        face = img[y:y + h, x:x + w]
        cv2.imwrite(os.path.join( dirr , 'out_'+str(k)+'.jpg'),face)
        cv2.imshow('img',cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
        #sleep(1.5)              
        k= k+1   
            
cv2.waitKey()
cv2.destroyAllWindows()

