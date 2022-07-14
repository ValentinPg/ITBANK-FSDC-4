

#defino la clasee Madre
from asyncio.windows_events import INFINITE
from json.encoder import INFINITY


class Cuenta(object):
    def __init__(self,tipo_cliente,limite_extraccion_diario=0,limite_transferencia_recibida=0,monto=0,costo_transferencias=0,saldo_descubierto_disponible=0):
        try:
            self.limite_extraccion_diario = float(limite_extraccion_diario)
            self.limite_transferencia_recibida = float(limite_transferencia_recibida)
            self.monto = float(monto)
            self.costo_transferencias = float(costo_transferencias)
            self.saldo_descubierto_disponible = float(saldo_descubierto_disponible)
            self.tipo_cliente = tipo_cliente
            
            if self.tipo_cliente != "CLASSIC" and self.tipo_cliente != "GOLD" and self.tipo_cliente != "BLACK":
                raise TypeError
        except ValueError:
            print("el valor ingresado debe ser un numero")
            exit()
        except TypeError:
            print (f"El tipo de cliente '{self.tipo_cliente}' no existe")
            
        
#subclase 1    
class Caja_ahorro_pesos(Cuenta):
    def __init__(self, tipo_cliente, limite_extraccion_diario=0, limite_transferencia_recibida=0, monto=0, costo_transferencias=0, saldo_descubierto_disponible=0):
        super().__init__(tipo_cliente, limite_extraccion_diario, limite_transferencia_recibida, monto, costo_transferencias, saldo_descubierto_disponible)
        #la caja de ahorros no puede quedar en negativo
        if self.monto >= self.saldo_descubierto_disponible:
            print("no hay suficiente saldo disponible en la Caja de Ahorros para realizar la operacion")
            exit()
    
    
    #metodo para verificar el limite de extraccion de el individuo
    def limiteExtraccion(self):  
        #funcion auxiliar que me ayuda a calcular el limite de extraccion
        def prueboExtraccion(self):
            if self.monto > self.limite_extraccion_diario:
                print("ERROR: Limite de extraccion diario superado")
                
        
        #el limite de extraccion cambia segun el tipo de cliente
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
        self.saldo_descubierto_disponible = self.saldo_descubierto_disponible-self.monto-self.costoTransferencia()
        return self.saldo_descubierto_disponible
    
           
    #metodo para verificar la recepcion del dinero       
    def limiteRecepcion(self):
        #metodo para verificar el limite de extraccion de el individuo
        def prueboRecepcion(self):
            if self.monto > self.limite_transferencia_recibida:
                print("ERROR: Superado el limite de transferencia permitido")
        
        if self.tipo_cliente == "CLASSIC":
            self.limite_transferencia_recibida = 150000
            prueboRecepcion(self)
            #falta imprimir resultado en el HTML
        elif self.tipo_cliente == "GOLD":
            self.limite_transferencia_recibida = 500000
            prueboRecepcion(self)
            #falta imprimir resultado en el HTML
        elif self.tipo_cliente == "BLACK":
            self.limite_transferencia_recibida = self.monto + 1
            prueboRecepcion(self)
            #falta imprimir resultado en el HTML
        self.saldo_descubierto_disponible = self.saldo_descubierto_disponible+self.monto-self.costoTransferencia()
        return self.saldo_descubierto_disponible
    
    
    #metodo que calcula el costo de la transferencia
    def costoTransferencia(self):
        #asigno los procentajes de comision
        if self.tipo_cliente == "CLASSIC":
            porcentaje = 0.01
        elif self.tipo_cliente == "GOLD":
            porcentaje = 0.005
        elif self.tipo_cliente == "BLACK":
            porcentaje = 0
        costoDebitado =self.monto*porcentaje
        print(f"Se toman ${costoDebitado} debido a gastos de gestion de la transferencia")
        return costoDebitado
    
    def __str__(self) -> str:
        return f"La caja de ahorro tiene un saldo de ${self.saldo_descubierto_disponible}"
            
        
#Subclase 2
class Caja_ahorro_dolares(Cuenta):
    pass
#Subclase 3
class Cuenta_corriente(Cuenta):
    pass




#pRUEBa
xa = Caja_ahorro_pesos(tipo_cliente="BLACK", monto=1, saldo_descubierto_disponible=0)
xa = xa.limiteRecepcion()
print(xa)
