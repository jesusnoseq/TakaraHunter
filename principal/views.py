from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate, logout


def inicio(request):
	return render_to_response('inicio.html',{'hola':'na',},context_instance=RequestContext(request))

def login(request):
	return render_to_response('login.html',{'mensaje':'hola'},context_instance=RequestContext(request))


def registro(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))


@login_required(login_url='/login')
def logout(request):
	logout(request)
	state='Sesion cerrada.'
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


