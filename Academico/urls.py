from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Acceder a directorio raiz
urlpatterns = [
    path('', views.portada, name="portada"),
    path('pensum/', views.asignatura_admin, name="pensum"),
    path('cursos/', views.cursos, name="cursos"),
    path('salir/', views.salir, name="salir"),
    path('pensum/eliminacionCurso/<codigo>', views.eliminarCurso),
    path('pensum/edicionCurso/<codigo>', views.edicionCurso, name="editarCurso"),
    path('editarCurso/', views.editarCurso, name="editar"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)