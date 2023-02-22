const imagenes =document.querySelectorAll('.img-galeria');
const imagenesLigth = document.querySelector('.agregar-imagen');
const contenedorLigth =document.querySelector('.imagen-ligth');
const bar_opacity = document.querySelector('.bar');

imagenes.forEach(imagen=>{
    imagen.addEventListener('click',()=>{
        // Extraemos el valor de la direccion de cada unos de los elementos  tecleados
        aparecerImagen(imagen.getAttribute('src'));
    })
})

const aparecerImagen = (imagen)=>{
    imagenesLigth.src = imagen;
    contenedorLigth.classList.toggle('show');
    imagenesLigth.classList.toggle('showImage');
    bar_opacity.style.opacity ='0';
}
contenedorLigth.addEventListener('click',(e)=>{
    if(e.target !== imagenesLigth){
        contenedorLigth.classList.toggle('show');
        imagenesLigth.classList.toggle('showImage');
        bar_opacity.style.opacity ='1';
    }
})