
from moduloCuenta import Cuenta_corriente,Caja_ahorro,Caja_dolares
from direccion import Direccion

class Cliente():
    def __init__(self) -> None:
        pass
    
    def obtener_nombre(self,nombre):
        try:
            self.nombre = nombre
            print(self.nombre)
        except ValueError:
            print("No se ha encontrado el nombre del cliente")
            exit()

    def obtener_apellido(self,apellido):
        try:
            self.apellido = apellido
            print(self.apellido)
        except ValueError:
            print("No se ha encontrado el apellido del cliente")
            exit()

    def obtener_numero(self,numero):
        try:
            self.numero = numero
            print(self.numero)
        except ValueError:
            print("No se ha encontrado el numero del cliente")
            exit()
        

    def obtener_dni(self,dni):
        try:
            self.dni = dni
            print(self.dni)
        except ValueError:
            print("No se ha encontrado el DNI del cliente")
            exit()
        


class Cliente_clasico(Cliente):
    def __init__(self) -> None:
        super().__init__()
        self.caja_ahorro = Caja_ahorro(limite_extraccion_diario=10000,costo_transferencias=0.01,limite_transferencia_recibida=150000)

    def puede_crear_cheuqera():
        return False
    def puede_crear_tarjeta_credito():
        return True
    def puede_comprar_dolar():
        return False

class Cliente_gold(Cliente):
    def __init__(self) -> None:
        super().__init__()
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
    def __init__(self) -> None:
        super().__init__()
        self.caja_ahorro = Caja_ahorro(limite_extraccion_diario=100000)
        self.cuenta_corriente = Cuenta_corriente(limite_extraccion_diario=-10000)
        self.caja_dolares = Caja_dolares()
        
    def puede_crear_cheuqera():
            return True
    def puede_crear_tarjeta_credito():
            return True
    def puede_comprar_dolar():
            return True
