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


//resetear datos arrays
function borrarAray(){
     nombresDolar = [];
     ventaDolar = [];
     compraDolar = [];

}

 //prueba de una lista que muestre los valores de venta de cada tipo de dolar
function imprimirDolar(){
    let lista = nombresDolar.forEach(element => {
        let valores = document.createElement("li");
        tablaDolar.appendChild(valores);
        valores.innerHTML = element + "= " + ventaDolar[nombresDolar.indexOf(element)];
    });
    
}

