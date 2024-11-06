from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from ACCESORIOS.models import ruedas
from django.urls import reverse_lazy


class CrearRuedas(CreateView):
    model = ruedas
    template_name = 'accesorios/crear_ruedas.html'
    success_url = reverse_lazy('accesorios:listado_ruedas')
    fields = ['Dureza', 'Perfil', 'Compuesto', 'Talla']
    
    
class ListadoRuedas(ListView):
    model = ruedas
    template_name = 'accesorios/listado_ruedas.html'
    context_object_name = 'ruedas'
    