from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

# Acceder a directorio raiz
urlpatterns = [
    path('', views.portada, name="portada"),
    path('pensum/', login_required(views.asignatura_admin), name="pensum"),
    path('cursos/', login_required(views.cursos), name="cursos"),
    path('salir/', login_required(views.salir), name="salir"),
    path('cursos/seleccion_carrera/<codigo>',
         login_required(views.seleccion_carrera)),
    path('pensum/eliminacionCurso/<codigo>',
         login_required(views.eliminarCurso)),
    path('pensum/edicionCurso/<codigo>',
         login_required(views.edicionCurso), name="editarCurso"),
    path('pensum/editarCurso/', login_required(views.editarCurso), name="editar"),
    path('listarUsuarios/', login_required(views.listadoUsuario.as_view()),
         name="listarUsuarios"),
    path('registrarUsuario/', login_required(views.registrarUsuario.as_view()),
         name="registrarUsuario"),
    path('listarUsuarios/eliminarUsuario/<expediente>',
         login_required(views.eliminarUsuario), name="eliminarUsuario"),
    path('listarUsuarios/edicionUsuario/<expediente>',
         login_required(views.edicionUsuario), name="edicionUsuario"),
    path('listarUsuarios/editarUsuario/',
         login_required(views.editarUsuario), name="editarUsuario"),
    path('listarUsuarios/registro_usuario',
         login_required(views.registro_usuario), name="registroUsuario"),

    path('inscripciones/', login_required(views.inscripciones), name="inscripciones"),
    path('inscripciones/agregarMateria/<codigo>',
         login_required(views.agregar_materia), name="agregar"),
    path('inscripciones/eliminarMateria/<codigo>',
         login_required(views.eliminar_materia), name="eliminar"),
    path('inscripciones/limpiarMaterias',
         login_required(views.limpiar_materias), name="limpiar"),
    path('pago/estado_pago', login_required(views.estado_pago), name="estado_pago"),
    path('pago/volver_pendiente', login_required(views.volver_pendiente),
         name="volver_pendiente"),
    path('pago/volver_pago', login_required(views.volver_pago), name="volver_pago"),
    path('pago/estado_inscrito', login_required(views.estado_inscrito),
         name="estado_inscrito"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
