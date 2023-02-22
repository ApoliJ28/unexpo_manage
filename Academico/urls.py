from django.urls import path
from . import views

# Acceder a directorio raiz
urlpatterns = [
    path('', views.portada, name="portada"),
    path('pensum/', views.asignatura_admin, name="pensum"),
    path('cursos/', views.cursos, name="cursos"),
    # path('iniciarsesion/', views.iniciarsesion, name="salir"),
    path('salir/', views.salir, name="salir"),
    path('pensum/eliminacionCurso/<codigo>', views.eliminarCurso),
    path('pensum/edicionCurso/<codigo>', views.edicionCurso, name="editarCurso"),
    path('editarCurso/', views.editarCurso, name="editar"),
]
