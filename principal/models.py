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
ESTADOS_BUSQUEDA = (
                        ('a',"Abierta"), 
                        ('c',"Cerrada"), 
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
    #origen = models.CharField(max_length = 100, verbose_name="Origen", help_text="Origen de la ruta. 100 caracteres máximo.")
    #destino = models.CharField(max_length = 100, verbose_name="Destino", help_text="Destino de la ruta. 100 caracteres máximo.")
    origen_x = models.FloatField(verbose_name="Origen - Coordenada X", help_text="Coordenada X del origen de la ruta.")
    origen_y = models.FloatField(verbose_name="Origen - Coordenada Y", help_text="Coordenada Y del origen de la ruta.")
    destino_x = models.FloatField(verbose_name="Destino - Coordenada X", help_text="Coordenada X del destino de la ruta.")
    destino_y = models.FloatField(verbose_name="Destino - Coordenada Y", help_text="Coordenada Y del destino de la ruta.")
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
    slug = models.SlugField(blank=False, unique=True, verbose_name="Slug", help_text="Slug de la búsqueda.")
    titulo = models.CharField(max_length=250, unique=True, verbose_name="Título", help_text="Título de la búsqueda. 250 caracteres máximo. Debe ser único.")
    descripcion = models.TextField(verbose_name="Descripción", help_text="Descripción de la búsqueda.")
    fecha_modificacion = models.DateTimeField(db_index=True, auto_now=True)
    participantes = models.ManyToManyField(User,blank=True,null=True)
    estado = models.CharField(max_length=1, choices=ESTADOS_BUSQUEDA, default='a', verbose_name="Estado", help_text="La búsqueda puede estar abierta o cerrada.")
    class Meta:
        ordering=['-fecha_modificacion']
    def __unicode__(self):
        return u"%s" % self.titulo
    def as_json(self):
        #print self.participantes
        
        return dict(
            slug=self.slug,
            titulo=self.titulo,
            descripcion=self.descripcion,
            fecha_modificacion=self.fecha_modificacion.isoformat(),
            participantes='',
            estado=self.estado)

################################################################################
#                                        CLASE TESORO
#-------------------------------------------------------------------------------
class Tesoro(models.Model):
    x = models.FloatField(verbose_name="X", help_text="Coordenada X de la ubicación del tesoro.")
    y = models.FloatField(verbose_name="Y", help_text="Coordenada Y de la ubicación del tesoro.")
    busqueda = models.ForeignKey(Busqueda, verbose_name="Búsqueda", help_text="Búsqueda a la que pertenece el tesoro.")
    fecha_recogida = models.DateTimeField(auto_now=True)
    recogidaPor =  models.ForeignKey(User, null=True, blank=True, verbose_name="Recogido por", help_text="Usuario que ha recogido el tesoro.")
    def __unicode__(self):
        return u"%s - (%0.2f, %0.2f)" % (self.busqueda.titulo,self.x,self.y)
    
#return u"%s apuesta en %s: %ium a la opcion (%s)" % (self.user.username, self.apuesta, self.cantidad,self.opcion)
# mejor ponerlo como una relacion muchos a muchos en busqueda
#class Participa(models.Model):
#    busqueda = models.ForeignKey(Busqueda)
#    participante =  models.ForeignKey(User)
    