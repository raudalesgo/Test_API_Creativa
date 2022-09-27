from collections import namedtuple
from datetime import datetime, date
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from api.forms import PeliculaForm 

from api.models import Pelicula, Renta
from api.serializers import (PeliculaSerializer)


@api_view(['GET'])
def home(request):

    if request.method == 'GET':
        data = [{'message':'Bienvenido a la renta de Peliculas'}]
        # return JsonResponse(data, safe=False)
        return render(data, 'templates/show.html')


@api_view(['GET'])
def peliculas(request):

    if request.method == 'GET':
        peliculas = Pelicula.objects.all()
        serializer = PeliculaSerializer(peliculas, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def detalle_peliculas(request, pelicula_pk):

    try:
        peliculas = Pelicula.objects.get(pk=pelicula_pk)
    except Pelicula.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PeliculaSerializer(peliculas)
        return Response(serializer.data)


@api_view(['GET'])
def detalle_renta_peliculas(request, pelicula_pk):

    try:
        peliculas = Pelicula.objects.get(pk=pelicula_pk)
    except Pelicula.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        fecha_actual = date.today()
        Pelicula_detalle = namedtuple('Pelicula_detalle',('pelicula','rentas_actual'))

        # Conditions for filtering only currently active bookings of a particular car
        # suffix "__gte" stands for Greater Than or Equal to.
        condition_1 = Q(dia_renta__gte=fecha_actual)
        condition_2 = Q(dia_devolucion__gte=fecha_actual)

        pelicula_detalle = Pelicula_detalle(
            car = peliculas,
            current_active_bookings = Renta.objects.filter(car=pelicula_pk).filter(condition_1 | condition_2),
        )
        serializer = Pelicula_detalle(pelicula_detalle)
        return Response(serializer.data)


@api_view(['POST'])
def agregar_pelicula(request):

    if request.method == 'POST':
        serializer = PeliculaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def editar_pelicula(request, pelicula_pk):

    try:
        peliculas = Pelicula.objects.get(pk=pelicula_pk)
    except Pelicula.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PeliculaSerializer(peliculas, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def eliminar_pelicula(request, pelicula_pk):

    try:
        peliculas = Pelicula.objects.get(pk=pelicula_pk)
    except Pelicula.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        peliculas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


