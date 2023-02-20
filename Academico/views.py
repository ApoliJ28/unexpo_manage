from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import AsignaturaForm
from .models import Asignatura

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
                return redirect('/pensum')
        except ValueError:
            return render(request, '/pensum', {"asignaturas": asignaturas, "form": form, 'error': 'Ingresa valores correctamente'})

    return render(request, "materia.html", {"asignaturas": asignaturas, "form": form})

@login_required

def inicio(request):
    return render(request, "index.html")

def salir(request):
    logout(request)
    return redirect('/')