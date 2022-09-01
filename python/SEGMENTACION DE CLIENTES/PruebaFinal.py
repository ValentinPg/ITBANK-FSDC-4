from JSONprueba import Json,eventos_black,eventos_classic,eventos_gold
from moduloCliente import Cliente_black,Cliente_clasico,Cliente_gold
from print_HTML import obtenerRazones,plantillaHTML



#-------------------------Ingrese el archivo que se desea escanear (eventos_classic,eventos_gold,eventos_black)---------------------------------------------------------#
archivo = input("Ingrese el archivo que desea leer: ")

def iniciarPrograma(archivo):
    archivo = archivo.upper()
    if archivo == "CLASSIC":
        print(archivo)
        return Cliente_clasico(eventos_classic)
    elif archivo == "GOLD":
        print(archivo)
        return Cliente_gold(eventos_gold)
    elif archivo == "BLACK":
        print(archivo)
        return Cliente_black(eventos_black)
    else:
        print("archivo no reconocido")


 
x = iniciarPrograma(archivo)
plantillaHTML(x)
#--------------------------El archivo HTML se llama: indexpy.html (Caprpeta "SEGMENTACION CLIENTES"-------------------------------------------------------------------------------------------------------#