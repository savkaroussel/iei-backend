from rest_framework import serializers
from .models import Comuna, Nacionalidad, Direccion, Autor, Biblioteca, Libro, Lector, Prestamo

class ComunaSerializer(serializers.ModelSerializer):
 class Meta:
    model = Comuna
    fields = '__all__'

class NacionalidadSerializer(serializers.ModelSerializer):
 class Meta:
    model = Nacionalidad
    fields = '__all__'

class DireccionSerializer(serializers.ModelSerializer):
 id_comuna = ComunaSerializer()
 class Meta:
    model = Direccion 
    fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
 id_nacionalidad = NacionalidadSerializer()
 class Meta:
    model = Autor
    fields = '__all__'

class BibliotecaSerializer(serializers.ModelSerializer):
 class Meta:
    model = Biblioteca
    fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
 class Meta:
    model = Libro
    fields = '__all__'

class LectorSerializer(serializers.ModelSerializer):
 class Meta:
    model = Lector
    fields = '__all__'
 
class PrestamoSerializer(serializers.ModelSerializer):
 class Meta:
    model = Prestamo
    fields = '__all__'