from JSONprueba import Json,eventos_black
from moduloCliente import Cliente_black


class Razon(object):
    def __init__(self,type = None) -> None:
        self.type = str(type)
        
    def resolver(self, cliente):
        self.cliente = cliente

class RazonAltaChequera(Razon):
    def __init__(self, type=None) -> None:
        super().__init__(type)
    
    aprobados, rechazados = [],[]
    
    def resolver(self, cliente, transaccion):

        self.cliente = cliente
        if self.cliente.puede_crear_cheuqera():
            if transaccion["totalChequerasActualmente"] >= self.cliente.maxChequera:
                transaccion["razon"] = f"ha superado el limte de chequeras de su cuenta, el limite es {self.cliente.maxChequera}"
                RazonAltaChequera.rechazados.append(transaccion)
            else:
                transaccion["razon"] = ""
                RazonAltaChequera.aprobados.append(transaccion)
        else:
            transaccion["razon"] = 'este usuario no tiene permitido crear chequeras'
            RazonAltaChequera.rechazados.append(transaccion)

 



class RazonAltaTarjetaCredito(Razon):
    def __init__(self, type=None) -> None:
        super().__init__(type)
    
    aprobados, rechazados = [],[]
    
    def resolver(self, cliente, transaccion):
        super().resolver(cliente)
        if self.cliente.puede_crear_tarjeta_credito():
            if transaccion["totalTarjetasDeCreditoActualmente"] >= self.cliente.maxCredito:
                transaccion["razon"] = f"ha superado el limte de tarjetas de credito, el limite de esta cuenta es {self.cliente.maxCredito}"
                RazonAltaTarjetaCredito.rechazados.append(transaccion)
            else:
                RazonAltaTarjetaCredito.aprobados.append(transaccion)
        else:
            transaccion["razon"] = 'este usuario no tiene permitido crear tarjetas de credito'
            RazonAltaTarjetaCredito.rechazados.append(transaccion)



class RazonCompraDolar(Razon):
    def __init__(self, type=None) -> None:
        super().__init__(type)
        
    aprobados, rechazados = [],[]
    
    def resolver(self, cliente):
        super().resolver(cliente)
        for key in self.cliente.transacciones:
            if key["tipo"] == "COMPRA_DOLAR":
                if cliente.puede_comprar_dolar() is False :
                    key["razon"] = "cliente no habilitado para comprar dolares, debe ser BLACK o GOLD"
                    RazonCompraDolar.rechazados.append(key)
                elif key["monto"] > key["saldoEnCuenta"]:
                    key["razon"] = "Limite de saldo alcanzado"
                    RazonCompraDolar.rechazados.append(key)
                else:
                    RazonCompraDolar.aprobados.append(key)

                    

class RazonRetiroEfectivo(Razon):
    def __init__(self, type=None) -> None:
        super().__init__(type)
        
    aprobados, rechazados = [], []
    
    def resolver(self, cliente):
        super().resolver(cliente)
        for key in self.cliente.transacciones:
            if key["tipo"] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                if key["cupoDiarioRestante"] < key["monto"]:
                    key["razon"] = f"Cupo diario de extraccion superado, no puede superar los ${key['cupoDiarioRestante']} por dia"
                    RazonRetiroEfectivo.rechazados.append(key)
                elif key["saldoEnCuenta"] <= key["monto"]:
                    key["razon"] = "Saldo insuficiente"
                    RazonRetiroEfectivo.rechazados.append(key)
                else:
                    RazonRetiroEfectivo.aprobados.append(key)
                    
                    


class RazonTransferenciaEnviada(Razon):
    def __init__(self, type=None) -> None:
        super().__init__(type)
        
    aprobados, rechazados = [], []
    
    def resolver(self, cliente):
        super().resolver(cliente)
        for key in self.cliente.transacciones:
            if key["tipo"] == "TRANSFERENCIA_ENVIADA":
                if cliente.cuenta_corriente is False:
                    if (key["monto"]+(self.cliente.caja_ahorro.costo_transferencias*key["monto"])) > key["saldoEnCuenta"]:
                        key["razon"] = f"Saldo insuficiente, en las cuentas {self.cliente.tipo} el saldo no puede quedar negativo"
                        RazonTransferenciaEnviada.rechazados.append(key)
                    else:
                        RazonTransferenciaEnviada.aprobados.append(key)
                else:
                    if (key["monto"]+(self.cliente.caja_ahorro.costo_transferencias*key["monto"])) > (key["saldoEnCuenta"] + self.cliente.cuenta_corriente.limite_extraccion_diario):
                        key["razon"] = f"Saldo en cuenta insuficiente"
                        RazonTransferenciaEnviada.rechazados.append(key)
                    else:
                        RazonTransferenciaEnviada.aprobados.append(key)

class RazonTransferenciaRecibida(Razon):
    def __init__(self, type=None) -> None:
        super().__init__(type)
        
    aprobados, rechazados = [], []
    
    def resolver(self, cliente):
        super().resolver(cliente)
        for key in self.cliente.transacciones:
            if key["tipo"] == "TRANSFERENCIA_RECIBIDA":
                if key["monto"] > self.cliente.caja_ahorro.limite_transferencia_recibida and self.cliente.caja_ahorro.limite_transferencia_recibida != 0:
                    key["razon"] = "Limite de transferecia recibida excedido, debe pedir autorizacion al banco para realizar transferencias tan grandes"
                    RazonTransferenciaRecibida.rechazados.append(key)
                else:
                    RazonTransferenciaRecibida.aprobados.append(key)
        
        
      
cargado = Json(eventos_black)
cliente = Cliente_black(cargado,nombre=cargado.nombre,apellido=cargado.apellido,numero=cargado.apellido,dni=cargado.dni,tipo=cargado.tipo)                  
def razones(archivo,cliente):
    transacciones = archivo.obtenerTransacciones() #obtengo las transacciones del archivo que parsee
    for x in transacciones:  #itero sobre las transacciones
           #separacion por operacion
        if x['tipo'] == 'ALTA_CHEQUERA':
            RazonAltaChequera().resolver(transaccion=x, cliente=cliente)
            print(RazonAltaChequera.rechazados)
        elif x['tipo'] == 'ALTA_TARJETA_CREDITO':
            RazonAltaTarjetaCredito().resolver(transaccion=x, cliente=cliente)
            print(RazonAltaTarjetaCredito.aprobados)
        elif x['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
            pass
        elif x['tipo'] == 'COMPRA_DOLAR':
            pass
        elif x["tipo"] == "TRANSFERENCIA_ENVIADA":
            pass
        elif x["tipo"] == "TRANSFERENCIA_RECIBIDA":
            pass

            

razones(cliente=cliente,archivo=cargado)

    
