# Generated by Django 4.1.3 on 2023-02-20 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0002_alter_asignatura_abierta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='codigo',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]