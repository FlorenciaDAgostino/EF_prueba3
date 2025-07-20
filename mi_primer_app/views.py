from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


from .models import Familiar, Curso, Estudiante, Profesores, Televisores, Celulares, Heladeras, Lavarropas
from.forms import CursoForm, EstudianteForm, ProfesoresForm, TelevisoresForm, CelularesForm, HeladerasForm, LavarropasForm

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')


def saludo(request):
    return HttpResponse("¡Hola mundo!")


def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')


def crear_familiar(request, nombre):
    if nombre is not None:
        # Creamos un nuevo objeto Familiar
        nuevo_familiar = Familiar(
            nombre=nombre,
            apellido="ApellidoEjemplo",
            edad=30,
            fecha_nacimiento="1993-01-01",
            parentesco="Primo"
        )
        nuevo_familiar.save()
    return render(request, "mi_primer_app/crear_familiar.html", {"nombre": nombre})


def crear_curso(request):

    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el curso
            nuevo_curso = Curso(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                duracion_semanas=form.cleaned_data['duracion_semanas'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                activo=form.cleaned_data['activo']
            )
            nuevo_curso.save()
            return redirect('cursos')
    else:
        form = CursoForm()
        return render(request, 'mi_primer_app/crear_curso.html', {'form': form})
              
def crear_estudiante(request):

    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el curso
            nuevo_curso = Estudiante(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                edad=form.cleaned_data['edad'],
                fecha_inscripcion=form.cleaned_data['fecha_inscripcion']
            )
            nuevo_curso.save()
            return redirect('inicio')
    else:
        form = EstudianteForm()
        return render(request, 'mi_primer_app/crear_estudiante.html', {'form': form})
       
def crear_profesores(request):

    if request.method == 'POST':
        form =ProfesoresForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el curso
            nuevo_curso = Profesores(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                curso=form.cleaned_data['curso'],
            )
            nuevo_curso.save()
            return redirect('inicio')
    else:
        form = ProfesoresForm()
        return render(request, 'mi_primer_app/crear_profesores.html', {'form': form})
    
def crear_televisores(request):

    if request.method == 'POST':
        form =TelevisoresForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar 
            nuevo_curso = Televisores(
                modelo=form.cleaned_data['modelo'],
                marca=form.cleaned_data['marca'],
                fecha_publicación=form.cleaned_data['fecha_publicación']
            )
            nuevo_curso.save()
            return redirect('inicio')
    else:
        form = TelevisoresForm()
        return render(request, 'mi_primer_app/crear_televisores.html', {'form': form})

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos})

def buscar_cursos(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos, 'nombre': nombre})
    
class CelularesListView(ListView):
    model = Celulares
    template_name = 'mi_primer_app/listar_celulares.html'
    context_object_name = 'celulares'


class CelularesCreateView(CreateView):
    model = Celulares
    form_class = CelularesForm
    template_name = 'mi_primer_app/crear_celulares.html'
    success_url = reverse_lazy('listar-celulares')

class CelularesDetailView(DetailView):
    model = Celulares
    template_name = 'mi_primer_app/detalle_celulares.html'
    context_object_name = 'celulares'


class CelularesUpdateView(UpdateView):
    model = Celulares
    form_class = CelularesForm
    template_name = 'mi_primer_app/crear_celulares.html'
    success_url = reverse_lazy('listar-celulares') 


class CelularesDeleteView(DeleteView):
    model = Celulares
    template_name = 'mi_primer_app/eliminar_celulares.html'
    success_url = reverse_lazy('listar-celulares')    

class HeladerasListView(ListView):
    model = Heladeras
    template_name = 'mi_primer_app/listar_heladeras.html'
    context_object_name = 'heladeras'

class HeladerasCreateView(CreateView):
    model = Heladeras
    form_class = HeladerasForm
    template_name = 'mi_primer_app/crear_heladeras.html'
    success_url = reverse_lazy('listar-heladeras')

class HeladerasDetailView(DetailView):
    model = Heladeras
    template_name = 'mi_primer_app/detalle_heladeras.html'
    context_object_name = 'heladeras'


class HeladerasUpdateView(UpdateView):
    model = Heladeras
    form_class = HeladerasForm
    template_name = 'mi_primer_app/crear_heladeras.html'
    success_url = reverse_lazy('listar-heladeras') 


class HeladerasDeleteView(DeleteView):
    model = Heladeras
    template_name = 'mi_primer_app/eliminar_heladeras.html'
    success_url = reverse_lazy('listar-heladeras')   

class LavarropasListView(ListView):
    model = Lavarropas
    template_name = 'mi_primer_app/listar_lavarropas.html'
    context_object_name = 'lavarropas'    

class LavarropasCreateViews(CreateView):
    model = Lavarropas
    form_class = LavarropasForm
    template_name = 'mi_primer_app/crear_lavarropas.html'
    success_url = reverse_lazy('listar-lavarropas')   

class LavarropasDetailView(DetailView):
    model = Lavarropas
    template_name = 'mi_primer_app/detalle_lavarropas.html'
    context_object_name = 'lavarropas'


class LavarropasUpdateView(UpdateView):
    model = Lavarropas
    form_class = LavarropasForm
    template_name = 'mi_primer_app/crear_lavarropas.html'
    success_url = reverse_lazy('listar-lavarropas') 


class LavarropasDeleteView(DeleteView):
    model = Lavarropas
    template_name = 'mi_primer_app/eliminar_lavarropas.html'
    success_url = reverse_lazy('listar-lavarropas')