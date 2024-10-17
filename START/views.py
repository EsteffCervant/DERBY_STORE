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
    file_template = open(r'templates\template1.html')
    template = Template(file_template.read())
    file_template.close()
    
    contexto = Context()
    
    render_template = template.render(contexto)
    
    return HttpResponse(render_template)


def template2 (request):    
    file_template = open(r'templates\template2.html')
    template = Template(file_template.read())
    file_template.close()
    
    contexto = Context()
    
    render_template = template.render(contexto)
    
    return HttpResponse(render_template)


def template3 (request):
    Fecha = datetime.now()
    
    datos = {'Fecha': Fecha    
    }
    
    template = loader.get_template('template3.html')
    render_template = template.render(datos)
    return HttpResponse(render_template)

def productos_lista(request):
    productos = Patines.objects.all()  # O puedes filtrar por ciertas condiciones
    return render(request, 'productos.html', {'productos': productos})


def productos (request, Deporte, Marca, Talla):
    patines = Patines(deporte=Deporte, marca=Marca, talla=Talla)
    patines.save()
    return render(request,'productos.html', {'patines': patines})
    
    #(request, 'inicio/productos.html', {'patines': patines})
    #return render(request,'productos.html', {})



    