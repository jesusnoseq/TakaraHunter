#encoding:utf-8
from django.db                  import models
from django.contrib.auth.models import User

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
                        ('Abierta',"Abierta"), 
                        ('Cerrada',"Cerrada"), 
                    )    
################################################################################
#										CLASE USUARIO
#-------------------------------------------------------------------------------
User.add_to_class('sexo', models.CharField(max_length=6, choices=SEXO, blank=True, verbose_name="Sexo", help_text="Tu sexo."))
User.add_to_class('telefono', models.PositiveIntegerField(null=True, blank=True, verbose_name="Número de teléfono", help_text="Tu número de teléfono."))
User.add_to_class('px', models.FloatField(null=True, blank=True, verbose_name="Coordenada X", help_text="Coordenada X de tu localizacion."))
User.add_to_class('py', models.FloatField(null=True, blank=True, verbose_name="Coordenada Y", help_text="Coordenada Y de tu localizacion."))
User.add_to_class('fecha_nacimiento', models.DateField(null=True, blank=True, verbose_name="Fecha de nacimiento", help_text="La fecha en que naciste."))
User.add_to_class('profesion', models.CharField(max_length=30, blank=True, verbose_name="Profesión", help_text="Tu empleo actual."))
User.add_to_class('foto', models.ImageField(upload_to='fotos_usuario', blank=True, verbose_name="Foto", help_text="Tu fotografía."))

################################################################################
#                                        CLASE RUTA
#-------------------------------------------------------------------------------
class Ruta(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Nombre", help_text="Nombre de la ruta. 100 caracteres máximo.")
    user =  models.ForeignKey(User, verbose_name="Poseedor", null=True, blank=True, editable=False)
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
#                                        CLASE TESORO
#-------------------------------------------------------------------------------
class Tesoro(models.Model):
    x = models.FloatField(verbose_name="X", help_text="Coordenada X de la ubicación del tesoro.")
    y = models.FloatField(verbose_name="Y", help_text="Coordenada Y de la ubicación del tesoro.")
    recogidoPor =  models.ForeignKey(User, null=True, blank=True, verbose_name="Recogido por", help_text="Usuario que ha recogido el tesoro.")
    def __unicode__(self):
        return u"%s - (%0.2f, %0.2f)" % (self.recogidoPor,self.x,self.y)

################################################################################
#                                        CLASE BÚSQUEDA
#-------------------------------------------------------------------------------
class Busqueda(models.Model):
    titulo = models.CharField(max_length=250, unique=True, verbose_name="Título", help_text="Título de la búsqueda. 250 caracteres máximo. Debe ser único.")
    descripcion = models.TextField(verbose_name="Descripción", help_text="Descripción de la búsqueda.")
    fecha_modificacion = models.DateTimeField(db_index=True, auto_now=True)
    participantes = models.ManyToManyField(User,blank=True,null=True)
    tesoro = models.OneToOneField(Tesoro, verbose_name="Tesoro", help_text="Tesoro que contiene la búsqueda.")
    estado = models.CharField(max_length=7, choices=ESTADOS_BUSQUEDA, default='Abierta', verbose_name="Estado", help_text="La búsqueda puede estar abierta o cerrada.")
    class Meta:
        ordering=['-fecha_modificacion']
    def __unicode__(self):
        return u"%s" % self.titulo