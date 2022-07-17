from copy import copy
from moduloCuenta import Cuenta_corriente,Caja_ahorro,Caja_dolares
from direccion import Direccion
from JSONprueba import Json,eventos_black,eventos_classic,eventos_gold
lista = []

class Razon(object):
    def __init__(self,cliente) -> None:
        self.cliente = cliente
        self.transacciones = cliente.transacciones
        
    def ejecucion(self):
        for x in self.transacciones:
            if x == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                RazonAltaChequera(self.cliente)
        
class RazonAltaChequera(Razon):
    def __init__(self, cliente) -> None:
        super().__init__(cliente)
        for x in self.transacciones:
            if x["totalChequerasActualmente"] >= cliente.maxChequera:
                print("Rechazo")
            else:
                print("Acepto")

class RazonAltaTarjetaCredito(Razon):
    pass

class RazonCompraDolar(Razon):
    pass

class RazonRetiroEectivo(Razon):
    pass

class RazonTransferenciaEnviada(Razon):
    pass

class RazonTransferenciaRecibida(Razon):
    pass