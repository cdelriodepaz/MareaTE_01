from django.db import models


# Create your models here.
class Parroquia(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField(max_length=400)
    direccion_iglesia = models.CharField(max_length=80)
    direccion_oficina = models.CharField(max_length=80, blank=True)
    telefono = models.CharField(max_length=12)
    email = models.EmailField(blank=True)
    horario_misas = models.TextField()
    sello_credencial = models.BooleanField(default=False)
    info_peregrinos = models.TextField(blank=True)
    slug = models.SlugField()
    logotipo = models.ImageField(blank=True)
    activa = models.BooleanField(default=True)
    color_primario = models.CharField(max_length=7)

    def __str__(self):
        return self.nombre
