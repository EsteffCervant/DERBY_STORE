from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render, redirect
from START.models import Patines
from START.forms import AgregarPatinesForm, BuscarPatinesForm, EditarPatinesForm
from django.contrib.auth.decorators import login_required


def vista (request):
    return HttpResponse('ROLLER SKATES')


def inicio (request):
    return render(request, 'index.html')

def template1 (request):  
    return render(request, template_name='template1.html')


def template2 (request):    
    return render(request, template_name='template2.html')


def crear_patines (request, Deporte, Marca, Talla):
    patines=Patines(Deporte=Deporte, Marca=Marca, Talla=Talla)
    patines.save()
    return render(request, 'creacion_patines.html', {'patines': patines})


def about_me (request):  
    return render(request, template_name='about_me.html')


def crear_patines (request, Deporte, Marca, Talla):
    patines=Patines(Deporte=Deporte, Marca=Marca, Talla=Talla)
    patines.save()
    return render(request, 'creacion_patines.html', {'patines': patines})


def buscar_patines (request):
    formulario = BuscarPatinesForm(request.GET)
    if formulario.is_valid():
        Deporte = formulario.cleaned_data.get('Deporte')
        patiness = Patines.objects.filter(Deporte__icontains=Deporte)

    return render(request, 'buscar_patines.html', {'patiness': patiness, 'formulario': formulario})


def crear_patines (request):
    formulario = AgregarPatinesForm()
    
    if request.method == 'POST':
        
        formulario = AgregarPatinesForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            patines=Patines(Deporte=data.get('Deporte'), Marca=data.get('Marca'), Talla=data.get('Talla'))
            patines.save()
            return redirect('buscar_patines')
        
    return render(request, 'crear_patines.html', {'form': formulario})


def ver_patines (request, id):
    patines = Patines.objects.get(id=id)
    return render(request, 'ver_patines.html', {'patines': patines})

@login_required
def eliminar_patines (request, id):
    patines = Patines.objects.get(id=id)
    patines.delete()
    return redirect('buscar_patines')

@login_required
def editar_patines (request, id):
    patines = Patines.objects.get(id=id)
    
    formulario = EditarPatinesForm(initial={'Deporte': patines.Deporte, 'Marca': patines.Marca, 'Talla': patines.Talla})
    
    if request.method == 'POST':
        formulario = EditarPatinesForm(request.POST)
        if formulario.is_valid():
            patines.Deporte = formulario.cleaned_data.get('Deporte')
            patines.Marca = formulario.cleaned_data.get('Marca')
            patines.Talla = formulario.cleaned_data.get('Talla')
            
            patines.save()
            return redirect ('buscar_patines')
    
    return render(request, 'editar_patines.html', {'patines': patines, 'form': formulario})