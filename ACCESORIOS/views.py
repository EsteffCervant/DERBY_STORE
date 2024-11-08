from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from ACCESORIOS.models import ruedas
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class CrearRuedas(CreateView):
    model = ruedas
    template_name = 'accesorios/crear_ruedas.html'
    success_url = reverse_lazy('ACCESORIOS:listado_ruedas')
    fields = ['Dureza', 'Perfil', 'Compuesto', 'Talla']
    
    
class ListadoRuedas(ListView):
    model = ruedas
    template_name = 'accesorios/listado_ruedas.html'
    context_object_name = 'ruedas'
    
    
class VerRuedas(LoginRequiredMixin, DetailView):
    model = ruedas
    template_name = 'accesorios/ver_ruedas.html'


class EditarRuedas(LoginRequiredMixin, UpdateView):
    model = ruedas
    template_name = "accesorios/editar_ruedas.html"
    success_url = reverse_lazy('accesorios:listado_ruedas')
    fields = ['Dureza', 'Perfil', 'Compuesto', 'Talla']
    
    
class EliminarRuedas(DeleteView):
    model = ruedas
    template_name = "accesorios/eliminar_ruedas.html"
    success_url = reverse_lazy('accesorios:listado_ruedas')
    