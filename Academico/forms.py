from django.forms import ModelForm
from django import forms
from .models import Asignatura, Usuario

#FORMULARIO PARA EL REGISTRO DE LAS ASIGNATURAS
class AsignaturaForm(ModelForm):
    class Meta:
        model = Asignatura
        # Creamos los campos a  traves del formulario
        fields = '__all__'


#FORMULARIO PARA EL REGISTRO DE USARIOS
class FormularioUsuario(forms.ModelForm):
    """     Formulario de Registro de un usuario en la base de datos
        Variables:

            -password1: Contraseña
            -password2: Verificacion de Contraseña
    """

    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder': 'Ingrese la Contraseña...',
            'id' : 'password1',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label= 'Contraseña de confirmación', widget= forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder': 'Ingrese la Contraseña...',
            'id' : 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'email' : forms.EmailInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Correo Electronico'
                }
            ),
            'nombres' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese sus nombres'
                }
            ),
            'apellidos' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese sus apellidos'
                }
            ),
            'username' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su usuario'
                }
            )
        }