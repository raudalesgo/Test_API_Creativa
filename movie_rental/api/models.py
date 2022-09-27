from django.db import models

class Cliente(models.Model):
    nombre = models.CharField('Nombre',max_length=255)
    email = models.EmailField('Email',max_length=255)
    celular = models.CharField('Celular',max_length=20)
    
    class Meta:
        ordering = ['nombre','email','celular']

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField('Titulo',max_length=20)
    descripcion = models.CharField('Descipcion',max_length=50)
    renta_por_dia = models.IntegerField('Renta_por_dia')
    disponible = models.BooleanField('Disponible',null=True)

    def __str__(self):
        return self.titulo


class Renta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    dia_renta = models.DateField()
    dia_devolucion = models.DateField()

    def __str__(self):
        return str(self.cliente) + "- " + str(self.pelicula)
    
    def get_data(self):
        return {
            'id': self.id,
            'cliente': self.cliente,
            'email': self.email,
            'fecha_renta' : self.fecha_renta,
            'fecha_devolucion': self.fecha_devoluacion
        }