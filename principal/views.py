from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404

def inicio(request):
	hola = "Hola mundo"
	return render_to_response('inicio.html',
	{
		'hola':hola,
	})
