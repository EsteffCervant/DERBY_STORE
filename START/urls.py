from django.urls import path
from START.views import (
    vista, 
    inicio, 
    template1, 
    template2, 
    template3,
    crear_patines
)
#app_name = 'START'

urlpatterns = [
    path('vista/', vista),
    path('', inicio),
    path('deportes/', template1, name='deportes'),
    path('llantas-accesorios/', template2),
    path('compra/', template3),
    path('crear-patines/<str:Deporte>/<str:Marca>/<int:Talla>/', crear_patines)
]
