
from copy import copy
import json
from razones import RazonRetiroEfectivo


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
          
    def obtenerTransacciones(self):
        with open(self.archivo,"r") as file:
            datos = json.load(file)
            for x in datos["transacciones"]:
                listado.append(copy(x))
        return listado
    
    def ObtenerRazon(self,cliente):
        with open(self.archivo,"r") as file:
            datos = json.load(file)
            transacciones = datos["transacciones"]
            for x in transacciones:
                if x["estado"] == "RECHAZADA" and x["tipo"] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                    RazonRetiroEfectivo().resolver(cliente=cliente,transaccion=x)
                elif x["estado"] == "RECHAZADA" and x["tipo"] == 'ALTA_CHEQUERA':
                    listado.append(copy(x)) #poner razon
                elif x["estado"] == "RECHAZADA" and x["tipo"] == 'ALTA_TARJETA_CREDITO':
                    listado.append(copy(x)) #poner razon
                elif x["estado"] == "RECHAZADA" and x["tipo"] == 'COMPRA_DOLAR':
                    listado.append(copy(x)) #poner razon
                elif x["estado"] == "RECHAZADA" and x["tipo"] == 'TRANSFERENCIA_ENVIADA':
                    listado.append(copy(x)) #poner razon
                elif x["estado"] == "RECHAZADA" and x["tipo"] == 'TRANSFERENCIA_RECIBIDA':
                    listado.append(copy(x)) #poner razon
    
    
    def obtenerDireccion(self,dato):
        with open(self.archivo,"r") as file:
            datos = json.load(file)
            return datos["direccion"][dato]   
        
        
x = Json(eventos_black).ObtenerRazon()
print(listado)
    
            



        


