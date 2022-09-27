from rest_framework import serializers
from api.models import Cliente, Pelicula, Renta


class ClienteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Cliente
        fields = ['id','nombre','email','celular']

class PeliculaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Pelicula
        fields = ['id','titulo','descripcion','renta_por_dia']

class DisponibilidadPeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = ['id','titulo','descripcion','renta_por_dia','disponible']
        
class RentaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Renta
        fields = ['id','cliente','pelicula','dia_renta','dia_devolucion']

class DetallePeliculaRentaSerializer(serializers.Serializer):
    pelicula = PeliculaSerializer()
    cuenta_activa = RentaSerializer(many=True)