#encoding:utf-8
from django.db                  import models
from django.contrib.auth.models import User
#https://docs.djangoproject.com/en/dev/ref/contrib/gis/model-api/#pointfield
#from django.contrib.gis.db import models

################################################################################
#										TIPOS DE DATOS
#-------------------------------------------------------------------------------
SEXO = (
            ('Hombre', 'Hombre'),
            ('Mujer', 'Mujer'),
       )
MODE_CHOICES = (
                    ('DRIVING','Coche'),
                    ('WALKING','A pie'),
                    ('BICYCLING','Bicicleta'),
                    ('TRANSIT','Transporte público'),
                )
################################################################################
#										CLASE USUARIO
#-------------------------------------------------------------------------------
# Atributos obligatorios de usuario
#
# NOMBRE Y APELLIDO - Ya incluidos en la clase User por defecto
#                     Son first_name y last_name
# SEXO
User.add_to_class('sexo', models.CharField(max_length=6, choices=SEXO, blank=True, verbose_name="Sexo", help_text="Tu sexo."))
# TELEFONO
User.add_to_class('telefono', models.PositiveIntegerField(null=True, blank=True, verbose_name="Número de teléfono", help_text="Tu número de teléfono."))
# DIRECCION (Debería ser una dirección escrita o una coordenada de un mapa?)
#Hay que añadir el lugar donde viven( coordenada X e Y como dos floats ) 
User.add_to_class('px', models.FloatField(null=True, blank=True, verbose_name="Coordenada X", help_text="Coordenada X de tu localizacion."))
User.add_to_class('py', models.FloatField(null=True, blank=True, verbose_name="Coordenada Y", help_text="Coordenada Y de tu localizacion."))
# FECHA DE NACIMIENTO
User.add_to_class('fecha_nacimiento', models.DateField(null=True, blank=True, verbose_name="Fecha de nacimiento", help_text="La fecha en que naciste."))
# PROFESION
User.add_to_class('profesion', models.CharField(max_length=30, blank=True, verbose_name="Profesión", help_text="Tu empleo actual."))
# FOTO
User.add_to_class('foto', models.ImageField(upload_to='fotos_usuario', blank=True, verbose_name="Foto", help_text="Tu fotografía."))

################################################################################
#                                        CLASE RUTA
#-------------------------------------------------------------------------------
class Ruta(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Nombre", help_text="Nombre de la ruta. 100 caracteres máximo.")
    user =  models.ForeignKey(User, verbose_name="Poseedor", null=True, blank=True, editable=False)
    origen = models.CharField(max_length = 100, verbose_name="Origen", help_text="Origen de la ruta. 100 caracteres máximo.")
    destino = models.CharField(max_length = 100, verbose_name="Destino", help_text="Destino de la ruta. 100 caracteres máximo.")
    modo = models.CharField(max_length = 10, verbose_name="Modo", choices=MODE_CHOICES, help_text="Modo o medio de transporte de la ruta.")
    fecha_modificacion = models.DateTimeField(db_index=True, auto_now=True)
    class Meta:
        ordering=['-fecha_modificacion']
    def __unicode__(self):
        return u"%s" % self.titulo

################################################################################
#                                        CLASE BÚSQUEDA
#-------------------------------------------------------------------------------
class Busqueda(models.Model):
    slug = models.SlugField(blank=False,unique=True)
    titulo = models.CharField(max_length=250,unique=True)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now=True)
    participantes = models.ManyToManyField(User,blank=True,null=True) 

    def __unicode__(self):
        return u"%s" % self.titulo

################################################################################
#                                        CLASE TESORO
#-------------------------------------------------------------------------------
class Tesoro(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    busqueda = models.ForeignKey(Busqueda)
    fecha_recogida = models.DateTimeField(auto_now=True)
    recogidaPor =  models.ForeignKey(User,null=True)
    def __unicode__(self):
        return u"%s - (%0.2f, %0.2f)" % (self.busqueda.titulo,self.x,self.y)
    
#return u"%s apuesta en %s: %ium a la opcion (%s)" % (self.user.username, self.apuesta, self.cantidad,self.opcion)
# mejor ponerlo como una relacion muchos a muchos en busqueda
#class Participa(models.Model):
#    busqueda = models.ForeignKey(Busqueda)
#    participante =  models.ForeignKey(User)
    