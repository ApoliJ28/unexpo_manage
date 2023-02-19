from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class UsuarioModelForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'genero', 'carrera')
