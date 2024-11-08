from django.urls import path
from ACCESORIOS import views

app_name = 'ACCESORIOS'

urlpatterns = [
    path('ruedas/', views.ListadoRuedas.as_view(), name='listado_ruedas'),
    path('ruedas/crear/', views.CrearRuedas.as_view(), name='crear_ruedas'),
    path('ruedas/<int:pk>/', views.VerRuedas.as_view(), name='ver_ruedas'),
    path('ruedas/<int:pk>/editar/', views.EditarRuedas.as_view(), name='editar_ruedas'),
    path('ruedas/<int:pk>/eliminar/', views.EliminarRuedas.as_view(), name='eliminar_ruedas'),
]