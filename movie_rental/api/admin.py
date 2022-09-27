from multiprocessing.connection import Client
from django.contrib import admin
from api.models import Pelicula, Cliente, Renta

admin.site.register(Cliente)
admin.site.register(Pelicula)
admin.site.register(Renta)