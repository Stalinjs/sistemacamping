from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página de inicio
    path('inicio/', views.inicio, name='inicio'),
    path('campista/', views.nuevo_campista, name='nuevo_campista'),
    path('listadoCampista/', views.listar_campista, name='listar_campista'),
    path('guardarCampista/', views.guardar_campista, name='guardar_campista'),
    path('eliminarCampista/<int:id>/', views.eliminar_campista, name='eliminar_campista'),  
    path('editarCampista/<int:id>/', views.editar_campista, name='editar_campista'),
    path('edicionCampista/<int:id>/', views.edicion_campista, name='edicion_campista'),

    #================RUTAS RESERVA======================
    path('reserva/', views.nuevo_reserva, name='nuevo_reserva'),
    path('listadoReserva/', views.listar_reserva, name='listar_reserva'),
    path('guardarReserva/', views.guardar_reserva, name='guardar_reserva'),
    path('eliminarReserva/<int:id>', views.eliminar_reserva, name='eliminar_reserva'),
    path('editarReserva/<int:id>/', views.editar_reserva, name='editar_reserva'),
    path('edicionReserva/<int:id>/', views.edicion_reserva, name='edicion_reserva'),



]