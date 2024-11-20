from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import FormularioDeCreacionDeUsuario, FormularioEdicionPerfil, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtra, UserProfile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            
            django_login(request, usuario)
            
            DatosExtra.objects.get_or_create(user=usuario)
            return redirect('inicio')
            
    return render(request, 'usuarios/login.html', {'form': formulario})


def register(request):
    
    formulario = FormularioDeCreacionDeUsuario()
    if request.method == 'POST':
        formulario = FormularioDeCreacionDeUsuario(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('usuarios:login')
    
    return render(request, 'usuarios/register.html', {'form': formulario})

@login_required
def editar_perfil(request):
    datos_extra = request.user.datosextra
    formulario = FormularioEdicionPerfil(instance=request.user, initial={'avatar': datos_extra.avatar})
    
    if request.method == 'POST':
        formulario = FormularioEdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            new_avatar = formulario.cleaned_data.get('avatar')
            datos_extra.avatar = new_avatar if new_avatar else datos_extra.avatar
            datos_extra.save()
            
            formulario.save()
            
            return redirect('inicio')
    
    return render(request, 'usuarios/editar_perfil.html', {'form': formulario})


class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_password.html'
    success_url = reverse_lazy('usuarios:editar_perfil')  ##cambiar redirigirse a profile.html####
    

@login_required
def profile(request):
    profile = request.user.get_or_create_profile()
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        password_form = PasswordChangeForm(request.user, request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Mantener la sesión tras cambiar la contraseña
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        password_form = PasswordChangeForm(request.user)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'password_form': password_form,
    }
    return render(request, 'profile.html', {'profile': profile})
    