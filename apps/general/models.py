from django.db import models

# Create your models here.

class SistemaMetrico(models.Model):
    sistema = models.CharField(max_length=50)

    def __str__(self):
        return self.sistema

class Unidad(models.Model):
    unidad = models.CharField( max_length=20)
    sistema = models.ForeignKey(SistemaMetrico, on_delete=models.PROTECT)

    def __str__(self):
        return self.unidad
    
