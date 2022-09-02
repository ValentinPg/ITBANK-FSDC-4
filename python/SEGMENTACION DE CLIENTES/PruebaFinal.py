from JSONprueba import eventos_black,eventos_classic,eventos_gold, iniciarPrograma
from moduloCliente import Cliente_black,Cliente_clasico,Cliente_gold
from print_HTML import plantillaHTML
from JSONprueba import Json



#-------------------------Ingrese el archivo que se desea escanear (eventos_classic,eventos_gold,eventos_black)---------------------------------------------------------#
archivo = input("Ingrese el archivo que desea leer: ")



x = iniciarPrograma(archivo)
plantillaHTML(x)
#--------------------------El archivo HTML se llama: indexpy.html (Caprpeta "SEGMENTACION CLIENTES"-------------------------------------------------------------------------------------------------------#