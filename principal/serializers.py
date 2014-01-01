#encoding:utf-8

from django.contrib.auth.models import User, Group
from rest_framework import serializers


'''class UserSerializer(serializers.HyperlinkedModelSerializer):
    #busquedas = serializers.PrimaryKeyRelatedField(many=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')'''
        
class UserSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='myuser.city')
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'px', 'py')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')