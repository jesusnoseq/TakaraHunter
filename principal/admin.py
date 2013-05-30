#encoding:utf-8
from django.contrib.auth.models import User
from django.contrib.auth.admin  import UserAdmin
from django.contrib             import admin
from principal.models import *

class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined', 'first_name', 'last_name', 'sexo', 'telefono', 'fecha_nacimiento', 'profesion')
	fieldsets = (
        ('Información esencial',
				{
            'fields': ('username', 'email', 'password')
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Fechas importantes', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Perfil', {
            'fields': ('first_name', 'last_name', 'sexo', 'telefono', 'fecha_nacimiento', 'profesion', 'foto')
        }),
		('Localización', {
			'fields': ('px','py')
		}),
    )
	
class RutaAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'user', 'origen_x', 'origen_y', 'destino_x', 'destino_y', 'modo')
	fieldsets = (
        ('Ruta', {
            'fields': ('titulo', )
        }),
        ('Información de la ruta', {
            'fields': ('origen_x', 'origen_y', 'destino_x', 'destino_y', 'modo')
        }),
    )
	
class BusquedaAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'slug', 'descripcion', )
	fieldsets = (
        ('Información de la búsqueda', {
            'fields': ('titulo', 'slug', 'descripcion')
        }),
        ('Participantes', {
            'fields': ('participantes', )
        }),
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Ruta, RutaAdmin)
admin.site.register(Busqueda, BusquedaAdmin)
admin.site.register(Tesoro)
#admin.site.register(Participa)

