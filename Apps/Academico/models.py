from django.db import models


class Asignatura(models.Model):
    codigo = models.CharField(primary_key=True,  max_length=6)
    nombre = models.CharField(max_length=100)
    unidades = models.PositiveIntegerField()
    credito_requerido = models.IntegerField()
    cantidadmax_estudiantes = models.IntegerField()
    cantidad_estudiantes = models.IntegerField()
    abierta = models.BooleanField(default=False)
    opciones_carrera = [('Industrial', 'Ingieneria Industrial'), ('Mecanica', 'Ingieneria Mecanica'),
                        ('Sistemas', 'Ingieneria Sistemas'), ('General', 'General')]
    carrera = models.CharField(
        choices=opciones_carrera, max_length=15, verbose_name=u'Carrera')

    def __str__(self):
        datos = "{0} {1} {2}"
        return datos.format(self.codigo, self.carrera, self.nombre)
