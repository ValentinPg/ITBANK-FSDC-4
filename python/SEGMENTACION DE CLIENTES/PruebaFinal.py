from JSONprueba import Json,eventos_black,eventos_classic,eventos_gold
from moduloCliente import iniciarPrograma

from print_HTML import obtenerRazones,plantillaHTML

#-------------------------Ingrese el archivo que se desea escanear (eventos_classic,eventos_gold,eventos_black)---------------------------------------------------------#
# archivo = input("Ingrese el archivo que quiere revisar: ")
# print(archivo)

cliente = iniciarPrograma(eventos_black)
Json(eventos_black).ObtenerRazon(cliente = cliente)
#--------------------------El archivo HTML se llama: indexpy.html (Caprpeta "SEGMENTACION CLIENTES"-------------------------------------------------------------------------------------------------------#