const tablaDolar = document.getElementById("pruebas");
const URLApi = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
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
        //Debug
        console.log(ventaDolar);
        console.log(nombresDolar);
        console.log(compraDolar);

    })
}
conseguirDatos()
setInterval(borrarAray, 60000)
setInterval(conseguirDatos,60000)

//resetear datos arrays
function borrarAray(){
     nombresDolar = [];
     ventaDolar = [];
     compraDolar = [];

}

 //prueba de una lista que muestre los valores de venta de cada tipo de dolar
function imprimirDolar(){
    let lista = nombresDolar.forEach(element => {
        let valores = document.createElement("div");
        tablaDolar.appendChild(valores);
        valores.innerHTML = element + "= " + ventaDolar[nombresDolar.indexOf(element)];
    });
    
}


//Funcion para visualizar la seccion de cotizaciones
function visualizacionOn() {
    document.getElementById('visualizacion').style.display = 'inline-block'
}

function idObtener() {
    document.querySelectorAll(".click").forEach(el => {
        el.addEventListener("click", e => {
          const id = e.target.getAttribute("id");
          let typeDolar = document.getElementById(id).innerHTML
          console.log(typeDolar);
          for(let i of nombresDolar){
            if(i == nombresDolar){
                console.log("hola")
            }
          }
        });
      });
}