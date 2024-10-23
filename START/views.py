from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render
from START.models import Patines
#from inicio.forms import CrearAutoFormulario, BuscarAutoFormulario, EditarAutoFormulario


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



    