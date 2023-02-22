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
        fields = ('email','username','nombres','apellidos', 'expediente')
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
            ),
            'expediente' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su expediente'
                }
            )
        }
    def clean_password2(self):
        """
            Esta es la validacion de contraseña
            Metodo que valida que ambas contraseñas ingresadas sean igual, esto antes de ser encriptadas
            y guardadas en la base de datos, Retornar la contraseña Valida.

            Excepciones:
            -ValidationError  -- cuando las contraseñas no son iguales muestra un mensaje de error
        """

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('contraseñas no coinciden!')
        return password2 
    
    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

