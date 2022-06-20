const tablaDolar = document.getElementById("pruebas");
const URLApi = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
const ventaTabla = document.getElementById("valor-venta");
const tituloTabla = document.getElementById("tipo-dolar");
const compraTabla = document.getElementById("valor-compra");
const cronometro = document.getElementById("cronometro");
let nombresDolar = [];
let ventaDolar = [];
let compraDolar = [];

//consigo la info de la api
function conseguirDatos(){
    
   let api = fetch(URLApi);

   let apiResponse = api.then(response => response.json());

   let  datosTabla = apiResponse.then(function(data) { 

         data.map(x => {if (x.casa.nombre.includes("Dolar")){

         nombresDolar.push(x.casa.nombre);
         ventaDolar.push(x.casa.venta);
         compraDolar.push(x.casa.compra);

        }});


    })
}
conseguirDatos();


//cronometro que se actualiza cada 1 minuto
function cronometraje() {
      setInterval(() => {
          let fecha = new Date();
          let minutos = fecha.getMinutes();
          let horas = fecha.getHours();
          let dias = fecha.getDay();
          
          cronometro.innerHTML = `Actualizado por ultima vez a las ${horas} horas y ${minutos} minutos `
      },60000)
}

//resetear datos arrays
function borrarAray(){
     nombresDolar = [];
     ventaDolar = [];
     compraDolar = [];

}
//recargar la tabla por si hubiese un erro visual o en los datos
function recargar(){
    tituloTabla.innerHTML = "Seleccione un tipo de Dolar";
    ventaTabla.innerHTML = "-";
    compraTabla.innerHTML = "-";
    cronometro.innerHTML = "-";
}
function imprimirDolar(){}


//Funcion para visualizar la seccion de cotizaciones
function visualizacionOn() {
    document.getElementById('visualizacion').style.display = 'inline-block'
}

function idObtener() {
    document.querySelectorAll(".click").forEach(el => {
        el.addEventListener("click", e => {
          const id = e.target.getAttribute("id");
          let typeDolar = document.getElementById(id).innerHTML;
          for(let i of nombresDolar){
            if(i == typeDolar){
                tituloTabla.innerHTML = nombresDolar[nombresDolar.indexOf(i)];
                ventaTabla.innerHTML = ventaDolar[nombresDolar.indexOf(i)];
                compraTabla.innerHTML = compraDolar[nombresDolar.indexOf(i)];
            }
          }
        });
      });
      cronometraje();

    }
idObtener();
//Actualizacion de datos minuto a minuto
setInterval(borrarAray, 60000);
setInterval(conseguirDatos, 60000)

