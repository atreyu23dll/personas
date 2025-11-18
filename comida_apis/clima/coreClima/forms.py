from django import forms

class RegistroUsuarioForm(forms.Form):
    nombre = forms.CharField(label='Nombre de usuario', max_length=100)
    email = forms.EmailField(label='Correo electrónico')


