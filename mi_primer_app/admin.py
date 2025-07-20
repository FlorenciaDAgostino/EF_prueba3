from django.contrib import admin

# Register your models here.
from .models import Familiar, Curso, Estudiante, Profesores, Televisores, Celulares, Heladeras, Lavarropas 

register_models = [Familiar, Curso, Estudiante, Profesores, Televisores, Celulares, Heladeras, Lavarropas]

admin.site.register(register_models)