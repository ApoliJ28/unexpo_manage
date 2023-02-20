from django.shortcuts import render, redirect
from django.urls import reverse
# Exportamos el modelo de los cursos
from .forms import AsignaturaForm
from .models import Asignatura
# Create your views here.

# Importamos el modelo de las tareas


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
                return redirect('/pensum')
        except ValueError:
            return render(request, '/pensum', {"asignaturas": asignaturas, "form": form, 'error': 'Ingresa valores correctamente'})

    return render(request, "materia.html", {"asignaturas": asignaturas, "form": form})


def login(request):
    return render(request, "login.html")
