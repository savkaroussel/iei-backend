from rest_framework import serializers
from .models import Comuna, Nacionalidad, Direccion, Autor, Biblioteca, Libro, Lector, Prestamo


# --- NACIONALIDAD ---
class NacionalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nacionalidad
        fields = ['id', 'pais', 'nacionalidad']


# --- AUTOR ---
class AutorSerializer(serializers.ModelSerializer):
    nacionalidad = serializers.StringRelatedField(
        source='id_nacionalidad', read_only=True
    )
    id_nacionalidad = serializers.PrimaryKeyRelatedField(
        queryset=Nacionalidad.objects.all()
    )

    class Meta:
        model = Autor
        fields = [
            'id',
            'nombre',
            'pseudonimo',
            'bio',
            'id_nacionalidad',
            'nacionalidad',
        ]


# --- COMUNA ---
class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ['id', 'codigo', 'comuna']


# --- DIRECCIÓN ---
class DireccionSerializer(serializers.ModelSerializer):
    comuna = serializers.StringRelatedField(
        source='id_comuna', read_only=True
    )
    id_comuna = serializers.PrimaryKeyRelatedField(
        queryset=Comuna.objects.all()
    )

    class Meta:
        model = Direccion
        fields = [
            'id',
            'calle',
            'numero',
            'departamento',
            'id_comuna',
            'comuna',
        ]


# --- BIBLIOTECA ---
class BibliotecaSerializer(serializers.ModelSerializer):
    direccion = serializers.StringRelatedField(
        source='id_direccion', read_only=True
    )
    id_direccion = serializers.PrimaryKeyRelatedField(
        queryset=Direccion.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Biblioteca
        fields = [
            'id',
            'nombre',
            'id_direccion',
            'direccion',
        ]


# --- LIBRO ---
class LibroSerializer(serializers.ModelSerializer):
    biblioteca = serializers.StringRelatedField(
        source='id_biblioteca', read_only=True
    )
    id_biblioteca = serializers.PrimaryKeyRelatedField(
        queryset=Biblioteca.objects.all()
    )

    autor = serializers.StringRelatedField(
        source='id_autor', read_only=True
    )
    id_autor = serializers.PrimaryKeyRelatedField(
        queryset=Autor.objects.all()
    )

    class Meta:
        model = Libro
        fields = [
            'id',
            'genero',
            'titulo',
            'paginas',
            'copias',
            'id_biblioteca',
            'biblioteca',
            'id_autor',
            'autor',
        ]


# --- LECTOR ---
class LectorSerializer(serializers.ModelSerializer):
    biblioteca = serializers.StringRelatedField(
        source='id_biblioteca', read_only=True
    )
    id_biblioteca = serializers.PrimaryKeyRelatedField(
        queryset=Biblioteca.objects.all()
    )

    direccion = serializers.StringRelatedField(
        source='id_direccion', read_only=True
    )
    id_direccion = serializers.PrimaryKeyRelatedField(
        queryset=Direccion.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Lector
        fields = [
            'id',
            'nombre',
            'rut',
            'correo',
            'fecha_nacimiento',
            'telefono',
            'id_biblioteca',
            'biblioteca',
            'id_direccion',
            'direccion',
        ]


# --- PRÉSTAMO ---
class PrestamoSerializer(serializers.ModelSerializer):
    libro = serializers.StringRelatedField(
        source='id_libro', read_only=True
    )
    id_libro = serializers.PrimaryKeyRelatedField(
        queryset=Libro.objects.all()
    )

    lector = serializers.StringRelatedField(
        source='id_lector', read_only=True
    )
    id_lector = serializers.PrimaryKeyRelatedField(
        queryset=Lector.objects.all()
    )

    class Meta:
        model = Prestamo
        fields = [
            'id',
            'id_libro',
            'libro',
            'id_lector',
            'lector',
            'created_at',
            'fecha_devolucion',
            'updated_at',
        ]
