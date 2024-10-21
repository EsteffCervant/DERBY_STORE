from django.urls import path
from START.views import (
    vista, 
    inicio, 
    template1, 
    template2, 
    template3,
    crear_patines,
)

urlpatterns = [
    path('vista/', vista),
    path('', inicio),
    path('deportes/', template1),
    path('llantas-accesorios/', template2),
    path('compra/', template3),
    path('creacion-patines/', crear_patines)
]
