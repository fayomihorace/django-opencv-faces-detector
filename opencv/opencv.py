import numpy as np
import cv2, os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def run(path):
	img0 = cv2.imread(path)
	#print(path)
	height, width, channels = img0.shape	
	scale_percent = 255*100/width 
	width = int(img0.shape[1] * scale_percent / 100)
	height = int(img0.shape[0] * scale_percent / 100)
	dim = (width, height)
	# resize image
	img = cv2.resize(img0, dim, interpolation = cv2.INTER_AREA)
	#print('Resized Dimensions : ',img.shape)
	
	surface0 = height*width
	surfaceRatio = 12
	#print('aire initial: ',surface0)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.01, 5)
	ratios = []
	for (x,y,w,h) in faces:
	    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	    roi_gray = gray[y:y+h, x:x+w]
	    roi_color = img[y:y+h, x:x+w]
	    eyes = eye_cascade.detectMultiScale(roi_gray)
	    surface = w*h
	    ratios.append(surface0/surface)
	    """
	    for (ex,ey,ew,eh) in eyes:
	        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	cv2.imshow('img',img)
	key = cv2.waitKey(0)
	cv2.destroyAllWindows()
	print(ratios)
	"""
	if len(ratios)==0:
		print('Aucun visage trouvé')
	elif min(ratios) <= surfaceRatio: 
	    print('Visage trouvé')
	else:
		print("Visage trop petit.")

run('../media/images/image.jpeg')
os.popen('rm ../media/images/image.jpeg')

	faces = face_cascade.detectMultiScale(gray, 1.01, 5)
	ratios = []
	for (x,y,w,h) in faces:
		surface = w*h
		ratios.append(surface0/surface)
	if len(ratios)==0:
		return('Aucun visage trouvé')
	elif min(ratios) <= surfaceRatio:
		return('Visage trouvé')
	else:
		return("Visage trop petit.")
