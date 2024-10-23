from django.urls import path
from START.views import (vista, inicio, template1, template2, template3, crear_patines)


urlpatterns = [
    path('vista/', vista, name='vista'),
    path('', inicio, name='inicio'),
    path('deportes/', template1, name='deportes'),
    path('llantas-accesorios/', template2, name='accesorios'),
    path('compra/', template3, name='compra'),
    path('crear-patines/<str:Deporte>/<str:Marca>/<int:Talla>/', crear_patines, name='crear_patines')
]
