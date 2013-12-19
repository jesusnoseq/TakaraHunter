from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
# ini movil url
	url(r'^movil/$','principal.views.inicioMovil'),
	url(r'^movil/login/$','principal.views.entrarMovil'),
	url(r'^movil/logout/$','principal.views.salirMovil'),
	url(r'^movil/registro/$','principal.views.registroMovil'),
	url(r'^movil/perfil/$','principal.views.perfilMovil'),
	url(r'^movil/perfil/editar$','principal.views.editarPerfilMovil'),
	
	url(r'^movil/misbusquedas/$','principal.views.miListaBusquedas'),
	url(r'^movil/misbusquedas/(?P<busqueda>\d+)\/[-\w]*$','principal.views.miDetallesBusquedasMovil'),
	url(r'^movil/misbusquedas/salir/(?P<busqueda>\d+)\/[-\w]*$','principal.views.miSalirBusquedasMovil'),
	url(r'^movil/misbusquedas/realizar/(?P<busqueda>\d+)\/[-\w]*$','principal.views.realizandoBusquedaMovil'),
	url(r'^movil/misbusquedas/tesoros/atrapar/(?P<busqueda>\d+)\/[-\w]*$','principal.views.atraparTesorosMovil'),		
	
	url(r'^movil/busquedas/$','principal.views.listaBusquedasMovil'),
	url(r'^movil/busquedas/(?P<busqueda>\d+)\/[-\w]*$','principal.views.detalleBusquedaMovil'),
	url(r'^movil/busquedas/unirse/(?P<busqueda>\d+)\/[-\w]*$','principal.views.unirseBusquedaMovil'),
	url(r'^movil/busquedas/salir/(?P<busqueda>\d+)\/[-\w]*$','principal.views.salirBusquedaMovil'),
					
# fin movil url
	url(r'^$','principal.views.inicio'),

	url(r'^login/$','principal.views.entrar'),
	url(r'^logout/$','principal.views.salir'),
	url(r'^registro/$','principal.views.registro'),
	url(r'^perfil/$','principal.views.perfil'),
	url(r'^perfil/editar$','principal.views.editarPerfil'),
	
	# no se si sabeis la forma de hacer crud en plan rapido con django, bueno, si alguien sabe que se encargue de ese tema
	url(r'^rutas/$','principal.views.listaRutas'),
	url(r'^rutas/nueva/$','principal.views.nuevaRuta'),
	url(r'^rutas/(?P<ruta>\d+)\/[-\w]*$','principal.views.detalleRuta'),
	url(r'^rutas/borrar/(?P<ruta>\d+)\/[-\w]*$','principal.views.borrarRuta'),
	#url(r'^rutas/(?P<ruta>\d+)\/[-\w]*/modificar$','principal.views.modificarRuta'),
	
	url(r'^misbusquedas/$','principal.views.miListaBusquedas'),
	url(r'^misbusquedas/(?P<busqueda>\d+)\/[-\w]*$','principal.views.miDetallesBusquedas'),
	url(r'^misbusquedas/salir/(?P<busqueda>\d+)\/[-\w]*$','principal.views.miSalirBusquedas'),
	url(r'^misbusquedas/realizar/(?P<busqueda>\d+)\/[-\w]*$','principal.views.realizandoBusqueda'),
	url(r'^misbusquedas/tesoros/atrapar/(?P<busqueda>\d+)\/[-\w]*$','principal.views.atraparTesoros'),
	
	url(r'^matriz/$','principal.views.matriz'),
	url(r'^hall/$','principal.views.hall'),
	
	url(r'^busquedas/$','principal.views.listaBusquedas'),
	url(r'^busquedas/(?P<busqueda>\d+)\/[-\w]*$','principal.views.detalleBusqueda'),
	url(r'^busquedas/unirse/(?P<busqueda>\d+)\/[-\w]*$','principal.views.unirseBusqueda'),
	url(r'^busquedas/salir/(?P<busqueda>\d+)\/[-\w]*$','principal.views.salirBusqueda'),
	url(r'^busquedas/borrar/(?P<busqueda>\d+)\/[-\w]*$','principal.views.borrarBusqueda'),
	url(r'^busquedas/nueva/$','principal.views.crearBusqueda'),
	
	url(r'^tesoros/$','principal.views.listaTesoros'),
	url(r'^tesoros/(?P<tesoro>\d+)\/[-\w]*$','principal.views.detalleTesoro'),
	url(r'^tesoros/nuevo/$','principal.views.crearTesoro'),
	url(r'^tesoros/borrar/(?P<tesoro>\d+)\/[-\w]*$','principal.views.borrarTesoro'),
		
	url(r'^about/$', direct_to_template, {'template': 'sobreNosotros.html'}),
	url('^404testing/$', direct_to_template, {'template': '404.html'}),
	#url(r'^login/$', 'auth.views.login_user'),

	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
