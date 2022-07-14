

#defino la clasee Madre
class Cuenta(object):
    def __init__(self,tipo_cliente,limite_extraccion_diario=0,limite_transferencia_recibida=0,monto=0,costo_transferencias=0,saldo_descubierto_disponible=0) -> None:
        try:
            self.limite_extraccion_diario = float(limite_extraccion_diario)
            self.limite_transferencia_recibida = float(limite_transferencia_recibida)
            self.monto = float(monto)
            self.costo_transferencias = float(costo_transferencias)
            self.saldo_descubierto_disponible = float(saldo_descubierto_disponible)
        except ValueError:
            print("el valor ingresado debe ser un numero")
            exit()
        self.tipo_cliente = tipo_cliente
#subclase 1    
class Caja_ahorro_pesos(Cuenta):
    
    #metodo para verificar el limite de extraccion de el individuo
    def limiteExtraccion(self):
        
        #funcion auxiliar que me ayuda a calcular el limite de extraccion
        def prueboExtraccion(self):
            if self.monto > self.limite_extraccion_diario:
                print("ERROR: Limite de extraccion diario superado")
        
        #el limite de extraccion cambia segun el tipo de cliente
        try:
            if self.tipo_cliente == "CLASSIC":
                self.limite_extraccion_diario = 10000
                prueboExtraccion(self)
                #falta imprimir resultado en el HTML
            elif self.tipo_cliente == "GOLD":
                self.limite_extraccion_diario = 20000
                prueboExtraccion(self)
                #falta imprimir resultado en el HTML
            elif self.tipo_cliente == "BLACK":
                self.limite_extraccion_diario = 100000
                prueboExtraccion(self)
                #falta imprimir resultado en el HTML
            else:
                raise TypeError
        except TypeError:
            print (f"El tipo de cliente '{self.tipo_cliente}' no existe")
            
        
#Subclase 2
class Caja_ahorro_dolares(Cuenta):
    pass
#Subclase 3
class Cuenta_corriente(Cuenta):
    pass

Caja_ahorro_pesos(tipo_cliente="CLASSIC", monto=10, limite_extraccion_diario=10).limiteExtraccion()