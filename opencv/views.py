import numpy as np
import cv2, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from django.shortcuts import render
from django.http import  HttpResponse
from .forms import ImageFileUploadForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
face_cascade = cv2.CascadeClassifier( os.path.join(BASE_DIR, 'opencv/haarcascade_frontalface_default.xml'))
eye_cascade = cv2.CascadeClassifier(os.path.join(BASE_DIR,'opencv/haarcascade_eye.xml'))
from opencv.models import *
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
	    surface = w*h
	    ratios.append(surface0/surface)
	
	if len(ratios)==0:
		return('Aucun visage trouvé')
	elif min(ratios) <= surfaceRatio: 
	    return('Visage trouvé')
	else:
		return("Visage trop petit.")

from django.conf import settings
from django.core.files.storage import default_storage

@csrf_exempt
def test(request):
	if request.method == 'POST':
		form = ImageFileUploadForm(request.POST, request.FILES)
		if form.is_valid():
			s = len( ImageName.objects.all() )
			imn = ImageName( name= 'image'+str(s+1)+'.jpeg' ).save()
			save_path = os.path.join(settings.MEDIA_ROOT, 'images', 'image'+str(s)+'.jpeg')
			path = default_storage.save(save_path, request.FILES['image'])
			res = run( path)
			return JsonResponse({'error': False, 'message': res})
		else:
			return JsonResponse({'error': True, 'errors': form.errors})
	else:
		return render(request, 'testopencv.html', locals())