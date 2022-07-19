from ast import Return
from copy import copy
from http import client
from mimetypes import init
from moduloCuenta import Cuenta_corriente,Caja_ahorro,Caja_dolares
from direccion import Direccion
from JSONprueba import Json,eventos_black,eventos_classic,eventos_gold



# class Razon(object):
#     def __init__(self, archivo) -> None:
#         self.transacciones = archivo.obtenerTransacciones()
    
 
#     def resolver(self,cliente, evento):
#         self.evento = evento
#         self.cliente = cliente
#         for x in self.cliente.transacciones:
#             RazonAltaChequera(x).resolver(self.cliente,"ALTA_CHEQUERA")
#             # RazonRetiroEectivo(x).resolver(self.cliente,"RETIRO_EFECTIVO_CAJERO_AUTOMATICO") 
#             # RazonAltaTarjetaCredito(x).resolver(self.cliente,"ALTA_TARJETA_CREDITO")
#             # RazonCompraDolar(x).resolver(self.cliente,"COMPRAR_DOLAR")
#             # RazonTransferenciaEnviada(x).resolver(self.cliente,"TRANSFERENCIA_ENVIADA")
#             # RazonTransferenciaRecibida(x).resolver(self.cliente,"TRANSFERENCIA_RECIBIDA")
#         print("AAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHH")

        
# class RazonAltaChequera(Razon):
#     def __init__(self,diccionario, archivo=None) -> None:
#         self.diccionario = diccionario
        
#     def resolver(self,cliente,evento):
#         self.cliente = cliente
#         self.evento = evento
#         for x in self.diccionario:
#             if x["tipo"] == self.evento:
#                 if self.diccionario["totalChequerasActualmente"] >= self.cliente.maxChequera:
#                     print ("Limite de chequeras alcanzado")
                    
#                 else:
#                     pass

# class RazonAltaTarjetaCredito(Razon):
#     def __init__(self) -> None:
#         super().__init__()
        
#     def resolver(self,cliente,evento):
#         self.cliente = cliente
#         self.evento = evento
#         for x in self.cliente.transacciones:
#             if x["tipo"] == self.evento:
#                 if x["totalTarjetasDeCreditoActualmente"] >= self.cliente.maxCredito:
#                     return ("Limite de trajetas de credito alcanzado")
                    
#                 else:
#                     pass


# class RazonCompraDolar(Razon):
#     def __init__(self) -> None:
#         super().__init__()
        
#     def resolver(self,cliente,evento):
#         self.cliente = cliente
#         self.evento = evento
#         for x in self.cliente.transacciones:
#             if x["tipo"] ==  self.evento:
#                 if self.cliente.puede_comprar_dolar() == False:
#                    pass
#                 else:
#                     return ("Esta cuenta no esta habilitada para comprar dolares")
                    

# class RazonRetiroEectivo(Razon):
#     def __init__(self) -> None:
#         super().__init__()
        
#     def resolver(self,cliente,evento):
#         self.cliente = cliente
#         self.evento = evento
#         for x in self.cliente.transacciones:
#             if x["tipo"] ==  self.evento:
#                 if x["cupoDiarioRestante"]-(x["monto"]*self.cliente.caja_ahorro.costo_transferencias) < x["monto"]:
#                     return ("Limite diario alcanzado")
#                 else:
#                     pass

# class RazonTransferenciaEnviada(Razon):
#     def __init__(self) -> None:
#         super().__init__()

#     def resolver(self,cliente,evento):
#         self.cliente = cliente
#         self.evento = evento
#         if self.cliente.tipo == "CLASSIC":
#             for x in self.cliente.transacciones:
#                 if x["tipo"] ==  self.evento:
#                     if x["cupoDiarioRestante"]-(x["monto"]*self.cliente.caja_ahorro.costo_transferencias) < x["monto"]:
#                         return ("Limite diario transferencias alcanzado")
                        
#         else:
#             for x in self.cliente.transacciones:
#                 if x["tipo"] ==  self.evento:
#                     if x["saldoEnCuenta"]-(x["monto"]*self.cliente.cuenta_corriente.costo_transferencias) < self.cliente.cuenta_corriente.limite_extraccion_diario:
#                         return ("Limite diario transferencias alcanzado")
                        
        

# class RazonTransferenciaRecibida(Razon):
#     def __init__(self) -> None:
#         super().__init__()
        
#     def resolver(self,cliente,evento):
#         self.cliente = cliente
#         self.evento = evento
#         for x in self.cliente.transacciones:
#             if x["tipo"] ==  self.evento:
#                 if x["monto"] > self.cliente.caja_ahorro.limite_transferencia_recibida:
#                     return (f"El cliente solo tiene permitido recibir ${self.cliente.caja_ahorro.limite_transferencia_recibida} sin autorizacion previa")
#                 else:
#                     pass


class Razon(object):
    def __init__(self,type = None) -> None:
        self.type = str(type)
        
    def resolver(self, cliente):
        self.cliente = cliente

class RazonAltaChequera(Razon):
    def __init__(self, type=None) -> None:
        super().__init__(type)
    
    aprobados, rechazados = [],[]
    
    def resolver(self, cliente):
        super().resolver(cliente)
        for key in self.cliente.transacciones:
            if key["tipo"] == "ALTA_CHEQUERA":
                try:
                    if key["totalChequerasActualmente"] >= self.cliente.maxChequera:
                        key["razon"] = "ha superado el limte de chequeras"
                        RazonAltaChequera.rechazados.append(key)
                    else:
                        RazonAltaChequera.aprobados.append(key)
                except Exception:
                        key["razon"] = 'este usuario no tiene permitido crear chequeras'
                        RazonAltaChequera.rechazados.append(key)

 



class RazonAltaTarjetaCredito(Razon):
    pass

class RazonCompraDolar(Razon):
    pass

class RazonRetiroEectivo(Razon):
    pass

class RazonRetiroEectivo(Razon):
    pass

class RazonTransferenciaEnviada(Razon):
    pass

class RazonTransferenciaRecibida(Razon):
    pass