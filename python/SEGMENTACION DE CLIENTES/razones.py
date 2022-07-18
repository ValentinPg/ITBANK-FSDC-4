from ast import Return
from copy import copy
from moduloCuenta import Cuenta_corriente,Caja_ahorro,Caja_dolares
from direccion import Direccion
from JSONprueba import Json,eventos_black,eventos_classic,eventos_gold


class Razon(object):
    def __init__(self,cliente) -> None:
        self.cliente = cliente
        self.transacciones = cliente.transacciones
        self.motivo = None
        
    def verificar(self):
        for x in self.transacciones:    
            if x["tipo"] == "ALTA_CHEQUERA":
                RazonAltaChequera(self.cliente).verificar()
            elif x["tipo"] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                RazonRetiroEectivo(self.cliente).verificar() 
            elif x["tipo"] == "ALTA_TARJETA_CREDITO":
                RazonAltaTarjetaCredito(self.cliente).verificar()
            elif x["tipo"] == "COMPRAR_DOLAR":
                RazonCompraDolar(self.cliente).verificar()
            elif x["tipo"] == "TRANSFERENCIA_ENVIADA":
                RazonTransferenciaEnviada(self.cliente).verificar()
            elif x["tipo"] == "TRANSFERENCIA_RECIBIDA":
                RazonTransferenciaRecibida(self.cliente).verificar()
 
        
class RazonAltaChequera(Razon):
    def __init__(self, cliente) -> None:
        super().__init__(cliente)
        
    def verificar(self):
        for x in self.transacciones:
            if x["tipo"] == "ALTA_CHEQUERA":
                if x["totalChequerasActualmente"] >= self.cliente.maxChequera:
                    print ("Limite de chequeras alcanzado")
                    return copy(self.motivo)
                else:
                    print("normal")

class RazonAltaTarjetaCredito(Razon):
    def __init__(self, cliente) -> None:
        super().__init__(cliente)
        
    def verificar(self):
        for x in self.transacciones:
            if x["tipo"] == "ALTA_TARJETA_CREDITO":
                if x["totalTarjetasDeCreditoActualmente"] >= self.cliente.maxCredito:
                    print ("Limite de trajetas de credito alcanzado")
                    return copy(self.motivo)
                else:
                    print("normal")


class RazonCompraDolar(Razon):
    def __init__(self, cliente) -> None:
        super().__init__(cliente)
        
    def verificar(self):
        for x in self.transacciones:
            if x["tipo"] == "COMPRAR_DOLAR":
                if self.cliente.puede_comprar_dolar():
                   print("normal")
                else:
                    print ("Esta cuenta no esta habilitada para comprar dolares")
                    return copy(self.motivo)

class RazonRetiroEectivo(Razon):
    def __init__(self, cliente) -> None:
        super().__init__(cliente)
        
    def verificar(self):
            for x in self.transacciones:
                if x["tipo"] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                    if x["cupoDiarioRestante"]-(x["monto"]*self.cliente.caja_ahorro.costo_transferencias) < x["monto"]:
                        print ("Limite diario alcanzado")
                        return copy(self.motivo)
                    else:
                        print("normal")

class RazonTransferenciaEnviada(Razon):
    def __init__(self, cliente) -> None:
        super().__init__(cliente)

    def verificar(self):
        if self.cliente.tipo == "CLASSIC":
            for x in self.transacciones:
                if x["tipo"] == "TRANSFERENCIA_ENVIADA":
                    if x["cupoDiarioRestante"]-(x["monto"]*self.cliente.caja_ahorro.costo_transferencias) < x["monto"]:
                        print ("Limite diario transferencias alcanzado")
                        
        else:
            for x in self.transacciones:
                if x["tipo"] == "TRANSFERENCIA_ENVIADA":
                    if x["saldoEnCuenta"]-(x["monto"]*self.cliente.cuenta_corriente.costo_transferencias) < self.cliente.cuenta_corriente.limite_extraccion_diario:
                        print ("Limite diario transferencias alcanzado")
                        print(copy(self.motivo))
        

class RazonTransferenciaRecibida(Razon):
    def __init__(self, cliente) -> None:
        super().__init__(cliente)
        
    def verificar(self):
        for x in self.transacciones:
            if x["tipo"] == "TRANSFERENCIA_RECIBIDA":
                if x["monto"] > self.cliente.caja_ahorro.limite_transferencia_recibida:
                    print (f"El cliente solo tiene permitido recibir ${self.cliente.caja_ahorro.limite_transferencia_recibida} sin autorizacion previa")
                    print(copy(self.motivo))
                else:
                    print("normal")