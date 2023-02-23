from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models import F, Sum, FloatField


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
    fecha_inscripcion = models.DateTimeField(
        'Fecha de inscripcion', blank=True, null=True)
    opciones_carrera = [('Industrial', 'Ingieneria Industrial'), ('Mecanica', 'Ingieneria Mecanica'),
                        ('Sistemas', 'Ingieneria Sistemas')]
    carrera = models.CharField(
        'Carrera', choices=opciones_carrera, max_length=15, blank=True, null=True)
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
        return f'{self.nombres},{self.apellidos}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador


class Pedido(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            unidadestotales=Sum(F("cantidad"), outpu_field=FloatField())

        )["total"]

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']


class LineaPedido(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    codigo = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} inscribio {self.asignatura_id.nombre}'

    class Meta:
        db_table = 'lineapedidos'
        verbose_name = 'lineapedido'
        verbose_name_plural = 'lineapedidos'
        ordering = ['id']
