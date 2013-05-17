from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
import os

def inicio(request):
	PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
	PROJECT_DIR = os.path.join(PROJECT_DIR, 'static'),
	return render_to_response('inicio.html',
	{
		'hola':PROJECT_DIR,
	})
