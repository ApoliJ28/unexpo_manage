from django.urls import path
from . import views
# Acceder a directorio raiz
urlpatterns = [
    path('pensum/', views.asignatura_admin),
    path('login/', views.login)
]
