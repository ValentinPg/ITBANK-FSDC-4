const tablaDolar = document.getElementById("pruebas");
const URLApi = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
const ventaTabla = document.getElementById("valor-venta");
const tituloTabla = document.getElementById("tipo-dolar");
const compraTabla = document.getElementById("valor-compra");
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


//resetear datos arrays
function borrarAray(){
     nombresDolar = [];
     ventaDolar = [];
     compraDolar = [];

}

 //prueba de una lista que muestre los valores de venta de cada tipo de dolar
function imprimirDolar(){
    
}


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
      borrarAray();
      conseguirDatos();
}
idObtener()