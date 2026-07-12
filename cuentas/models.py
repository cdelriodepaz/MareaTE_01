from django.db import models
from django.contrib.auth.models import AbstractUser
from comunidad.models import Parish

# Create your models here.


class ParishUser(AbstractUser):
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    parish = models.ForeignKey(Parish, null=True, blank=True, on_delete=models.CASCADE)
