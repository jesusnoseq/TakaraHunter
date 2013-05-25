from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
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
	
	url(r'^matriz/$','principal.views.matriz'),
	
	url(r'^hall/$','principal.views.hall'),
	
	url(r'^busquedas/detalle/(?P<id_busqueda>\d+)\/[-\w]*$','principal.views.detalleBusqueda'),
	url(r'^busquedas/unirse/(?P<id_busqueda>\d+)\/[-\w]*$','principal.views.unirseBusqueda'),
	url(r'^busquedas/salir/(?P<id_busqueda>\d+)\/[-\w]*$','principal.views.salirBusqueda'),
	url(r'^busquedas/tesoros/atrapar/(?P<id_busqueda>\d+)\/[-\w]*$','principal.views.atraparTesoros'),
	url(r'^busquedas/crear/$','principal.views.crearBusqueda'),
	url(r'^busquedas/$','principal.views.listaBusquedas'),
		
	url(r'^about/$', direct_to_template, {'template': 'sobreNosotros.html'}),
	url('^404testing/$', direct_to_template, {'template': '404.html'}),
	#url(r'^login/$', 'auth.views.login_user'),

	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
