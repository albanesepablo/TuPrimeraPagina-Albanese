from django.db import models
from django.db.models import Max

class Novedad(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='novedades/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()

    def __str__(self):
        return f"Novedad {self.nro_novedad} - {self.titulo}"
