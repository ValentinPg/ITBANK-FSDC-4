
from moduloCuenta import Cuenta_corriente,Caja_ahorro,Caja_dolares
from direccion import Direccion
from JSONprueba import Json,eventos_black,eventos_classic,eventos_gold



class Cliente():
    def __init__(self,archivo) -> None:
        self.archivo = Json(archivo)
        self.nombre = self.archivo.obtenerDatos("nombre")
        self.apellido = self.archivo.obtenerDatos("apellido")
        self.numero = self.archivo.obtenerDatos("numero")
        self.dni = self.archivo.obtenerDatos("dni")
        self.direccion = Direccion(calle=self.archivo.obtenerDireccion("calle"),numero=self.archivo.obtenerDireccion("numero"),ciudad=self.archivo.obtenerDireccion("ciudad"), estado=self.archivo.obtenerDireccion("provincia"), cp=self.archivo.obtenerDireccion("pais"))
        self.transacciones = self.archivo.obtenerTransacciones()
        self.caja_ahorro = None
        self.cuenta_corriente = None
        self.caja_dolares = None
        
    def puede_crear_cheuqera():
        return False
    def puede_crear_tarjeta_credito():
        return True
    def puede_comprar_dolar():
        return False
    

        


class Cliente_clasico(Cliente):
    def __init__(self, archivo) -> None:
         super().__init__(archivo)
         self.caja_ahorro = Caja_ahorro(limite_extraccion_diario=10000,costo_transferencias=0.01,limite_transferencia_recibida=150000)

    def puede_crear_cheuqera():
        return False
    def puede_crear_tarjeta_credito():
        return True
    def puede_comprar_dolar():
        return False

class Cliente_gold(Cliente):
    def __init__(self, archivo) -> None:
        super().__init__(archivo)
        self.caja_ahorro = Caja_ahorro(costo_transferencias=0.05,limite_extraccion_diario=20000)
        self.cuenta_corriente = Cuenta_corriente(limite_extraccion_diario=-10000,costo_transferencias=0.005,limite_transferencia_recibida=500000)
        self.caja_dolares = Caja_dolares()
        
    def puede_crear_cheuqera():
            return False
    def puede_crear_tarjeta_credito():
            return True
    def puede_comprar_dolar():
            return False

class Cliente_black(Cliente):
    def __init__(self, archivo) -> None:
        super().__init__(archivo)
        self.caja_ahorro = Caja_ahorro(limite_extraccion_diario=100000)
        self.cuenta_corriente = Cuenta_corriente(limite_extraccion_diario=-10000)
        self.caja_dolares = Caja_dolares()
        
    def puede_crear_cheuqera():
            return True
    def puede_crear_tarjeta_credito():
            return True
    def puede_comprar_dolar():
            return True


def iniciarPrograma(archivo):
    file = Json(archivo)
    if file.obtenerDatos("tipo") == "CLASSIC":
        Cliente_clasico(archivo)
    elif file.obtenerDatos("tipo") == "GOLD":
        Cliente_gold(archivo)
    elif file.obtenerDatos("tipo") == "BLACK":
        Cliente_black(archivo)