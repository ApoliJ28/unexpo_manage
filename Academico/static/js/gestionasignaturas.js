(function () {
  // Seleccionamos el boton de eliminacion
  const btnElminacion = document.querySelectorAll(".btn-eliminacion");

  btnElminacion.forEach((Eliminar) => {
    Eliminar.addEventListener("click", (evento) => {
      const confirmar = confirm(
        "Estas Seguro de la Eliminacion de esta Materia"
      );

      if (!confirmar) {
        evento.preventDefault();
      }
    });
  });
})();
