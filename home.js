const tablaDolar = document.getElementById("promociones");
const URLApi = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"

function precio_dolar(){
   let api = fetch(URLApi);

   let apiResponse = api.then(response => response.json());

   let  datosTabla = apiResponse.then(function(data) { console.log(data);

        let filtro = data.map(x => {if (x.casa.nombre.includes("Dolar")){

            return x.casa.nombre + " Compra= " + x.casa.compra + " Venta= " + x.casa.venta;

        } else {
            return x.casa.nombre + " Compra= " + x.casa.compra + " Venta= " + x.casa.venta;
            
        }});

        console.log(filtro);
    })
 
}