import pytz
from Academico.context_process import total
from datetime import date, datetime, time
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic import CreateView, ListView
from .context_process import total
from .forms import AsignaturaForm, FormularioUsuario, RegistroInscripcionForm
from .models import Materia, Usuario, Departamento, Carrera, RegistroInscripcion, RegistroPago
from django.contrib import messages


def portada(request):
    return render(request, "portada.html")

# Create your views here.


def asignatura_admin(request):
    form = RegistroInscripcionForm()

    if request.method == 'POST':
        form = AsignaturaForm(data=request.POST)
        try:
            if form.is_valid():
                form.save()
                # Datos correctos
                messages.success(request, "Curso Registrado!")
                return redirect('academico:pensum')
        except ValueError:
            return render(request, '/pensum', {"asignaturas": asignaturas, "form": form, 'error': 'Ingresa valores correctamente'})

    messages.success(request, "Cursos listados!")

    return render(request, "materia.html", {"asignaturas": asignaturas, "form": form})


def asignatura_admin(request):
    form = AsignaturaForm()

    # En una variable guardamos todos los materia de una db
    asignaturas = Materia.objects.all()
    if request.method == 'POST':
        form = AsignaturaForm(data=request.POST)
        try:
            if form.is_valid():
                form.save()
                # Datos correctos
                messages.success(request, "Curso Registrado!")
                return redirect('academico:pensum')
        except ValueError:
            return render(request, '/pensum', {"asignaturas": asignaturas, "form": form, 'error': 'Ingresa valores correctamente'})

    messages.success(request, "Cursos listados!")

    return render(request, "materia.html", {"asignaturas": asignaturas, "form": form})


def eliminarCurso(request, codigo):
    asignatura = Materia.objects.get(codigo=codigo)
    asignatura.delete()

    messages.success(request, "Curso Eliminado!")

    return redirect("academico:pensum")


def edicionCurso(request, codigo):
    asignatura = Materia.objects.get(codigo=codigo)
    return render(request, "edicion_materia.html", {"asignatura": asignatura})


def editarCurso(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']
    unidades = request.POST['num_unidades']
    credito_requerido = request.POST['credito_requerido']
    cantidadmax_estudiantes = request.POST['cantidadmax_estudiantes']
    cantidad_estudiantes = request.POST['cantidad_estudiantes']
    carrera = request.POST['carrera']

    abierta = request.POST.get('abierta', False)
    abierta_bool = False
    if abierta == 'on':
        abierta_bool = True

    asignatura = Materia.objects.get(codigo=codigo)
    asignatura.nombre = nombre
    asignatura.unidades = unidades
    asignatura.credito_requerido = credito_requerido
    asignatura.cantidadmax_estudiantes = cantidadmax_estudiantes
    asignatura.cantidad_estudiantes = cantidad_estudiantes
    asignatura.abierta = abierta_bool
    asignatura.carrera = carrera
    asignatura.save()

    messages.success(request, "Curso Actualizado!")

    return redirect("academico:pensum")


def registro_usuario(request):
    form = RegistroInscripcionForm()

    if request.method == 'POST':
        form = RegistroInscripcionForm(data=request.POST)
        try:
            if form.is_valid():
                form.save()
                # Datos correctos
                messages.success(request, "Curso Registrado!")
                return redirect('academico:cursos')
        except ValueError:
            return render(request, '/pensum', {"form": form, 'error': 'Ingresa valores correctamente'})

    messages.success(request, "Cursos listados!")

    return render(request, "tiempo_usuario.html", {"form": form})


def cursos(request):
    estudiante = request.user.id
    # Obtengo los registros de inscripcion del estudiante
    registros_inscripcion = RegistroInscripcion.objects.filter(
        estudiante_id=estudiante,
        estado="inscrito"
    )

    if registros_inscripcion:
        for registro in registros_inscripcion:
            materias = registro.materias_ids.all()

        context = {
            "registro_inscripcion": registros_inscripcion,
            "materias": materias
        }
        return render(request, "index.html", context)
    else:
        context = {
            "registro_inscripcion": False,
            "materias": False
        }
        return render(request, "index.html", context)


def seleccion_carrera(request, codigo):
    # Obtengo la tabla de las carreras
    carrera = Carrera.objects.get(codigo_c=codigo)
    # Obtengo los semestres de la clase Materia
    semestres = Materia().opciones_semestres
    semestre_dict = {}
    if carrera:
        # Si existe la carrera traeme los departamentos de esa carrera
        departamentos = Departamento.objects.filter(carrera_ids=codigo)
        # Guarda en un diccionario las materias por semestre
        for semestre in semestres:
            semestre_dict[f"{semestre[1]}"] = []
            for departamento in departamentos:
                dpto_code = departamento.codigo_dep
                materias = Materia.objects.filter(
                    departamento_id=dpto_code, semestre=semestre[0])
                for materia in materias:
                    semestre_dict[f"{semestre[1]}"].append(materia)

        return render(request, "prueba.html", {"carrera": carrera, "materias_semestre": semestre_dict})


def salir(request):
    logout(request)
    return redirect('/')


class listadoUsuario(ListView):
    model = Usuario
    template_name = 'listar_usuario.html'

    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True)


class registrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'crear_usuario.html'
    success_url = reverse_lazy('academico:listarUsuarios')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo_usuario = Usuario(
                email=form.cleaned_data['email'],
                username=form.cleaned_data['username'],
                nombres=form.cleaned_data['nombres'],
                apellidos=form.cleaned_data['apellidos'],
                expediente=form.cleaned_data['expediente'],
                cedula=form.cleaned_data['cedula'],
                creditos_aprobados=form.cleaned_data['creditos_aprobados'],
                carrera_id=form.cleaned_data['carrera_id'],
                semestre=form.cleaned_data['semestre'],
                tipo_estudiante=form.cleaned_data['tipo_estudiante'],
                imagen=form.cleaned_data['imagen'],

            )
            nuevo_usuario.set_password(form.cleaned_data['password1'])
            nuevo_usuario.save()
            return redirect('academico:listarUsuarios')
        else:
            return render(request, self.template_name, {'form': form})


def eliminarUsuario(request, expediente):
    user = Usuario.objects.get(expediente=expediente)
    user.delete()

    return redirect("academico:listarUsuarios")


def edicionUsuario(request, expediente):
    user = Usuario.objects.get(expediente=expediente)
    return render(request,  "edicion_usuario.html", {"user": user})


def editarUsuario(request):
    expediente = request.POST['expediente']
    nombres = request.POST['nombres']
    apellidos = request.POST['apellidos']
    username = request.POST['username']
    email = request.POST['email']
    cedula = request.POST['cedula']
    creditos_aprobados = request.POST['creditos_aprobados']

    tipo_estudiante = request.POST['tipo_estudiante']

    user = Usuario.objects.get(expediente=expediente)
    user.nombres = nombres
    user.apellidos = apellidos
    user.username = username
    user.email = email
    user.cedula = cedula
    user.creditos_aprobados = creditos_aprobados

    user.tipo_estudiante = tipo_estudiante

    user.save()

    return redirect("academico:listarUsuarios")


def inscripciones(request):
    # Obtengo el id del estudiante
    estudiante = request.user.id

    # Obtengo los registros de inscripcion del estudiante
    registros_inscripcion = RegistroInscripcion.objects.filter(
        estudiante_id=estudiante)

    # Si tiene inscripciones en pendiente, traeme el registro
    if registros_inscripcion:
        for registro in registros_inscripcion:
            fecha_apertura = registro.fecha_apertura
            hora_apertura = registro.hora_apertura
            if registro.estado == "pendiente":
                fecha_actual = date.today()
                hora_actual = datetime.now(pytz.timezone('America/Caracas')).time()
                if (fecha_actual == fecha_apertura and hora_actual >= hora_apertura) or fecha_actual > fecha_apertura:
                    # Obtengo la tabla de las carreras
                    codigo = request.user.carrera_id.codigo_c
                    carrera = Carrera.objects.get(codigo_c=codigo)

                    # Obtengo los semestres de la clase Materia
                    semestres = Materia().opciones_semestres
                    semestre_dict = {}

                    if carrera:
                        # Si existe la carrera traeme los departamentos de esa carrera
                        departamentos = Departamento.objects.filter(
                            carrera_ids=codigo)

                        # Guarda en un diccionario las materias por semestre
                        for semestre in semestres:
                            semestre_dict[f"{semestre[1]}"] = []
                            for departamento in departamentos:
                                dpto_code = departamento.codigo_dep
                                materias = Materia.objects.filter(
                                    departamento_id=dpto_code, semestre=semestre[0])
                                for materia in materias:
                                    materias_inscritas = RegistroInscripcion.objects.filter(
                                        materias_ids=materia)
                                    if len(materias_inscritas) >= 2:
                                        materia.abierta = False
                                    else:
                                        materia.abierta = True

                                    semestre_dict[f"{semestre[1]}"].append(materia)

                        context = {
                            "registro_inscripcion": registros_inscripcion,
                            "carrera": carrera,
                            "materias_semestre": semestre_dict,
                            "inscripcion_estado": registro.estado,
                            "turno_abierto": True
                        }
                        return render(request, "inscripciones.html", context)
                else:
                    context = {
                        "registro_inscripcion": registros_inscripcion,
                        "turno_abierto": False,
                        "fecha_apertura": fecha_apertura,
                        "hora_apertura": hora_apertura
                    }
                    return render(request, "inscripciones.html", context)
            elif registro.estado == "pago":
                return redirect("academico:estado_pago")
            else:
                return redirect("academico:estado_inscrito")
    else:
        context = {
            "registro_inscripcion": False,
        }
        return render(request, "inscripciones.html", context)


def agregar_materia(request, codigo):
    # Obtengo el id del estudiante
    estudiante = request.user.id

    # Obtengo los registros de inscripcion del estudiante
    registros_inscripcion = RegistroInscripcion.objects.filter(
        estudiante_id=estudiante)

    # Obtengo la asignatura que se agregara
    asignatura = Materia.objects.get(codigo=codigo)

    # Si tiene inscripciones en pendiente, traeme el registro
    if registros_inscripcion:
        for registro in registros_inscripcion:
            if registro.estado == "pendiente":
                registro.materias_ids.add(asignatura)

    return redirect("academico:inscripciones")


def eliminar_materia(request, codigo):
    # Obtengo el id del estudiante
    estudiante = request.user.id

    # Obtengo los registros de inscripcion del estudiante
    registros_inscripcion = RegistroInscripcion.objects.filter(
        estudiante_id=estudiante
    )

    # Obtengo la asignatura que se agregara
    asignatura = Materia.objects.get(codigo=codigo)

    # Si tiene inscripciones en pendiente, traeme el registro
    if registros_inscripcion:
        for registro in registros_inscripcion:
            if registro.estado == "pendiente":
                registro.materias_ids.remove(asignatura)
    return redirect("academico:inscripciones")


def limpiar_materias(request):
    # Obtengo el id del estudiante
    estudiante = request.user.id

    # Obtengo los registros de inscripcion del estudiante
    registros_inscripcion = RegistroInscripcion.objects.filter(
        estudiante_id=estudiante
    )

    # Si tiene inscripciones en pendiente, traeme el registro
    if registros_inscripcion:
        for registro in registros_inscripcion:
            if registro.estado == "pendiente":
                registro.materias_ids.clear()
    return redirect("academico:inscripciones")


# Accion para guardar los datos en la tabla de inscripciones y pasar al estado de pago
def estado_pago(request):
    # carrito = Carrito(request).carrito
    estudiante_id = request.user.id
    registros_inscripcion = RegistroInscripcion.objects.filter(
        estudiante_id=estudiante_id)

    if registros_inscripcion:
        for registro in registros_inscripcion:
            estado = registro.estado
            materias = registro.materias_ids.all()

            if estado == "pendiente":
                registro.estado = "pago"
                registro.save()

                context = {
                    "registros_inscripcion": registros_inscripcion,
                    "materias": materias
                }
                return render(request, "pago_views.html", context)
            elif estado == "pago":
                context = {
                    "registros_inscripcion": registros_inscripcion,
                    "materias": materias
                }
                return render(request, "pago_views.html", context)
    else:
        context = {"registros_inscripcion": [], "materias": []}
        return render(request, "pago_views.html", context)


def estado_inscrito(request):
    estudiante_id = request.user.id
    registros_inscripcion = RegistroInscripcion.objects.filter(
        estudiante_id=estudiante_id)

    if registros_inscripcion:
        for registro in registros_inscripcion:
            estado = registro.estado
            materias = registro.materias_ids.all()

            if estado == "pago":
                registro.estado = "inscrito"
                pago_total = total(request)
                pago_rec = RegistroPago.objects.create(
                    fecha_pago=datetime.now(pytz.timezone('America/Caracas')),
                    estudiante_id=request.user,
                    registro_inscripcion=registro.id,
                    cantidad_pago=pago_total["pago_total"]
                )
                registro.pago_id = pago_rec
                registro.fecha_inscripcion = datetime.now(
                    pytz.timezone('America/Caracas'))
                registro.save()
                context = {
                    "registros_inscripcion": registros_inscripcion,
                    "materias": materias
                }
                return render(request, "finalizada.html", context)

            elif estado == "inscrito":
                context = {
                    "registros_inscripcion": registros_inscripcion,
                    "materias": materias
                }
                return render(request, "finalizada.html", context)


def volver_pendiente(request):
    estudiante_id = request.user.id
    registros_inscripcion = RegistroInscripcion.objects.filter(
        estudiante_id=estudiante_id, estado="pago")

    if registros_inscripcion:
        for registro in registros_inscripcion:
            registro.estado = "pendiente"
            registro.save()

    return redirect("academico:inscripciones")


def volver_pago(request):
    estudiante_id = request.user.id
    registros_inscripcion = RegistroInscripcion.objects.filter(
        estudiante_id=estudiante_id, estado="inscrito")

    if registros_inscripcion:
        for registro in registros_inscripcion:
            registro.estado = "pago"
            registro.save()

    return redirect("academico:estado_pago")

def registro_pago(request):
    metodo = request.POST['metodo']
    #usuario = request.user

    if metodo == "Pago movil":
        cedula = request.POST['cedula']
        tlf = request.POST['tlf']
        banco = request.POST['banco']
        num_referencia = request.POST['numReferncia']
        monto = request.POST['monto']

        #Aqui se guarda los datos en el modelo... Ejemplo

        RegistroInscripcion.objects.create(cedula=cedula, tlf=tlf, banco=banco, 
                num_referencia=num_referencia, monto=monto)
        

    elif metodo == "Efectivo":
        moneda = request.POST['moneda']
        monto = request.POST['monto']

        #Aqui se guarda los datos en el modelo... Ejemplo

        RegistroInscripcion.objects.create(moneda=moneda, monto=monto)

    elif metodo == "Tarjeta de credito":
        cedula = request.POST['cedula']
        num_tarjeta = request.POST['numTarjeta']
        banco = request.POST['banco']
        num_referencia = request.POST['numReferncia']
        monto = request.POST['monto']


        #Aqui se guarda los datos en el modelo... Ejemplo

        RegistroInscripcion.objects.create(cedula=cedula, num_tarjeta=num_tarjeta, 
                    banco=banco, num_referencia=num_referencia, monto=monto)
    else:
        cedula = request.POST['cedula']
        num_tarjeta = request.POST['numTarjeta']
        cuenta = request.POST['cuenta']
        banco = request.POST['banco']
        num_referencia = request.POST['numReferncia']
        monto = request.POST['monto']


        #Aqui se guarda los datos en el modelo... Ejemplo

        RegistroInscripcion.objects.create(cedula=cedula, num_tarjeta=num_tarjeta, 
                    banco=banco, cuenta=cuenta, num_referencia=num_referencia, 
                    monto=monto)
        
    return redirect("academico:estado_inscrito")
