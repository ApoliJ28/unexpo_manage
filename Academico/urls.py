from django.urls import path
from . import views

# Acceder a directorio raiz
urlpatterns = [
    path('pensum/', views.asignatura_admin, name= "pensum"),
    path('', views.inicio, name = "inicio" ),
    path('salir/', views.salir, name = "salir"),
    path('pensum/eliminacionCurso/<codigo>', views.eliminarCurso),
    path('pensum/edicionCurso/<codigo>', views.edicionCurso, name= "editarCurso"),
    path('editarCurso/', views.editarCurso, name = "editar"),
]
