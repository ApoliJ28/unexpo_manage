from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Carrera(models.Model):
    codigo_c = models.CharField(primary_key=True,  max_length=5)
    nombre = models.CharField(max_length=100)
    costo = models.FloatField()

    def __str__(self):
        return f'{self.nombre} {self.costo}'


class Departamento(models.Model):
    codigo_dep = models.CharField(primary_key=True,  max_length=5)
    nombre = models.CharField(max_length=100)
    carrera_ids = models.ManyToManyField(Carrera, "Carreras")

    def __str__(self):
        return f'{self.nombre}'


class Materia(models.Model):
    codigo = models.CharField(primary_key=True,  max_length=5)
    nombre = models.CharField(max_length=100)
    creditos = models.PositiveIntegerField()
    creditos_requerido = models.IntegerField()
    departamento_id = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    opciones_semestres = [(1, 'Semestre 1'), (2, 'Semestre 2'), (3, 'Semestre 3'),
                          (4, 'Semestre 4'), (5, 'Semestre 5'), (6, 'Semestre 6'),
                          (7, 'Semestre 7'), (8, 'Semestre 8'), (9, 'Semestre 9'), (10, 'Semestre 10')]
    semestre = models.IntegerField(
        choices=opciones_semestres, blank=True, null=True)
    # cantidadmax_estudiantes = models.IntegerField()
    # cantidad_estudiantes = models.IntegerField()
    abierta = models.BooleanField(default=True)
    opciones_carrera = [('Industrial', 'Ingieneria Industrial'), ('Mecanica', 'Ingieneria Mecanica'),
                        ('Sistemas', 'Ingieneria Sistemas'), ('General', 'General')]
    carrera = models.CharField(
        choices=opciones_carrera, max_length=15, verbose_name=u'Carrera')

    def __str__(self):
        datos = "{0} {1} {2}"
        return datos.format(self.codigo, self.carrera, self.nombre)


class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, expediente, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            expediente=expediente,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, expediente, password):
        user = self.create_user(
            email,
            username=username,
            password=password,
            expediente=expediente,
        )
        user.usuario_administrador = True
        user.save()
        return user


class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(
        'Nombre de usuario', unique=True, max_length=30)
    expediente = models.CharField('Expediente', unique=True, max_length=10)
    cedula = models.CharField('Cedula', unique=True,
                              max_length=8, blank=True, null=True)
    creditos_aprobados = models.IntegerField(
        'Creditos Aprobados', blank=True, null=True)
    carrera_id = models.ForeignKey(
        Carrera, null=True, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(
        'Fecha de inscripcion', blank=True, null=True)

    opciones_tipo_estudiante = [('C', 'Completo'), ('P', 'Parcial')]
    tipo_estudiante = models.CharField(
        'Tipo de estudiante', choices=opciones_tipo_estudiante, max_length=15, blank=True, null=True)
    opciones_semestres = [(1, 'Semestre 1'), (2, 'Semestre 2'), (3, 'Semestre 3'),
                          (4, 'Semestre 4'), (5, 'Semestre 5'), (6, 'Semestre 6'),
                          (7, 'Semestre 7'), (8, 'Semestre 8'), (9, 'Semestre 9'), (10, 'Semestre 10')]
    semestre = models.IntegerField(
        choices=opciones_semestres, blank=True, null=True)
    email = models.EmailField('Correo electronico',
                              max_length=100, unique=True)
    nombres = models.CharField(
        'Nombres', max_length=100, blank=True, null=True)
    apellidos = models.CharField(
        'apellidos', max_length=100, blank=True, null=True)
    imagen = models.ImageField(
        'Imagen de perfil', upload_to='perfil/', max_length=200, blank=True, null=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'expediente']

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador


class RegistroPago(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_pago = models.DateTimeField()
    estudiante_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    registro_inscripcion = models.IntegerField()
    cantidad_pago = models.FloatField()

    def __str__(self):
        return f'Registro: {self.id} Estudiante: {self.estudiante_id} Inscripcion: {self.registro_inscripcion}'


class RegistroInscripcion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_apertura = models.DateTimeField()
    estudiante_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    materias_ids = models.ManyToManyField(Materia, blank=True)
    fecha_inscripcion = models.DateTimeField(null=True, blank=True)
    pago_id = models.OneToOneField(
        RegistroPago, on_delete=models.CASCADE, null=True, blank=True)
    estados = [("pendiente", "Pendiente"),
               ("pago", "Estado de pago"), ("inscrito", "Inscrito")]
    estado = models.CharField(
        choices=estados, max_length=15, default="pendiente")

    def __str__(self):
        return f'Registro: {self.id} Estudiante: {self.estudiante_id} Materias: {self.materias_ids}'
