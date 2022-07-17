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
        


class Cuenta_clasica(Cliente):
    def __init__(self) -> None:
        super().__init__()

    def puede_crear_cheuqera():
        return False
    def puede_crear_tarjeta_credito():
        return True
    def puede_comprar_dolar():
        return False

class Cuenta_gold(Cliente):
        def puede_crear_cheuqera():
            return False
        def puede_crear_tarjeta_credito():
            return True
        def puede_comprar_dolar():
            return False

class Cuenta_black(Cliente):
        def puede_crear_cheuqera():
            return True
        def puede_crear_tarjeta_credito():
            return True
        def puede_comprar_dolar():
            return True

usuario_1 = Cuenta_clasica
usuario_1.obtener_nombre('lucas')
