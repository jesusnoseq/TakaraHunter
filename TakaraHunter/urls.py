from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','principal.views.inicio'),
	
	url(r'^login/$','principal.views.login'),
	url(r'^logout/$','principal.views.logout'),
	url(r'^registro/$','principal.views.registro'),
	url(r'^perfil/$','principal.views.perfil'),
	
	# no se si sabeis la forma de hacer crud en plan rapido con django, bueno, si alguien sabe que se encargue de ese tema	
	url(r'^ruta/nueva/$','principal.views.nuevaRuta'),
	url(r'^ruta/(?P<id_ruta>\d+)\/[-\w]*$','principal.views.detalleRuta'),
	url(r'^ruta/modificar/(?P<id_ruta>\d+)\/[-\w]*$','principal.views.modificarRuta'),
	url(r'^ruta/borrar/(?P<id_ruta>\d+)\/[-\w]*$','principal.views.borrarRuta'),
	
	
	url(r'^busqueda/detalle/(?P<id_busqueda>\d+)\/[-\w]*$','principal.views.detalleBusqueda'),
	url(r'^busqueda/unirse/(?P<id_busqueda>\d+)\/[-\w]*$','principal.views.unirseBusqueda'),
	url(r'^busqueda/salir/(?P<id_busqueda\d+)\/[-\w]*$','principal.views.salirBusqueda'),
	
	url(r'^busqueda/tesoros/atrapar/(?P<id_busqueda>\d+)\/[-\w]*$','principal.views.atraparTesoros'),

	url(r'^busqueda/crear/$','principal.views.crearBusqueda'),

		
	url(r'^about/$', direct_to_template, {'template': 'sobreNosotros.html'}),
	url('^404testing/$', direct_to_template, {'template': '404.html'}),
	#url(r'^login/$', 'auth.views.login_user'),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
