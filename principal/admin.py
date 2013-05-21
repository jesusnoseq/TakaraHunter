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
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Ruta)
admin.site.register(Busqueda)
admin.site.register(Tesoro)
#admin.site.register(Participa)

