from django import forms
from .models import Pelicula, Cliente, Renta


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'descripcion', 'renta_por_dia','disponible']
        widgets = {'titulo': forms.TextInput(attrs={'class': 'form-control'}),
                   'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
                   'renta_por_dia': forms.IntegerField(),
                   'disponible': forms.BooleanField( required=True),
                   }


# class ClienteForm(forms.ModelForm):
#     class Meta:
#         model = Cliente
#         fields = ['nombre', 'apellido', 'fecha_nacimiento','direccion', 'telefono', 'correo']
#         widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control'}),
#                    'apellido': forms.TextInput(attrs={'class': 'form-control'}),
#                    'fecha_nacimiento': forms.DateInput(format=('%d-%m-%y'), attrs={'class': 'form-control',
#                                                                                  'placeholder': 'Select a date',
#                                                                                  'type': 'date'
#                                                                                  }),
#                    'direccion': forms.TextInput(attrs={'class': 'form-control'}),
#                    'telefono': forms.TextInput(attrs={'class': 'form-control'}),
#                    'correo': forms.EmailInput(attrs={'placeholder': ('Email')})
#         }

# class RentaForm(forms.ModelForm):
#     class Meta:
#         model = Renta
#         fields = ['valor', 'fecha_alquiler', 'fecha_devolucion', 'cliente' , 'pelicula']
#         # def __init__(self, *args, **kwargs):
#         # pelicula = kwargs.pop('pelicula','')
#         # super(DocumentForm, self).__init__(*args, **kwargs)
#         # self.fields['user_defined_code']=forms.ModelChoiceField(queryset=UserDefinedCode.objects.filter(owner=pelicula))
#         widgets = {'valor': forms.TextInput(attrs={'class': 'form-control' }),
#                    'fecha_alquiler': forms.DateInput(format=('%d-%m-%y'), attrs={'class': 'form-control',
#                                                                                  'placeholder': 'Select a date',
#                                                                                  'type': 'date'
#                                                                                  }),
#                    'fecha_devolucion': forms.DateInput(format=('%d-%m-%y'), attrs={'class': 'form-control',
#                                                                                    'placeholder': 'Select a date',
#                                                                                    'type': 'date'
#                                                                                    }),

                   
#                    }
