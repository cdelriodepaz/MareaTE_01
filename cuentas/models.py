from django.db import models
from django.contrib.auth.models import AbstractUser
from comunidad.models import Parish

# Create your models here.


class ParishUser(AbstractUser):
    parish = models.ForeignKey(Parish, null=True, blank=True, on_delete=models.CASCADE)
