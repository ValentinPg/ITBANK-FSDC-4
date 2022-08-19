
from moduloCuenta import Cuenta_corriente,Caja_ahorro,Caja_dolares
from direccion import Direccion
from JSONprueba import Json,eventos_black,eventos_classic,eventos_gold
from razones import RazonAltaChequera



class Cliente():
    def __init__(self,nombre,apellido,numero,dni,tipo) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni
        self.tipo = tipo
        self.direccion = ""
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
    def __init__(self, nombre, apellido, numero, dni, tipo) -> None:
        super().__init__(nombre, apellido, numero, dni, tipo)
        self.caja_ahorro = Caja_ahorro(limite_extraccion_diario=10000,costo_transferencias=0.01,limite_transferencia_recibida=150000)

    def puede_crear_cheuqera(self):
        return False
    def puede_crear_tarjeta_credito(self):
        return True
    def puede_comprar_dolar(self):
        return False

class Cliente_gold(Cliente):
    def __init__(self, nombre, apellido, numero, dni, tipo) -> None:
        super().__init__(nombre, apellido, numero, dni, tipo)
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
    def __init__(self, nombre, apellido, numero, dni, tipo) -> None:
        super().__init__(nombre, apellido, numero, dni, tipo)
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
        return Cliente_clasico(nombre= file.obtenerDatos("nombre"), apellido=file.obtenerDatos("apellido"), numero=file.obtenerDatos("numero"), dni=file.obtenerDatos("dni"), tipo=file.obtenerDatos("tipo"))
    elif file.obtenerDatos("tipo") == "GOLD":
        return Cliente_gold(nombre= file.obtenerDatos("nombre"), apellido=file.obtenerDatos("apellido"), numero=file.obtenerDatos("numero"), dni=file.obtenerDatos("dni"), tipo=file.obtenerDatos("tipo"))
    elif file.obtenerDatos("tipo") == "BLACK":
        return Cliente_black(nombre= file.obtenerDatos("nombre"), apellido=file.obtenerDatos("apellido"), numero=file.obtenerDatos("numero"), dni=file.obtenerDatos("dni"), tipo=file.obtenerDatos("tipo"))
    