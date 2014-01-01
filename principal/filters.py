#encoding:utf-8

from rest_framework import filters
import django_filters
from django.contrib.auth.models import User
from models import *

class BusquedaFilter(django_filters.FilterSet):
    class Meta:
        model = Busqueda
        fields = ['slug','estado','participantes']

class TesoroFilter(django_filters.FilterSet):
    class Meta:
        model = Tesoro
        fields = ['busqueda','recogidaPor']    
        
        
class UsernameFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username']

'''

class hIsOwnerFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(name="price", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price", lookup_type='lte')
    class Meta:
        model = Product
        fields = ['category', 'in_stock', 'min_price', 'max_price']
        class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['category', 'in_stock', 'manufacturer__name`]
        
class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(name="price", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price", lookup_type='lte')
    class Meta:
        model = Product
        fields = ['category', 'in_stock', 'min_price', 'max_price']
        
        '''


#class UsernameFilter(filters.BaseFilterBackend):
#    name = django_filters.CharFilter(name="name",lookup_type="icontains")
#
#    class Meta:
#        model = Card
#        fields = ['name']