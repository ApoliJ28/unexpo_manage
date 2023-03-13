# Generated by Django 4.1.6 on 2023-03-01 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0006_alter_registroinscripcion_fecha_inscripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroinscripcion',
            name='estado',
            field=models.CharField(choices=[('inscribiendo', 'Inscribiendo'), ('pago', 'Pago'), ('inscrito', 'Inscrito')], default='inscribiendo', max_length=15),
        ),
    ]