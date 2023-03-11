class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, materia):
        codigo = materia.codigo
        if codigo not in self.carrito.keys():
            self.carrito[codigo] = {
                "materia_codigo": materia.codigo,
                "nombre": materia.nombre,
                "unidades": materia.creditos,
                "carrera": materia.carrera,
                "cantidad_estudiantes": 10
            }
            self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, materia):
        codigo = materia.codigo
        if codigo in self.carrito:
            del self.carrito[codigo]
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
