from django.db import models
import datetime
from rutificador import Rut
from django.core.exceptions import ValidationError

ahora = datetime.datetime.now

# Create your models here.

def validar_rut(rut):
    try: 
        rut_valido = Rut(rut)
    except: 
        raise ValidationError('Digito validador no corresponde')
    
def validar_mayoria_edad(fecha_nacimiento):
    fecha_actual = datetime.datetime.today()
    edad = fecha_actual.year - fecha_nacimiento.year
    if (fecha_nacimiento.month, fecha_nacimiento.day) > (fecha_actual.month, fecha_actual.day):
        edad -= 1
    if edad < 18:
        raise ValidationError('Debe ser mayor de edad...')

class Nacionalidad(models.Model):
    pais = models.CharField(max_length=50, null=False)
    nacionalidad = models.CharField(max_length=50, null=False)
    created_at=models.DateTimeField(default = ahora)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nacionalidad

class Autor(models.Model):
    nombre = models.CharField(max_length=250, null=False)
    pseudonimo = models.CharField(max_length=50, null=True)
    id_nacionalidad = models.ForeignKey(
        Nacionalidad, on_delete=models.CASCADE, blank=True)
    bio = models.TextField()
    created_at=models.DateTimeField(default = ahora)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.pseudonimo!='':
            return self.pseudonimo
        else:
            return self.nombre


class Comuna(models.Model):
    codigo = models.CharField(max_length=5, null=False)
    comuna = models.CharField(max_length=50, null=False)
    created_at=models.DateTimeField(default = ahora)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comuna

class Direccion(models.Model):
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    calle = models.CharField(max_length=50, null=True)
    numero = models.CharField(max_length=10, null=True)
    departamento = models.CharField(max_length=20, null=True)
    created_at=models.DateTimeField(default = ahora)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comuna: {self.id_comuna}, Calle: {self.calle}'

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    id_direccion = models.ForeignKey(
        Direccion, on_delete=models.CASCADE, null=True)
    created_at=models.DateTimeField(default = ahora)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    genero = models.CharField(max_length=50, null=False)
    titulo = models.CharField(max_length=250, null=False)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    paginas = models.IntegerField()
    copias = models.IntegerField()
    created_at=models.DateTimeField(default = ahora)
    updated_at = models.DateTimeField(auto_now=True)

class Lector(models.Model):
    id_biblioteca = models.ForeignKey(
        Biblioteca, on_delete=models.CASCADE, null=False)
    id_direccion = models.ForeignKey(
        Direccion, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=150, null=False)
    rut = models.CharField(null=False, max_length=12, unique=True, validators=[validar_rut])
    #digito_verificador = models.CharField(max_lenght=1, null=False)
    correo = models.CharField(max_length=50, null=True)
    fecha_nacimiento = models.DateField(null=True, validators=[validar_mayoria_edad])
    telefono = models.CharField(max_length=20, null=True)
    created_at=models.DateTimeField(default = ahora)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    id_lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    created_at=models.DateTimeField(default = ahora)
    fecha_devolucion = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)