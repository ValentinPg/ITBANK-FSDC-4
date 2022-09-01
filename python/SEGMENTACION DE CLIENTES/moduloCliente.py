
from moduloCuenta import Cuenta_corriente,Caja_ahorro,Caja_dolares
from direccion import Direccion
from JSONprueba import Json,eventos_black,eventos_classic,eventos_gold




class Cliente():
    def __init__(self,archivo, nombre, apellido, numero,dni,tipo = None) -> None:
        self.archivo = Json(archivo)
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni
        self.tipo = tipo
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
    def __init__(self, archivo, nombre, apellido, numero, dni, tipo=None) -> None:
        super().__init__(archivo, nombre, apellido, numero, dni, tipo)
        self.caja_ahorro = Caja_ahorro(limite_extraccion_diario=10000,costo_transferencias=0.01,limite_transferencia_recibida=150000)
        self.cuenta_corriente = False

    def puede_crear_cheuqera(self):
        return False
    def puede_crear_tarjeta_credito(self):
        return False
    def puede_comprar_dolar(self):
        return False

class Cliente_gold(Cliente):
    def __init__(self, archivo, nombre, apellido, numero, dni, tipo=None) -> None:
        super().__init__(archivo, nombre, apellido, numero, dni, tipo)
        self.caja_ahorro = Caja_ahorro(costo_transferencias=0.05,limite_extraccion_diario=20000,limite_transferencia_recibida=500000)
        self.cuenta_corriente = Cuenta_corriente(limite_extraccion_diario=-10000,costo_transferencias=0.005,limite_transferencia_recibida=500000)
        self.caja_dolares = Caja_dolares()
        self.maxCredito = 1
        self.maxChequera = 1
        
    def puede_crear_cheuqera(self):
        return True
    def puede_crear_tarjeta_credito(self):
        return True
    def puede_comprar_dolar(self):
        return True

class Cliente_black(Cliente):
    def __init__(self, archivo, nombre, apellido, numero, dni, tipo=None) -> None:
        super().__init__(archivo, nombre, apellido, numero, dni, tipo)
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
    
# print(Cliente_black(eventos_black).cuenta_corriente)



    