from moduloCliente import Cliente_black,Cliente_clasico,Cliente_gold
from copy import copy
import json

eventos_black= "python\ejemplos_json\eventos_black.json"
eventos_gold = "python\ejemplos_json\eventos_gold.json"
eventos_classic = "python\ejemplos_json\eventos_classic.json"
listado = []
razones = []

class Json(object):
    
    def __init__(self, archivo) -> None:
        self.archivo = archivo
        with open(self.archivo, "r") as file: #abro el archivo una sola vez y guardo todo en atributos
            datos = json.load(file)
            self.nombre = datos["nombre"]
            self.apellido = datos["apellido"]
            self.tipo = datos["tipo"]
            self.numero = datos["numero"]
            self.dni = datos["dni"]
    
        
    def obtenerDatos(self,dato):
        with open(self.archivo,"r") as file:
            datos = json.load(file)
            return datos[dato]
 
    def obtenerTransacciones(self):
        with open(self.archivo,"r") as file:
            datos = json.load(file)
            for x in datos["transacciones"]:
                listado.append(copy(x))
        return listado
    
    def ObtenerRazon(self):
        with open(self.archivo,"r") as file:
            datos = json.load(file)
            for x in datos["transacciones"]:
                if x["estado"] == "RECHAZADA":
                    pass
    
    def obtenerDireccion(self,dato):
        with open(self.archivo,"r") as file:
            datos = json.load(file)
            return datos["direccion"][dato] 
        
        
        
        
def iniciarPrograma(archivo):
    archivo = archivo.upper()
    
    if archivo == "CLASSIC":
        print(archivo)
        archivo = eventos_classic
        cargado = Json(archivo)
        return Cliente_clasico(cargado,nombre=cargado.nombre,apellido=cargado.apellido,numero=cargado.apellido,dni=cargado.dni,tipo=cargado.tipo)
    elif archivo == "GOLD":
        print(archivo)
        archivo = eventos_gold
        cargado = Json(archivo)
        return Cliente_gold(cargado,nombre=cargado.nombre,apellido=cargado.apellido,numero=cargado.apellido,dni=cargado.dni,tipo=cargado.tipo)
    elif archivo == "BLACK":
        print(archivo)
        archivo = eventos_black
        cargado = Json(archivo)
        return Cliente_black(cargado,nombre=cargado.nombre,apellido=cargado.apellido,numero=cargado.apellido,dni=cargado.dni,tipo=cargado.tipo)
    else:
        print("archivo no reconocido")
 
            



        


