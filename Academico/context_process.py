def total(request):
    total_creditos = 0
    if request.user.is_authenticated and request.session.get("carrito"):
        for key, value in request.session["carrito"].items():
            total_creditos += int(value["unidades"])
    return {"total_creditos": total_creditos}
