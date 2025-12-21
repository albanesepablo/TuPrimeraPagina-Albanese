from django.db import models

class Sector(models.Model):
    nombre = models.CharField(max_length=50)
    nro_sector = models.IntegerField(unique=True)
    nro_empleados = models.IntegerField(null=True)
    fecha_de_creacion = models.DateField(auto_now_add=True)
    email_sector = models.EmailField()

    def __str__(self):
        return f'Nombre: {self.nombre} / Nro de sector: {self.nro_sector}'