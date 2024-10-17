from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime


def vista (request):
    return HttpResponse('ROLLER SKATES')


def inicio (request):
    return HttpResponse('INICIO')


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