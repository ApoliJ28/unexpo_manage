from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import AsignaturaForm
from .models import Asignatura
from django.contrib import messages


@login_required
# Create your views here.
def asignatura_admin(request):
    form = AsignaturaForm()
    # En una variable guardamos todos los materia de una db
    asignaturas = Asignatura.objects.all()
    print(asignaturas)
    if request.method == 'POST':
        form = AsignaturaForm(data=request.POST)
        try:
            if form.is_valid():
                form.save()
                # Datos correctos
                messages.success(request, "Curso Registrado!")
                return redirect('/pensum')
        except ValueError:
            return render(request, '/pensum', {"asignaturas": asignaturas, "form": form, 'error': 'Ingresa valores correctamente'})

    messages.success(request, "Cursos listados!")

    return render(request, "materia.html", {"asignaturas": asignaturas, "form": form})


@login_required
def eliminarCurso(request, codigo):
    asignatura = Asignatura.objects.get(codigo=codigo)
    asignatura.delete()

    messages.success(request, "Curso Eliminado!")

    return redirect("/pensum")


@login_required
def edicionCurso(request, codigo):
    asignatura = Asignatura.objects.get(codigo=codigo)
    return render(request, "edicion_materia.html", {"asignatura": asignatura})


@login_required
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

    asignatura = Asignatura.objects.get(codigo=codigo)
    asignatura.nombre = nombre
    asignatura.unidades = unidades
    asignatura.credito_requerido = credito_requerido
    asignatura.cantidadmax_estudiantes = cantidadmax_estudiantes
    asignatura.cantidad_estudiantes = cantidad_estudiantes
    asignatura.abierta = abierta_bool
    asignatura.carrera = carrera
    asignatura.save()

    messages.success(request, "Curso Actualizado!")

    return redirect("/pensum")


@login_required
def inicio(request):
    return render(request, "index.html")


def salir(request):
    logout(request)
    return redirect('/')


def iniciarsesion(request):
    return render(request, "login.html")
