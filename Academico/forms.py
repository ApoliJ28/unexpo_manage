from django.forms import ModelForm
# Creamos un formulario a traves de modelo
from .models import Asignatura

# Creamos el modelo de la


class AsignaturaForm(ModelForm):
    class Meta:
        model = Asignatura
        # Creamos los campos a  traves del formulario
        fields = '__all__'