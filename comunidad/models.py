from django.db import models


# Create your models here.
class Parish(models.Model):
    name = models.CharField(max_length=60, verbose_name="nombre")
    description = models.TextField(max_length=400, verbose_name="descripción")
    church_dir = models.CharField(max_length=80, verbose_name="dirección iglesia")
    office_dir = models.CharField(
        max_length=80, blank=True, verbose_name="dirección oficina"
    )
    phone = models.CharField(max_length=12, verbose_name="teléfono")
    email = models.EmailField(blank=True)
    mass_schedule = models.TextField(verbose_name="horario misas")
    pilgrim_stamp = models.BooleanField(default=False, verbose_name="sello peregrinos")
    pilgrim_info = models.TextField(blank=True, verbose_name="información peregrinos")
    slug = models.SlugField()
    logo = models.ImageField(blank=True)
    active = models.BooleanField(default=True, verbose_name="activa")
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name
