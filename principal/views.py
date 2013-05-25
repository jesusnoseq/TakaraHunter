#encoding:utf-8

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate, logout
from principal.models import *
from principal.forms import *

def inicio(request):
	#if not request.user.is_anonymous():
	#	return HttpResponseRedirect('/perfil')
	return render_to_response('inicio.html',{},context_instance=RequestContext(request))

def entrar(request):
	state=""
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/perfil')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		print  username, password
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = "Bienvenido %s" % username
				listaRutas = Ruta.objects.filter(user=request.user)[:10]
				return render_to_response('perfil.html',
				{
					'ultimas_rutas':listaRutas,
					'mensaje':state
				},context_instance=RequestContext(request))
			else:
				state = "Tu cuenta no esta activa, contacta con el administrador."
		else:
			state = "Tu nombre de usuario y/o contraseña no son correctas."
	#state="Error al logearse, vuelva a intentarlo."
	return render_to_response('login.html',
	{
		'mensaje':state
	},context_instance=RequestContext(request))

def registro(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/perfil')
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/login')
	else:
		formulario = UserCreationForm()
	return render_to_response('registro.html',
	{
		'formulario':formulario
	}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def salir(request):
	logout(request)
	state='Sesión cerrada.'
	return render_to_response('mensaje.html',{'mensaje':state},context_instance=RequestContext(request))

@login_required(login_url='/login')
def perfil(request):
	listaRutas = Ruta.objects.filter(user=request.user)[:10]
	
	return render_to_response('perfil.html',
	{
		'ultimas_rutas':listaRutas
	},context_instance=RequestContext(request))

@login_required(login_url='/login')
def editarPerfil(request):
	if request.method=='POST':
		formulario= UserForm(request.POST,request.FILES,instance=request.user)
		if formulario.is_valid():
			user = formulario.save(commit=True)
			return HttpResponseRedirect('perfil/')
	else:
		formulario = UserForm(instance=request.user)
	return render_to_response('editarPerfil.html',{'formulario':formulario},context_instance=RequestContext(request))

@login_required(login_url='/login')
def listaRutas(request):
	listaRutas = Ruta.objects.filter(user=request.user)
	return render_to_response('listaRutas.html',
	{
		'rutas':listaRutas
	},context_instance=RequestContext(request))

@login_required(login_url='/login')
def nuevaRuta(request):
	if request.method=='POST':
		formulario = RutaForm(request.POST, request.FILES)		
		if formulario.is_valid():
			ruta = formulario.save(commit=False)
			ruta.save()
			pagina_de_vuelta='/rutas/'
			return HttpResponseRedirect(pagina_de_vuelta)
	else:
		formulario = RutaForm()
	return render_to_response('nuevaRuta.html',
	{
		'formulario':formulario
	},context_instance=RequestContext(request))

@login_required(login_url='/login')
def detalleRuta(request, ruta):
	rutaAEditar = Ruta.objects.get(id=ruta)
	if request.method=='POST':
		formulario = RutaForm(request.POST, request.FILES, instance=rutaAEditar)		
		if formulario.is_valid():
			ruta = formulario.save(commit=False)
			ruta.save()
			return HttpResponseRedirect('/rutas/')
	else:
		formulario = RutaForm(instance=rutaAEditar)
	return render_to_response('detalleRuta.html',
	{
		'formulario':formulario,
		'id_ruta':ruta
	},context_instance=RequestContext(request))

#@login_required(login_url='/login')
#def modificarRuta(request):
#	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))

@login_required(login_url='/login')
def borrarRuta(request, ruta):
	Ruta.objects.get(id=ruta).delete()
	return HttpResponseRedirect('/rutas/')

@login_required(login_url='/login')
def detalleBusqueda(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))

@login_required(login_url='/login')
def unirseBusqueda(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))

@login_required(login_url='/login')
def listaBusquedas(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))

@login_required(login_url='/login')
def salirBusqueda(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))

@login_required(login_url='/login')
def atraparTesoros(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))

@login_required(login_url='/login')
def matriz(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))

@login_required(login_url='/login')
def hall(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))

@staff_member_required
def crearBusqueda(request):
	return render_to_response('prueba.html',{'mensaje':'hola'},context_instance=RequestContext(request))


