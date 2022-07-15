

# #defino la clase Madre

class Cuenta(object):
    def __init__(self,limite_extraccion_diario=0,limite_transferencia_recibida=0,monto=0,costo_transferencias=0,saldo_descubierto_disponible=0):
        try:
            self.limite_extraccion_diario = float(limite_extraccion_diario)
            self.limite_transferencia_recibida = float(limite_transferencia_recibida)
            self.monto = float(monto)
            self.costo_transferencias = float(costo_transferencias)
            self.saldo_descubierto_disponible = float(saldo_descubierto_disponible)
        except ValueError:
            print("el valor ingresado debe ser un numero")
            exit()

class Cuenta_corriente(Cuenta):    #esta cuenta es nada mas para los usuarios Black y Gold
    def __init__(self,saldo_descubierto_disponible, limite_extraccion_diario=0, limite_transferencia_recibida=0, monto=0, costo_transferencias=0,):
        super().__init__(limite_extraccion_diario, limite_transferencia_recibida, monto, costo_transferencias, saldo_descubierto_disponible)
        # Hay que especificar si o si el saldo desucbierto disponible
        #el saldo descubierto disponible puede ser NEGATIVO
                        
class Caja_ahorro(Cuenta):
    def __init__(self, saldo_caja, limite_extraccion_diario=0, limite_transferencia_recibida=0, monto=0, costo_transferencias=0, saldo_descubierto_disponible=0):
        super().__init__(limite_extraccion_diario, limite_transferencia_recibida, monto, costo_transferencias, saldo_descubierto_disponible)
        self.saldo_caja = saldo_caja #el saldo_caja es siempre el "saldoEnCuenta", no importa si se repite en el caso de las cuentas Gold y Black
        #El monto extraido JAMÁS puede superar el saldo caja
        
class Caja_dolares: #clase unica de los Gold y Black
    pass #IMPORTANTE: no se puden transferir ni recibir dolares, solo comprar
        
        
        
#RECOMIENDO: Usemos el saldo en caja de ahorro para operacionesd de extraccion y que para transferencias usemos el saldo descubierto de cuenta corriente, salvo que el usuario se classic.