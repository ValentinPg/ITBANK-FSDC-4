from ast import Pass
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
    
        
    def obtenerDatos(self,dato):
        with open(self.archivo,"r") as file:
            datos = json.load(file)
            return datos[dato]
    aaa = []    
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
            



        


