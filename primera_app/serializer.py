from rest_framework import serializers
from .models import Comuna, Nacionalidad, Direccion, Autor, Biblioteca, Libro, Lector, Prestamo

class Comuna_Serializer(serializers.ModelSerializer):
 class Meta:
    model = Comuna
    fields = '__all__'

class Nacionalidad_Serializer(serializers.ModelSerializer):
 class Meta:
    model = Nacionalidad
    fields = '__all__'

class Direccion_Serializer(serializers.ModelSerializer):
 class Meta:
    model = Direccion 
    fields = '__all__'

class Autor_Serializer(serializers.ModelSerializer):
 class Meta:
    model = Autor
    fields = '__all__'

class Biblioteca_Serializer(serializers.ModelSerializer):
 class Meta:
    model = Biblioteca
    fields = '__all__'

class Libro_Serializer(serializers.ModelSerializer):
 class Meta:
    model = Libro
    fields = '__all__'

class Lector_Serializer(serializers.ModelSerializer):
 class Meta:
    model = Lector
    fields = '__all__'
 
class Prestamo_Serializer(serializers.ModelSerializer):
 class Meta:
    model = Prestamo
    fields = '__all__'