from django.urls import path

from .views import (saludo, saludo_con_template, crear_familiar,
                    inicio, crear_curso, crear_estudiante, buscar_cursos, cursos, crear_profesores, crear_televisores,
                    CelularesCreateView, CelularesListView, CelularesDeleteView, CelularesDetailView, CelularesUpdateView, HeladerasCreateView, HeladerasListView, HeladerasDeleteView, HeladerasDetailView, HeladerasUpdateView, LavarropasCreateViews,LavarropasListView, LavarropasDeleteView, LavarropasDetailView, LavarropasUpdateView)

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-familiar/<str:nombre>/', crear_familiar),
    path('crear-curso/', crear_curso, name= 'crear-curso'),
    path('crear-estudiante/', crear_estudiante, name= 'crear-estudiante'),
    path('crear-profesores/', crear_profesores, name= 'crear-profesores'),
    path('crear-televisores/', crear_televisores, name= 'crear-televisores'),
    path('cursos/', cursos, name='cursos'),
    path('cursos/buscar', buscar_cursos, name='buscar-cursos'),

    # urls con vistas basadas en clase
    path('listar-celulares/', CelularesListView.as_view(), name= 'listar-celulares'),
    path('crear-celulares/', CelularesCreateView.as_view(), name= 'crear-celulares'),
    path('detalle-celulares/<int:pk>', CelularesDetailView.as_view(), name='detalle-celulares'),
    path('editar/<int:pk>/', CelularesUpdateView.as_view(), name='editar-celulares'),
    path('eliminar/<int:pk>/', CelularesDeleteView.as_view(), name='eliminar-celulares'),
    path('listar-heladeras/', HeladerasListView.as_view(), name= 'listar-heladeras'),
    path('crear-heladeras/', HeladerasCreateView.as_view(), name= 'crear-heladeras'),
    path('detalle-heladeras/<int:pk>', HeladerasDetailView.as_view(), name='detalle-heladeras'),
    path('editar/<int:pk>/', HeladerasUpdateView.as_view(), name='editar-heladeras'),
    path('eliminar/<int:pk>/', HeladerasDeleteView.as_view(), name='eliminar-heladeras'),
    path('listar-lavarropas/', LavarropasListView.as_view(), name= 'listar-lavarropas'),
    path('crear-lavarropas/', LavarropasCreateViews.as_view(), name= 'crear-lavarropas'),
    path('detalle-lavarropas/<int:pk>', LavarropasDetailView.as_view(), name='detalle-lavarropas'),
    path('editar/<int:pk>/', LavarropasUpdateView.as_view(), name='editar-lavarropas'),
    path('eliminar/<int:pk>/', LavarropasDeleteView.as_view(), name='eliminar-lavarropas'),
]
    
    

 