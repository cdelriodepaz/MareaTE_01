from django.db import models
from comunidad.models import Parish


# Create your models here.
class Project(models.Model):
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    name = models.CharField(max_length=50, verbose_name="nombre")
    date = models.DateField(blank=True, null=True)
    parish = models.ForeignKey(
        Parish, on_delete=models.CASCADE, verbose_name="parroquia"
    )
    description = models.TextField(blank=True, verbose_name="descripción")

    def __str__(self):
        return self.name


class Song(models.Model):
    class Meta:
        verbose_name = "Canción"
        verbose_name_plural = "Canciones"

    title = models.CharField(max_length=50, verbose_name="título")
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, verbose_name="proyecto"
    )
    doctrinal_guide = models.TextField(
        max_length=500, blank=True, verbose_name="guía doctrinal"
    )
    order = models.IntegerField(verbose_name="orden")

    def __str__(self):
        return self.title


class VoiceTrack(models.Model):
    class Meta:
        verbose_name = "Maqueta de voz"
        verbose_name_plural = "Maquetas de voz"

    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name="canción")
    instrument = models.CharField(max_length=50, verbose_name="instrumento/voz")
    audio_file = models.FileField(upload_to="audio/", verbose_name="archivo")

    def __str__(self):
        return f"{self.instrument} — {self.song.title}"
