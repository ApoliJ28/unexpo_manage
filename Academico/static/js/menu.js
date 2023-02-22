const bar =document.querySelector('.bar');
const menu =document.querySelector('.menu-navegacion');
console.log(menu);
console.log(bar);
/*
Vamos a agregale un  evento a caa uno de los elemento selecionadao que ina ves 
clickeados estos  ocurriria un suceso en la pagina
*/
/*Vamos a cambiar la clase para que pueda ser mostrado el menu*/
bar.addEventListener('click',()=>{
    // Al utilizar toggle cada vez que yo presione ese boton a colocar o quitar la clase spread
    menu.classList.toggle("spread");
})
window.addEventListener('click',e=>{
    console.log(e.target);
    if(menu.classList.contains('spread') && e.target != menu && e.target != bar){
        menu.classList.toggle("spread");
    }
})