import json
from datetime import date
from urllib import response

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from api.models import Renta
from api.serializers import RentaSerializer


@api_view(['GET'])
def rentas_all(request):

    if request.method == 'GET':
        rentas = Renta.objects.all()
        serializer = RentaSerializer(rentas, many=True)
        return Response(serializer.data)
    
    def rentas(request):
        rentas = Renta.objects.all()
        data = [rentas.get_data() for renta in rentas]
        response = {'data': data}
        return JsonResponse(response)


@api_view(['GET'])
def ver_renta(request, renta_pk):

    try:
        reservation = Renta.objects.get(pk=renta_pk)
    except Renta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RentaSerializer(reservation)
        return Response(serializer.data)


# @api_view(['POST'])
# def book_car(request):
#     """
#     API endpoint for booking an available car.
#     """
#     if request.method == 'POST':
#         serializer = RentaSerializer(data=request.data)
            
#         if serializer.is_valid():
#             current_date = date.today()
#             issue_date = serializer.validated_data['issue_date']
#             return_date = serializer.validated_data['return_date']

#             car = serializer.validated_data['car']
#             rentas = Renta.objects.all().filter(car=car.id)

#             # Check if the issue_date of new reservation doesn't clash with any previous rentas
#             for r in rentas:
#                 if r.issue_date <= issue_date <= r.return_date:
#                     content = {"message":"The selected car is not available on this date"}
#                     return Response(data=json.dumps(content), status=status.HTTP_400_BAD_REQUEST)

#             # Check whether issue_date is not older than today's date, and is less equal to return_date
#             if current_date <= issue_date and issue_date <= return_date:
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def cancelar_renta(request, renta_pk):

    try:
        reservation = Renta.objects.get(pk=renta_pk)
    except Renta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)