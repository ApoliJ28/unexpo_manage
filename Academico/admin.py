from django.contrib import admin
from .models import Asignatura, Usuario

# Register your models here.


class FiltroAsignatura(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'abierta', 'carrera')
    search_fields = ('codigo', 'nombre', 'abierta', 'carrera')
    list_filter = ('carrera', 'codigo', 'abierta')


admin.site.register(Asignatura, FiltroAsignatura)

admin.site.register(Usuario)
