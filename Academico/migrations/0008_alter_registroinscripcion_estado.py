# Generated by Django 4.1.7 on 2023-03-02 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0007_alter_registroinscripcion_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroinscripcion',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('pagado', 'Pagado'), ('inscrito', 'Inscrito')], default='pendiente', max_length=15),
        ),
    ]
