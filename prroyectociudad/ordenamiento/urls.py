"""
    Manejo de urls para la aplicación
    ordenamiento
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('barrios', views.barrios, name='barrios'),
    path('crear/parroquia', views.crear_Parroquia, 
        name='crear_Parroquia'),
    path('crear/barrio/barrio/parroquia/<int:id>', 
            views.crearBarrioParr, name='crearBarrioParr'),
    path('editar_parroquia/<int:id>', views.editar_parroquia, 
            name='editar_parroquia'),
    path('editar_barrio/<int:id>', views.editar_barrio, 
            name='editar_barrio'),
]