from JSONprueba import eventos_black,eventos_classic,eventos_gold
from moduloCliente import Cliente_black,Cliente_clasico,Cliente_gold
from print_HTML import plantillaHTML
from JSONprueba import Json



#-------------------------Ingrese el archivo que se desea escanear (eventos_classic,eventos_gold,eventos_black)---------------------------------------------------------#
archivo = input("Ingrese el archivo que desea leer: ")

def iniciarPrograma(archivo):
    archivo = archivo.upper()
    
    if archivo == "CLASSIC":
        print(archivo)
        archivo = eventos_classic
        cargado = Json(archivo)
        return Cliente_clasico(eventos_classic,nombre=cargado.nombre,apellido=cargado.apellido,numero=cargado.apellido,dni=cargado.dni,tipo=cargado.tipo)
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