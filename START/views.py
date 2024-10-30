from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render, redirect
from START.models import Patines
from START.forms import AgregarPatinesForm, BuscarPatinesForm


def vista (request):
    return HttpResponse('ROLLER SKATES')


def inicio (request):
    return render(request, 'index.html')

def template1 (request):  
    return render(request, template_name='template1.html')


def template2 (request):    
    return render(request, template_name='template2.html')


def template3 (request):
    Fecha = datetime.now()
    
    datos = {'Fecha': Fecha    
    }
    
    template = loader.get_template('template3.html')
    render_template = template.render(datos)
    return HttpResponse(render_template)


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



    