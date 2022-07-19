
from moduloCuenta import Cuenta_corriente,Caja_ahorro,Caja_dolares
from direccion import Direccion
from JSONprueba import Json,eventos_black,eventos_classic,eventos_gold
from razones import RazonAltaChequera



class Cliente():
    def __init__(self,archivo = None) -> None:
        self.archivo = Json(archivo)
        self.nombre = self.archivo.obtenerDatos("nombre")
        self.apellido = self.archivo.obtenerDatos("apellido")
        self.numero = self.archivo.obtenerDatos("numero")
        self.dni = self.archivo.obtenerDatos("dni")
        self.tipo = self.archivo.obtenerDatos("tipo")
        self.direccion = Direccion(calle=self.archivo.obtenerDireccion("calle"),numero=self.archivo.obtenerDireccion("numero"),ciudad=self.archivo.obtenerDireccion("ciudad"), estado=self.archivo.obtenerDireccion("provincia"), cp=self.archivo.obtenerDireccion("pais"))
        self.transacciones = self.archivo.obtenerTransacciones()
        self.maxCredito = 0
        self.maxChequera = 0
        self.caja_ahorro = None
        self.cuenta_corriente = None
        self.caja_dolares = None
        
    def puede_crear_cheuqera(self):
        return False
    def puede_crear_tarjeta_credito(self):
        return True
    def puede_comprar_dolar(self):
        return False
    

        


class Cliente_clasico(Cliente):
    def __init__(self, archivo) -> None:
        super().__init__(archivo)
        self.caja_ahorro = Caja_ahorro(limite_extraccion_diario=10000,costo_transferencias=0.01,limite_transferencia_recibida=150000)

    def puede_crear_cheuqera(self):
        return False
    def puede_crear_tarjeta_credito(self):
        return True
    def puede_comprar_dolar(self):
        return False

class Cliente_gold(Cliente):
    def __init__(self, archivo) -> None:
        super().__init__(archivo)
        self.caja_ahorro = Caja_ahorro(costo_transferencias=0.05,limite_extraccion_diario=20000,limite_transferencia_recibida=500000)
        self.cuenta_corriente = Cuenta_corriente(limite_extraccion_diario=-10000,costo_transferencias=0.005,limite_transferencia_recibida=500000)
        self.caja_dolares = Caja_dolares()
        self.maxCredito = 1
        self.maxChequera = 1
        
    def puede_crear_cheuqera(self):
        return False
    def puede_crear_tarjeta_credito(self):
        return True
    def puede_comprar_dolar(self):
        return False

class Cliente_black(Cliente):
    def __init__(self, archivo) -> None:
        super().__init__(archivo)
        self.caja_ahorro = Caja_ahorro(limite_extraccion_diario=100000)
        self.cuenta_corriente = Cuenta_corriente(limite_extraccion_diario=-10000)
        self.caja_dolares = Caja_dolares()
        self.maxCredito = 5
        self.maxChequera = 2
        
        
    def puede_crear_cheuqera(self):
        return True
    def puede_crear_tarjeta_credito(self):
        return True
    def puede_comprar_dolar(self):
        return True


def iniciarPrograma(archivo):
    file = Json(archivo)
    if file.obtenerDatos("tipo") == "CLASSIC":
        return Cliente_clasico(archivo)
    elif file.obtenerDatos("tipo") == "GOLD":
        return Cliente_gold(archivo)
    elif file.obtenerDatos("tipo") == "BLACK":
        return Cliente_black(archivo)
    
# x =iniciarPrograma(eventos_classic)
# Razon(x).verificar()
        
# print(Cliente_clasico(eventos_classic).transacciones)

# print(RazonAltaChequera(x,x.transacciones).resolver())
# print(RazonAltaTarjetaCredito(x,x.transacciones).resolver())
# print(RazonRetiroEectivo(x,x.transacciones).resolver())
# print(RazonCompraDolar(x,x.transacciones).resolver())
# print(RazonTransferenciaEnviada(x,x.transacciones).resolver())
# print(RazonTransferenciaRecibida(x,x.transacciones).resolver())

# for x in [RazonAltaChequera(x,x.transacciones).resolver(),RazonTransferenciaRecibida(x,x.transacciones).resolver(),RazonTransferenciaEnviada(x,x.transacciones).resolver(),RazonCompraDolar(x,x.transacciones).resolver(),RazonRetiroEectivo(x,x.transacciones).resolver(),RazonAltaTarjetaCredito(x,x.transacciones).resolver(),RazonAltaChequera(x,x.transacciones).resolver()]:
#     if x == None:
#         pass
#     else:
#         print(x)