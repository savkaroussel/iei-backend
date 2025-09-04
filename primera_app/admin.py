from django.contrib import admin
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Lector, Libro, Prestamo

# Register your models here.
admin.site.register(Nacionalidad)
admin.site.register(Autor)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Biblioteca)
admin.site.register(Lector)
admin.site.register(Libro)
admin.site.register(Prestamo)