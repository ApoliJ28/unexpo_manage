from django.db import models

# Create your models here.


class Asignatura(models.Model):
    Codigo = models.IntegerField(primary_key=True, unique=True)
    Nombre = models.CharField(max_length=100)
    Especialidad = models.CharField(max_length=100)
    Unidades = models.IntegerField()
    CantidadMax = models.IntegerField()
    Abierta = models.BooleanField(default=False)
    Unidades = models.IntegerField()

    # Para que lo podemos visualizar en el administrardoe

    def __str__(self):
        return self.Nombre + " su cargo es  " + self.Especialidad

# class Usuario(AbstractUser):
#     CHOICES = [('Mujer', 'Mujer'), ('Hombre', 'Hombre'),
#                ('PN', 'Prefiero no contestar')]

#     genero = models.CharField(choices=CHOICES, max_length=15,
#                               verbose_name=u"Género")
#     fecha_nacimiento = models.DateField(verbose_name=u"Fecha Nac.")
#     foto = models.FileField(
#         upload_to='video', max_length=500, verbose_name=u"Foto")
# # class Usuario(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.PROTECT)
# #     id = models.AutoField(primary_key=True, verbose_name=u"ID")
# #     email = models.EmailField(max_length=50, verbose_name=u"ID")
# #     email = models.EmailField(max_length=50, verbose_name=u"ID")
# #     opciones = [('Mujer', 'Mujer'), ('Hombre', 'Hombre'),
# #                 ('PN', 'Prefiero no decirlo')]
# #     genero = models.CharField(
# #         choices=opciones, max_length=15, verbose_name=u'Genero')
# #     opciones_carrera = [('In', 'Ingieneria Industrial'), ('Mec', 'Ingieneria Mecanica'),
# #                         ('Sis', 'Ingieneria Sistemas')]
# #     carrera = models.CharField(
# #         choices=opciones_carrera, max_length=15, verbose_name=u'Carrera')

# #     def __unicode__(self):
# #         return self.user.username
