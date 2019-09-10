import numpy as np
import cv2, os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def run(path):
	img0 = cv2.imread(path)
	print(path)
	height, width, channels = img0.shape	
	scale_percent = 255*100/width 
	width = int(img0.shape[1] * scale_percent / 100)
	height = int(img0.shape[0] * scale_percent / 100)
	dim = (width, height)
	# resize image
	img = cv2.resize(img0, dim, interpolation = cv2.INTER_AREA)
	#print('Resized Dimensions : ',img.shape)
	
	surface0 = height*width
	surfaceRatio = 3/2
	#print('aire initial: ',surface0)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.2, 5)

	for (x,y,w,h) in faces:
	    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	    roi_gray = gray[y:y+h, x:x+w]
	    roi_color = img[y:y+h, x:x+w]
	    eyes = eye_cascade.detectMultiScale(roi_gray)
	    surface = w*h
	    if surface0/surface >= surfaceRatio: 
	    	print('Found')
	    for (ex,ey,ew,eh) in eyes:
	        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	cv2.imshow('img',img)


images = [ img  for img in os.popen('ls  ../static/images/' ).read().split('\n')[:-1]]

for imPath in images:
	run('../static/images/'+imPath)
	key = cv2.waitKey(0)
	if key == 27: break
	cv2.destroyAllWindows()


