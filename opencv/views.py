import numpy as np
import cv2, os

from django.shortcuts import render
from django.http import  HttpResponse
from .forms import ImageFileUploadForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def test(request):
	if request.method == 'POST':
		form = ImageFileUploadForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			res = os.popen('cd opencv && python3 opencv.py' ).read()
			return JsonResponse({'error': False, 'message': res})
		else:
			return JsonResponse({'error': True, 'errors': form.errors})
	else:
		return render(request, 'testopencv.html', locals())