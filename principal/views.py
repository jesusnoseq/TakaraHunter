#encoding:utf-8

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate, logout


def inicio(request):
	return render_to_response('inicio.html',{'hola':'na',},context_instance=RequestContext(request))


def entrar(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		print  username, password
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = "Bienvenido %s" % username
			else:
				state = "Tu cuenta no esta activa, contacta con el administrador."
		else:
			state = "Tu nombre de usuario y/o contraseña no son correctas."
	state="Error al logearse, vuelva a intentarlo."
	return render_to_response('login.html',{'mensaje':state},context_instance=RequestContext(request))


def registro(request):
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm()
	return render_to_response('registro.html',{'formulario':formulario},
							  context_instance=RequestContext(request))


@login_required(login_url='/login')
def salir(request):
	logout(request)
	state='Sesión cerrada.'
	return render_to_response('mensaje.html',{'mensaje':state},context_instance=RequestContext(request))

@login_required(login_url='/registro')
def perfil(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))

@login_required(login_url='/registro')
def nuevaRuta(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))

@login_required(login_url='/registro')
def detalleRuta(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))

@login_required(login_url='/registro')
def modificarRuta(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))

@login_required(login_url='/registro')
def borrarRuta(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))

@login_required(login_url='/registro')
def detalleBusqueda(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))

@login_required(login_url='/registro')
def unirseBusqueda(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))

@login_required(login_url='/registro')
def salirBusqueda(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))

@login_required(login_url='/registro')
def atraparTesoros(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))



@staff_member_required
def crearBusqueda(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))


