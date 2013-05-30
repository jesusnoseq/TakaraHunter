#encoding:utf-8

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate, logout
from django.db.models import Count
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
				numero_tesoros = Tesoro.objects.filter(recogidaPor=request.user).count()
				listaRutas = Ruta.objects.filter(user=request.user)[:10]
				listaBusquedas = Busqueda.objects.filter(estado="a").filter(participantes=request.user)[:10]
				########################################################################## WARNING CODIGO FEO Y PELIGROSO
				campeon = []
				diamante = []
				platino = []
				oro = []
				plata = []
				bronce = []
				soy_campeon = False
				soy_diamante = False
				soy_platino = False
				soy_oro = False
				soy_plata = False
				soy_bronce = False
				soy_nada = False
				result = Tesoro.objects.values('recogidaPor').annotate(Count('recogidaPor')).order_by('-recogidaPor__count')[:10]
				resultados = []
				for row in result:
					if row['recogidaPor']!=None:
						row['username']=User.objects.get(pk=row['recogidaPor']).username
						resultados.append(row)
				if len(resultados) >= 1:
					campeon = resultados[0]
					if campeon['username'] == request.user.username:
						soy_campeon = True
				if len(resultados) >= 2:
					diamante = resultados[1]
					if diamante['username'] == request.user.username:
						soy_diamante = True
				if len(resultados) >= 3:
					platino = resultados[2]
					if platino['username'] == request.user.username:
						soy_platino = True
				if len(resultados) >= 4:
					oro = resultados[3]
					if oro['username'] == request.user.username:
						soy_oro = True
				if len(resultados) >= 5:
					plata = resultados[4]
					if plata['username'] == request.user.username:
						soy_plata = True
				if len(resultados) >= 6:
					bronce = resultados[5]
					if bronce['username'] == request.user.username:
						soy_bronce = True
				if not(soy_campeon == True or soy_diamante == True or soy_platino == True or soy_oro == True or soy_plata == True or soy_bronce == True):
					soy_nada = True
				########################################################################## WARNING CODIGO FEO Y PELIGROSO
				return render_to_response('perfil.html',
				{
					########################################################################## WARNING CODIGO FEO Y PELIGROSO
					'campeon':soy_campeon,
					'diamante':soy_diamante,
					'platino':soy_platino,
					'oro':soy_oro,
					'plata':soy_plata,
					'bronce':soy_bronce,
					'nada':soy_nada,
					########################################################################## WARNING CODIGO FEO Y PELIGROSO
					'ultimas_busquedas':listaBusquedas,
					'ultimas_rutas':listaRutas,
					'mensaje':state
				},context_instance=RequestContext(request))
			else:
				state = "Tu cuenta no esta activa, contacta con el administrador"
		else:
			state = "Tu nombre de usuario y/o contraseña no son correctos"
	#state="Error al logearse, vuelva a intentarlo."
	return render_to_response('login.html',
	{
		'mensaje':state
	},context_instance=RequestContext(request))

def registro(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/perfil')
	if request.method=='POST':
		formulario = PerfilCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/login')
	else:
		formulario = PerfilCreationForm()
	return render_to_response('registro.html',
	{
		'formulario':formulario
	}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def salir(request):
	logout(request)
	state='Sesión cerrada'
	return render_to_response('mensaje.html',{'mensaje':state},context_instance=RequestContext(request))

@login_required(login_url='/login')
def perfil(request):
	numero_tesoros = Tesoro.objects.filter(recogidaPor=request.user).count()
	listaRutas = Ruta.objects.filter(user=request.user)[:10]
	listaBusquedas = Busqueda.objects.filter(estado="a").filter(participantes=request.user)[:10]
	########################################################################## WARNING CODIGO FEO Y PELIGROSO
	campeon = []
	diamante = []
	platino = []
	oro = []
	plata = []
	bronce = []
	soy_campeon = False
	soy_diamante = False
	soy_platino = False
	soy_oro = False
	soy_plata = False
	soy_bronce = False
	soy_nada = False
	result = Tesoro.objects.values('recogidaPor').annotate(Count('recogidaPor')).order_by('-recogidaPor__count')[:10]
	resultados = []
	for row in result:
		if row['recogidaPor']!=None:
			row['username']=User.objects.get(pk=row['recogidaPor']).username
			resultados.append(row)
	if len(resultados) >= 1:
		campeon = resultados[0]
		if campeon['username'] == request.user.username:
			soy_campeon = True
	if len(resultados) >= 2:
		diamante = resultados[1]
		if diamante['username'] == request.user.username:
			soy_diamante = True
	if len(resultados) >= 3:
		platino = resultados[2]
		if platino['username'] == request.user.username:
			soy_platino = True
	if len(resultados) >= 4:
		oro = resultados[3]
		if oro['username'] == request.user.username:
			soy_oro = True
	if len(resultados) >= 5:
		plata = resultados[4]
		if plata['username'] == request.user.username:
			soy_plata = True
	if len(resultados) >= 6:
		bronce = resultados[5]
		if bronce['username'] == request.user.username:
			soy_bronce = True
	if not(soy_campeon == True or soy_diamante == True or soy_platino == True or soy_oro == True or soy_plata == True or soy_bronce == True):
		soy_nada = True
	########################################################################## WARNING CODIGO FEO Y PELIGROSO
	return render_to_response('perfil.html',
	{
		########################################################################## WARNING CODIGO FEO Y PELIGROSO
		'campeon':soy_campeon,
		'diamante':soy_diamante,
		'platino':soy_platino,
		'oro':soy_oro,
		'plata':soy_plata,
		'bronce':soy_bronce,
		'nada':soy_nada,
		########################################################################## WARNING CODIGO FEO Y PELIGROSO
		'numero_tesoros':numero_tesoros,
		'ultimas_rutas':listaRutas,
		'ultimas_busquedas':listaBusquedas
	},context_instance=RequestContext(request))

@login_required(login_url='/login')
def editarPerfil(request):
	if request.method=='POST':
		formulario= UserForm(request.POST,request.FILES,instance=request.user)
		if formulario.is_valid():
			user = formulario.save(commit=True)
			return HttpResponseRedirect('/perfil')
	else:
		formulario = UserForm(instance=request.user)
	return render_to_response('editarPerfil.html',
	{
		'formulario':formulario
	},context_instance=RequestContext(request))

@login_required(login_url='/login')
def listaRutas(request):
	listaRutas = Ruta.objects.filter(user=request.user)
	for ruta in listaRutas:
		if ruta.modo == "DRIVING":
			ruta.modo = "Coche"
		if ruta.modo == "WALKING":
			ruta.modo = "A pie"
		if ruta.modo == "BICYCLING":
			ruta.modo = "Bicicleta"
		if ruta.modo == "TRANSIT":
			ruta.modo = "Transporte público"
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
			ruta.user = request.user
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
	rutaABorrar = Ruta.objects.get(id=ruta).delete()
	return HttpResponseRedirect('/rutas')

@login_required(login_url='/login')
def detalleBusqueda(request, busqueda):
	busqueda = Busqueda.objects.get(id=busqueda)
	participantes = busqueda.participantes.all()
	participo = False
	for participante in participantes:
		if participante == request.user:
			participo = True
	return render_to_response('detalleBusqueda.html',
	{
		'participo':participo,
		'participantes':participantes,
		'busqueda':busqueda
	},context_instance=RequestContext(request))

@login_required(login_url='/login')
def unirseBusqueda(request, busqueda):
	busqueda = Busqueda.objects.get(id=busqueda)
	busqueda.participantes.add(request.user)
	return HttpResponseRedirect('/busquedas')

@login_required(login_url='/login')
def listaBusquedas(request):
	if request.user.is_superuser == True:
		busquedas1 = Busqueda.objects.filter(participantes=request.user)
	else:
		busquedas1 = Busqueda.objects.filter(estado="a").filter(participantes=request.user)
	if request.user.is_superuser == True:
		busquedas2 = Busqueda.objects.exclude(participantes=request.user)
	else:
		busquedas2 = Busqueda.objects.filter(estado="a").exclude(participantes=request.user)
	return render_to_response('listaBusquedas.html',
	{
		'busquedas1':busquedas1,
		'busquedas2':busquedas2
	},context_instance=RequestContext(request))
	
@login_required(login_url='/login')
def miListaBusquedas(request):
	listaBusquedas = Busqueda.objects.filter(estado="a").filter(participantes=request.user)
	return render_to_response('miListaBusquedas.html',
	{
		'busquedas':listaBusquedas
	},context_instance=RequestContext(request))
	
@login_required(login_url='/login')
def miDetallesBusquedas(request, busqueda):
	busqueda = Busqueda.objects.get(id=busqueda)
	participantes = busqueda.participantes.all()
	return render_to_response('miDetalleBusqueda.html',
	{
		'participantes':participantes,
		'busqueda':busqueda
	},context_instance=RequestContext(request))

@login_required(login_url='/login')
def salirBusqueda(request, busqueda):
	busqueda = Busqueda.objects.get(id=busqueda)
	busqueda.participantes.remove(request.user)
	return HttpResponseRedirect('/busquedas')

@login_required(login_url='/login')
def miSalirBusquedas(request, busqueda):
	busqueda = Busqueda.objects.get(id=busqueda)
	busqueda.participantes.remove(request.user)
	return HttpResponseRedirect('/misbusquedas')

@login_required(login_url='/login')
def matriz(request):
	usuarios=User.objects.all().exclude(px=None).exclude(py=None)
	return render_to_response('matriz.html',{'usuarios':usuarios},context_instance=RequestContext(request))

@login_required(login_url='/login')
def hall(request):
	campeon = []
	diamante = []
	platino = []
	oro = []
	plata = []
	bronce = []
	elresto = []
	result = Tesoro.objects.values('recogidaPor').annotate(Count('recogidaPor')).order_by('-recogidaPor__count')[:10]
	resultados = []
	for row in result:
		if row['recogidaPor']!=None:
			row['username']=User.objects.get(pk=row['recogidaPor']).username
			resultados.append(row)
	if len(resultados) >= 1:
		campeon = resultados[0]
	if len(resultados) >= 2:
		diamante = resultados[1]
	if len(resultados) >= 3:
		platino = resultados[2]
	if len(resultados) >= 4:
		oro = resultados[3]
	if len(resultados) >= 5:
		plata = resultados[4]
	if len(resultados) >= 6:
		bronce = resultados[5]
	if len(resultados) >= 7:
		elresto = resultados[6:]
	return render_to_response('hallDeLaFama.html',
	{
		'campeon':campeon,
		'diamante':diamante,
		'platino':platino,
		'oro':oro,
		'plata':plata,
		'bronce':bronce,
		'elresto':elresto,
	},context_instance=RequestContext(request))

def realizandoBusqueda(request, busqueda):
	busquedaARealizar = Busqueda.objects.get(id=busqueda)
	participantes = busquedaARealizar.participantes.all()
	tesoro = Tesoro.objects.get(busqueda=busquedaARealizar)
	return render_to_response('tesoro.html',
	{
		'participantes':participantes,
		'busqueda':busquedaARealizar,
		'tesoro':tesoro
	},context_instance=RequestContext(request))

@login_required(login_url='/login')
def atraparTesoros(request, busqueda):
	busquedaAAtrapar = Busqueda.objects.get(id=busqueda)
	tesoro = Tesoro.objects.get(busqueda=busquedaAAtrapar)
	tesoro.recogidaPor = request.user
	busquedaAAtrapar.estado = 'c'
	tesoro.save()
	busquedaAAtrapar.save()
	return render_to_response('tesoroAtrapado.html',{
		'tesoro':tesoro,
	},context_instance=RequestContext(request))

@staff_member_required
def crearBusqueda(request):
	if request.method=='POST':
			formulario = BusquedaForm(request.POST, request.FILES)		
			if formulario.is_valid():
				formulario.save()
				pagina_de_vuelta='/busquedas/'
				return HttpResponseRedirect(pagina_de_vuelta)
	else:
		formulario = BusquedaForm()
	return render_to_response('nuevaBusqueda.html',
	{
		'formulario':formulario
	},context_instance=RequestContext(request))

@staff_member_required
def borrarBusqueda(request, busqueda):
	busquedaABorrar = Busqueda.objects.get(id=busqueda).delete()
	return HttpResponseRedirect('/busquedas')

@staff_member_required
def listaTesoros(request):
	tesoros = Tesoro.objects.all()
	return render_to_response('listaTesoros.html',
	{
		'tesoros':tesoros,
	},context_instance=RequestContext(request))

@staff_member_required
def borrarTesoro(request, tesoro):
	tesoroABorrar = Tesoro.objects.get(id=tesoro).delete()
	return HttpResponseRedirect('/tesoros')

@staff_member_required
def crearTesoro(request):
	if request.method=='POST':
			formulario = TesoroForm(request.POST, request.FILES)		
			if formulario.is_valid():
				formulario.save()
				pagina_de_vuelta='/tesoros/'
				return HttpResponseRedirect(pagina_de_vuelta)
	else:
		formulario = TesoroForm()
	return render_to_response('nuevoTesoro.html',
	{
		'formulario':formulario
	},context_instance=RequestContext(request))

@staff_member_required
def detalleTesoro(request, tesoro):
	tesoro = Tesoro.objects.get(id=tesoro)
	return render_to_response('detalleTesoro.html',
	{
		'tesoro':tesoro
	},context_instance=RequestContext(request))
	
	
