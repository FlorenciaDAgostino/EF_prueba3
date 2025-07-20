from django import forms
from .models import Celulares, Heladeras, Lavarropas

class CursoForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    duracion_semanas = forms.IntegerField(min_value=1, initial=4)
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    activo = forms.BooleanField(required=False, initial=True)


class EstudianteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField()
    edad = forms.IntegerField(min_value=10, max_value=100)
    fecha_inscripcion = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    
class ProfesoresForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField()
    curso = forms.CharField(label="Curso", max_length=100)  

class TelevisoresForm(forms.Form):
    modelo = forms.CharField(label="Modelo", max_length=20)
    marca = forms.CharField(label="Marca", max_length=20)
    fecha_publicación = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))   
    

class CelularesForm(forms.ModelForm):
    class Meta:
        model = Celulares
        fields = ['modelo', 'marca', 'descripcion']    

class HeladerasForm(forms.ModelForm):
    class Meta:
        model = Heladeras
        fields = ['modelo', 'marca', 'descripcion']   

class LavarropasForm(forms.ModelForm):
    class Meta:
        model = Lavarropas
        fields = ['modelo', 'marca', 'descripcion']   
