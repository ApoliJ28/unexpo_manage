from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Asignatura(models.Model):
    codigo = models.CharField(primary_key=True,  max_length=5)
    nombre = models.CharField(max_length=100)
    unidades = models.PositiveIntegerField()
    credito_requerido = models.IntegerField()
    cantidadmax_estudiantes = models.IntegerField()
    cantidad_estudiantes = models.IntegerField()
    abierta = models.BooleanField(default=True)
    opciones_carrera = [('Industrial', 'Ingieneria Industrial'), ('Mecanica', 'Ingieneria Mecanica'),
                        ('Sistemas', 'Ingieneria Sistemas'), ('General', 'General')]
    carrera = models.CharField(
        choices=opciones_carrera, max_length=15, verbose_name=u'Carrera')

    def __str__(self):
        datos = "{0} {1} {2}"
        return datos.format(self.codigo, self.carrera, self.nombre)


class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')
        user = Usuario(
            username = username, 
            email = self.normalize_email(email), 
            )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, password):
        user = self.create_user(
            email,
            username = username,
            password = password
        )
        user.usuario_administrador = True
        user.save()
        return user

class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', unique = True, max_length=30)
    expediente = models.CharField('Expediente',primary_key=True, unique=True, max_length=50)
    cedula = models.CharField('Cedula', unique=True, max_length=8, blank=True, null= True)
    creditos_aprobados = models.IntegerField('Creditos Aprobados',blank=True, null= True)
    fecha_inscripcion = models.DateTimeField('Fecha de inscripcion', blank=True, null= True)
    opciones_carrera = [('Industrial', 'Ingieneria Industrial'), ('Mecanica', 'Ingieneria Mecanica'),
                        ('Sistemas', 'Ingieneria Sistemas'), ('General', 'General')]
    carrera = models.CharField('Carrera',choices=opciones_carrera, max_length=15, blank=True, null= True)
    opciones_tipo_estudiante = [('C','Completo'),('P','Parcial')]
    tipo_estudiante = models.CharField('Tipo de estudiante', choices=opciones_tipo_estudiante, max_length=15, blank=True, null= True)
    email = models.EmailField('Correo electronico', max_length=100, unique=True)
    nombres = models.CharField('Nombres', max_length=100, blank=True, null= True)
    apellidos = models.CharField('apellidos', max_length=100, blank=True, null= True)
    imagen = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=200, blank=True, null= True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'
    
    def has_perm(self, perm, ob = None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador