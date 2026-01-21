from django.db import models

class Novedad(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='novedades/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    nro_novedad = models.IntegerField(unique=True)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo
