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
            
# x = Json(eventos_gold)
# a = x.obtenerTransacciones("tipo")
# print(a)

# print(Json(eventos_black).obtenerTransacciones())
# print(Json(eventos_black).obtenerDatos("tipo"))

# print(Json(eventos_black).obtenerDireccion("calle"))

# transacciones = Json(eventos_classic).obtenerTransacciones()
# aprobados, rechazados = [],[]
# for key in transacciones:
#     if key["tipo"] == "ALTA_CHEQUERA":
#         try:
#             if key["totalChequerasActualmente"] >= self.cliente.maxChequera:
#                 key["razon"] = "ha superado el limte de chequeras"
#                 rechazados.append(key)
                
#             else:
#                 aprobados.append(key)
#         except Exception:
#             key["razon"] = 'este usuario no tiene permitido crear chequeras'
#             rechazados.append(key)

        


