from ast import Return
from copy import copy
from http import client
from moduloCuenta import Cuenta_corriente,Caja_ahorro,Caja_dolares
from direccion import Direccion
from JSONprueba import Json,eventos_black,eventos_classic,eventos_gold


class Razon(object):
    def __init__(self, cliente,listado) -> None:
        self.listado = listado
        self.cliente = cliente
    
    def resolver(self):
        pass
    

        
    # def verificar(self):
    #     listado = list(filter(lambda x : x["estado"] == "RECHAZADA",self.transacciones))
    #     for x in listado:    
    #         if x["tipo"] == "ALTA_CHEQUERA":
    #             RazonAltaChequera(self.cliente,listado).verificar()
    #         elif x["tipo"] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
    #             RazonRetiroEectivo(self.cliente,listado).verificar() 
    #         elif x["tipo"] == "ALTA_TARJETA_CREDITO":
    #             RazonAltaTarjetaCredito(self.cliente,listado).verificar()
    #         elif x["tipo"] == "COMPRAR_DOLAR":
    #             RazonCompraDolar(self.cliente,listado).verificar()
    #         elif x["tipo"] == "TRANSFERENCIA_ENVIADA":
    #             RazonTransferenciaEnviada(self.cliente,listado).verificar()
    #         elif x["tipo"] == "TRANSFERENCIA_RECIBIDA":
    #             RazonTransferenciaRecibida(self.cliente,listado).verificar()
    #         print("AAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
 
        
class RazonAltaChequera(Razon):
    def __init__(self, cliente, listado) -> None:
        super().__init__(cliente, listado)
        
    def resolver(self):
        for x in self.listado:
            if x["tipo"] == "ALTA_CHEQUERA":
                if x["totalChequerasActualmente"] >= self.cliente.maxChequera:
                    print ("Limite de chequeras alcanzado")
                    
                else:
                    pass

class RazonAltaTarjetaCredito(Razon):
    def __init__(self, cliente, listado) -> None:
        super().__init__(cliente, listado)
        
    def resolver(self):
        for x in self.listado:
            if x["tipo"] == "ALTA_TARJETA_CREDITO":
                if x["totalTarjetasDeCreditoActualmente"] >= self.cliente.maxCredito:
                    print ("Limite de trajetas de credito alcanzado")
                    
                else:
                    pass


class RazonCompraDolar(Razon):
    def __init__(self, cliente, listado) -> None:
        super().__init__(cliente, listado)
        
    def resolver(self):
        for x in self.listado:
            if x["tipo"] == "COMPRAR_DOLAR":
                if self.cliente.puede_comprar_dolar() == False:
                   pass
                else:
                    print ("Esta cuenta no esta habilitada para comprar dolares")
                    

class RazonRetiroEectivo(Razon):
    def __init__(self, cliente, listado) -> None:
        super().__init__(cliente, listado)
        
    def resolver(self):
            for x in self.listado:
                if x["tipo"] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                    if x["cupoDiarioRestante"]-(x["monto"]*self.cliente.caja_ahorro.costo_transferencias) < x["monto"]:
                        print ("Limite diario alcanzado")
                    else:
                        pass

class RazonTransferenciaEnviada(Razon):
    def __init__(self, cliente, listado) -> None:
        super().__init__(cliente, listado)

    def resolver(self):
        if self.cliente.tipo == "CLASSIC":
            for x in self.listado:
                if x["tipo"] == "TRANSFERENCIA_ENVIADA":
                    if x["cupoDiarioRestante"]-(x["monto"]*self.cliente.caja_ahorro.costo_transferencias) < x["monto"]:
                        print ("Limite diario transferencias alcanzado")
                        
        else:
            for x in self.listado:
                if x["tipo"] == "TRANSFERENCIA_ENVIADA":
                    if x["saldoEnCuenta"]-(x["monto"]*self.cliente.cuenta_corriente.costo_transferencias) < self.cliente.cuenta_corriente.limite_extraccion_diario:
                        print ("Limite diario transferencias alcanzado")
                        
        

class RazonTransferenciaRecibida(Razon):
    def __init__(self, cliente, listado) -> None:
        super().__init__(cliente, listado)
        
    def resolver(self):
        for x in self.listado:
            if x["tipo"] == "TRANSFERENCIA_RECIBIDA":
                if x["monto"] > self.cliente.caja_ahorro.limite_transferencia_recibida:
                    print (f"El cliente solo tiene permitido recibir ${self.cliente.caja_ahorro.limite_transferencia_recibida} sin autorizacion previa")
                else:
                    pass