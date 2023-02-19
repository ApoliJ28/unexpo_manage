from django.contrib import admin
from .models import Asignatura, User
# Register your models here.
# Permite añadir los modelos al panale de administradorr
admin.site.register(Asignatura)
admin.site.register(User)
# SuperUsuario
# User: admin1
# password: 1234@
