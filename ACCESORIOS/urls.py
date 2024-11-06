from django.urls import path
from ACCESORIOS import views

app_name = 'ACCESORIOS'

urlpatterns = [
    path('ruedas/', views.ListadoRuedas.as_view(), name='listado_ruedas'),
    path('ruedas/crear/', views.CrearRuedas.as_view(), name='crear_ruedas')
]
