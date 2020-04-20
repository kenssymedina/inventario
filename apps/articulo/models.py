from django.db import models
from apps.general.models import (SistemaMetrico, Unidad)

# Create your models here.

class CategoriaArticulo(models.Model):
    categoria = models.TextField() # por si es electrodomestico, hogar, telas etc

    def __str__(self):
        return self.categoria


class Fabricante(models.Model):
    nombre = models.TextField()
    categoria = models.ManyToManyField(CategoriaArticulo, related_name = 'fabricantes')

    def __str__(self):
        return self.nombre


class TipoArticulo(models.Model):
    tipo = models.TextField()

    def __str__(self):
        return self.tipo


class Marca(models.Model):
    nombre = models.TextField()

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    codigoArticulo = models.CharField(max_length=20, unique= True)
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoArticulo, on_delete=models.PROTECT, related_name='articulos')
    fabricante = models.ForeignKey(Fabricante, on_delete=models.PROTECT, related_name='articulos')
    upc = models.IntegerField(blank=True, null=True) # numero unico asociado al articulo, codigo de barra
    marca= models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='articulos')
    unidad = models.ForeignKey(Unidad, on_delete=models.PROTECT, related_name='articulos')
    especificaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{} --> {}'.format(self.codigoArticulo, self.nombre)


class ImagenesArticulo(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.PROTECT, related_name = 'imagenes')
    imagen = models.ImageField( upload_to="imagenArticulo", height_field=None, blank = True, null =True)

    def __str__(self):
        return '{} --> {}'.format(self.id, self.articulo)




