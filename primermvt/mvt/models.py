from django.db import models
from datetime import datetime, date


class Familia(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Parentesco = models.CharField(max_length=50)
    Edad = models.IntegerField()
    FechaDeNacimiento = models.DateField(auto_created=False, auto_now=False, blank=True)
