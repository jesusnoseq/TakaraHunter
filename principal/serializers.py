#encoding:utf-8

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from principal.models import *


'''class UserSerializer(serializers.HyperlinkedModelSerializer):
    #busquedas = serializers.PrimaryKeyRelatedField(many=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')'''
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'px', 'py','foto')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        
class BusquedaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Busqueda
        fields = ('id', 'slug', 'titulo', 'descripcion', 'fecha_modificacion', 'estado', 'participantes')
        



        