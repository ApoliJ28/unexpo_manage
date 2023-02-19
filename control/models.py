from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.



class Asignatura(models.Model):
    Codigo = models.IntegerField(primary_key=True, unique=True)
    Nombre = models.CharField(max_length=100,unique=True)
    Especialidad = models.CharField(max_length=100)
    Unidades = models.IntegerField()
    CantidadMax = models.IntegerField()
    Abierta = models.BooleanField(default=False)
    

  #Visualizacion de Alumno y especialidad

    def __str__(self):
        return self.Nombre + " su cargo es  " + self.Especialidad


# Create your models here.


class User(AbstractUser):
    id = models.AutoField(primary_key=True, verbose_name=u"ID")
    opciones_carrera = [('In', 'Ingieneria Industrial'), ('Mec', 'Ingieneria Mecanica'),
                        ('Sis', 'Ingieneria Sistemas')]
    carrera = models.CharField(
        choices=opciones_carrera, max_length=15, verbose_name=u'Carrera')
    # opciones_modalidad = [('P', 'Parcial'), ('C', 'Completo')]
    # TipoEstudiante = models.CharField(
    #     choices=opciones_modalidad, max_length=15, verbose_name=u'Estudiante')

    def __str__(self):
        return self.user.username + " " + self.carrera
