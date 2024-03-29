#Create a dataset of images to enroll new face 
#Images saved to /dataset

import cv2
import numpy as np

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam = cv2.VideoCapture(0);

id=input('Enter a unique Face ID: ')
sampleNum=0;
print("Capturing face data ...\nPlease wait")

while(True):
	ret,img = cam.read();
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = faceDetect.detectMultiScale(gray, scaleFactor=1.2 , minNeighbors=5)

	for(x,y,w,h) in faces:
		sampleNum = sampleNum + 1;
		cv2.imwrite( "dataset/User."+str(id)+"."+str(sampleNum)+".jpg", gray[y:y+h,x:x+w])
		cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
		cv2.waitKey(25);	
	cv2.imshow("Face",img);
	cv2.waitKey(1);
	if(sampleNum>100):	#Number of images to capture
		break

cam.release()
cv2.destroyAllWindows()
