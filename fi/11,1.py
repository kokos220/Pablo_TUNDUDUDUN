import cv2
from PIL import Image

image_path = 'sm.jpeg'
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread(image_path)
face = face_cascade.detectMultiScale(image)

eye = Image.open(image_path)
glasses = Image.open('glas.png')
eye = eye.convert('RGBA')
glasses = glasses.convert('RGBA')

for (x,y,w,h) in face:
    glasses = glasses.resize((w,int(h/3)))
    eye.paste(glasses,(x,int(y+h/4)), glasses)
    eye.save("Fin.png")
    fin = cv2.imread("Fin.png")
    cv2.imshow("Fin",fin)
    cv2.waitKey()

