from django.contrib import admin
from .models import Materia, Usuario, Departamento, Carrera, RegistroInscripcion, RegistroPago

# Register your models here.


class FiltroAsignatura(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'abierta', 'carrera')
    search_fields = ('codigo', 'nombre', 'abierta', 'carrera')
    list_filter = ('carrera', 'codigo', 'abierta')


admin.site.register(Materia, FiltroAsignatura)

admin.site.register(Usuario)
admin.site.register(Departamento)
admin.site.register(Carrera)
admin.site.register(RegistroInscripcion)
admin.site.register(RegistroPago)
