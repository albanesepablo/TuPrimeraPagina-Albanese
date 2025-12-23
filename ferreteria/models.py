from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    categoria = models.CharField(max_length=50)
    proveedor = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
