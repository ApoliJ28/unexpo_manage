from .models import RegistroInscripcion


def total(request):
    total_creditos = 0
    estudiante_id = request.user.id
    registro_inscripcion = RegistroInscripcion.objects.filter(
        estudiante_id=estudiante_id
    )
    if request.user.is_authenticated and registro_inscripcion:
        for registro in registro_inscripcion:
            materias = registro.materias_ids.all()
            for materia in materias:
                total_creditos += materia.creditos
    return {"total_creditos": total_creditos, "pago_total": total_creditos*3}
