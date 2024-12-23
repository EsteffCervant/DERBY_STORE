from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from usuarios.models import DatosExtra, UserProfile


class FormularioDeCreacionDeUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contrasenia', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    
    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name', 'password1', 'password2']
        help_texts = {key: '' for key in fields}

        
class FormularioEdicionPerfil(UserChangeForm):
    email = forms.EmailField(label='Correo electrónico')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(label='Avatar', required=False)
    password = None

    class Meta:
        model = DatosExtra
        fields = ['email', 'first_name', 'last_name', 'avatar']
        
        
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo', 'bio']