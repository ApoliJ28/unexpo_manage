# Generated by Django 4.1.3 on 2023-02-22 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0003_alter_asignatura_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Nombre de usuario')),
                ('expediente', models.CharField(max_length=10, unique=True, verbose_name='Expediente')),
                ('cedula', models.CharField(blank=True, max_length=8, null=True, unique=True, verbose_name='Cedula')),
                ('creditos_aprobados', models.IntegerField(blank=True, null=True, verbose_name='Creditos Aprobados')),
                ('fecha_inscripcion', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de inscripcion')),
                ('carrera', models.CharField(blank=True, choices=[('Industrial', 'Ingieneria Industrial'), ('Mecanica', 'Ingieneria Mecanica'), ('Sistemas', 'Ingieneria Sistemas'), ('General', 'General')], max_length=15, null=True, verbose_name='Carrera')),
                ('tipo_estudiante', models.CharField(blank=True, choices=[('C', 'Completo'), ('P', 'Parcial')], max_length=15, null=True, verbose_name='Tipo de estudiante')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Correo electronico')),
                ('nombres', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombres')),
                ('apellidos', models.CharField(blank=True, max_length=100, null=True, verbose_name='apellidos')),
                ('imagen', models.ImageField(blank=True, max_length=200, null=True, upload_to='perfil/', verbose_name='Imagen de perfil')),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_administrador', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
