from django.urls import path
from START.views import (
    vista, 
    inicio, 
    template1, 
    template2, 
    template3, 
    crear_patines, 
    about_me, 
    buscar_patines, 
    ver_patines, 
    eliminar_patines, 
    editar_patines)


urlpatterns = [
    path('vista/', vista, name='vista'),
    path('', inicio, name='inicio'),
    path('deportes/', template1, name='deportes'),
    path('llantas-accesorios/', template2, name='accesorios'),
    path('compra/', template3, name='compra'),
    path('crear-patines/<str:Deporte>/<str:Marca>/<int:Talla>/', crear_patines, name='crear_patines'),
    path('buscar-patines/', buscar_patines, name='buscar_patines'),
    path('crear-patines/', crear_patines, name='crear_patines'),
    path('ver-patines/<int:id>/', ver_patines, name='ver_patines'),
    path('eliminar-patines/<int:id>/', eliminar_patines, name='eliminar_patines'),
    path('editar-patines/<int:id>/', editar_patines, name='editar_patines'),
    path('about-me/', about_me, name='about_me')
]
