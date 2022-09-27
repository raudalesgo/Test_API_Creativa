from pydoc import cli
from django.urls import path
from .views import cliente, pelicula, renta

urlpatterns = [
    path('', pelicula.home),
    
    path('cliente/', cliente.clientes_all),
    path('cliente/add/', cliente.add_customer),
    path('cliente/<int:client_pk>/', cliente.view_customer_details),
    path('cliente/<int:client_pk>/update/', cliente.edit_customer_details),
    path('cliente/<int:client_pk>/delete/', cliente.delete_customer),

    path('pelicula/', pelicula.peliculas),
    path('pelicula/add/', pelicula.agregar_pelicula), # API 1: Add new cars
    path('pelicula/<int:pelicula_pk>/', pelicula.detalle_peliculas),
    path('pelicula/<int:pelicula_pk>/active_booking/', pelicula.detalle_renta_peliculas), # API 3: Show details of pelicula with booking details
    path('pelicula/<int:pelicula_pk>/update/', pelicula.editar_pelicula),
    path('pelicula/<int:pelicula_pk>/delete/', pelicula.eliminar_pelicula),

    path('renta/', renta.rentas_all),
    # path('renta/book/', renta.), # API 2: Book an available pelicula
    path('renta/<int:renta_pk>/', renta.ver_renta),
    # path('renta/<int:renta_pk>/extend/', renta.extend_reservation_date), # API 5: Extend date of renta.
    path('renta/<int:renta_pk>/cancel/', renta.cancelar_renta), # API 6: Cancel Specific booking

    # path('pelicula/status/', pelicula.pe) # API 4: Show cars with availability status on given date.

]