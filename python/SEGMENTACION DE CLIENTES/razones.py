
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
                transaccion["razon"] = ""
                RazonAltaTarjetaCredito.aprobados.append(transaccion)
        else:
            transaccion["razon"] = 'este usuario no tiene permitido crear tarjetas de credito'
            RazonAltaTarjetaCredito.rechazados.append(transaccion)



class RazonCompraDolar(Razon):
    def __init__(self, type=None) -> None:
        super().__init__(type)
        
    aprobados, rechazados = [],[]
    
    def resolver(self, cliente, transaccion):
        super().resolver(cliente)
        if cliente.puede_comprar_dolar() is False :
            transaccion["razon"] = "cliente no habilitado para comprar dolares, debe ser BLACK o GOLD"
            RazonCompraDolar.rechazados.append(transaccion)
        elif transaccion["monto"] > transaccion["saldoEnCuenta"]:
            transaccion["razon"] = "Limite de saldo alcanzado"
            RazonCompraDolar.rechazados.append(transaccion)
        else:
            transaccion["razon"] = ""
            RazonCompraDolar.aprobados.append(transaccion)

                    

class RazonRetiroEfectivo(Razon):
    def __init__(self, type=None) -> None:
        super().__init__(type)
        
    aprobados, rechazados = [], []
    
    def resolver(self, cliente, transaccion):
        super().resolver(cliente)
        if transaccion["cupoDiarioRestante"] < transaccion["monto"]:
            transaccion["razon"] = f"Cupo diario de extraccion superado, no puede superar los ${transaccion['cupoDiarioRestante']} por dia"
            RazonRetiroEfectivo.rechazados.append(transaccion)
        elif transaccion["saldoEnCuenta"] <= transaccion["monto"]:
            transaccion["razon"] = "Saldo insuficiente"
            RazonRetiroEfectivo.rechazados.append(transaccion)
        else:
            transaccion["razon"] = ""
            RazonRetiroEfectivo.aprobados.append(transaccion)
            
                    
                    


class RazonTransferenciaEnviada(Razon):
    def __init__(self, type=None) -> None:
        super().__init__(type)
        
    aprobados, rechazados = [], []
    
    def resolver(self, cliente,transaccion):
        super().resolver(cliente)

        if cliente.cuenta_corriente is False:
            if (transaccion["monto"]+(self.cliente.caja_ahorro.costo_transferencias*transaccion["monto"])) > transaccion["saldoEnCuenta"]:
                transaccion["razon"] = f"Saldo insuficiente, en las cuentas {self.cliente.tipo} el saldo no puede quedar negativo"
                RazonTransferenciaEnviada.rechazados.append(transaccion)
            else:
                transaccion["razon"] = ""
                RazonTransferenciaEnviada.aprobados.append(transaccion)
        else:
            if (transaccion["monto"]+(self.cliente.caja_ahorro.costo_transferencias*transaccion["monto"])) > (transaccion["saldoEnCuenta"] + self.cliente.cuenta_corriente.limite_extraccion_diario):
                transaccion["razon"] = f"Saldo en cuenta insuficiente"
                RazonTransferenciaEnviada.rechazados.append(transaccion)
            else:
                transaccion["razon"] = ""
                RazonTransferenciaEnviada.aprobados.append(transaccion)

class RazonTransferenciaRecibida(Razon):
    def __init__(self, type=None) -> None:
        super().__init__(type)
        
    aprobados, rechazados = [], []
    
    def resolver(self, cliente,transaccion):
        super().resolver(cliente)
        if transaccion["monto"] > self.cliente.caja_ahorro.limite_transferencia_recibida and self.cliente.caja_ahorro.limite_transferencia_recibida != 0:
            transaccion["razon"] = "Limite de transferecia recibida excedido, debe pedir autorizacion al banco para realizar transferencias tan grandes"
            RazonTransferenciaRecibida.rechazados.append(transaccion)
        else:
            transaccion["razon"] = ""
            RazonTransferenciaRecibida.aprobados.append(transaccion)
        
def razones(archivo,cliente):
    transacciones = archivo.obtenerTransacciones() #obtengo las transacciones del archivo que parsee
    lista = []
    for x in transacciones:  #itero sobre las transacciones
           #separacion por operacion
        if x['tipo'] == 'ALTA_CHEQUERA':
            RazonAltaChequera().resolver(transaccion=x, cliente=cliente)
            # lista += (RazonAltaChequera().aprobados + RazonAltaChequera().rechazados)
            
        elif x['tipo'] == 'ALTA_TARJETA_CREDITO':
            RazonAltaTarjetaCredito().resolver(transaccion=x, cliente=cliente)
            # lista += (RazonAltaTarjetaCredito().aprobados + RazonAltaTarjetaCredito().rechazados)
        elif x['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
            RazonRetiroEfectivo().resolver(transaccion=x, cliente=cliente)
            # lista += (RazonRetiroEfectivo().aprobados + RazonRetiroEfectivo().rechazados)
        elif x['tipo'] == 'COMPRA_DOLAR':
            RazonCompraDolar().resolver(transaccion=x,cliente=cliente)
            # lista += (RazonCompraDolar().aprobados + RazonCompraDolar().rechazados)
        elif x["tipo"] == "TRANSFERENCIA_ENVIADA":
            RazonTransferenciaEnviada().resolver(transaccion=x, cliente=cliente)
            # lista += (RazonTransferenciaEnviada().aprobados + RazonTransferenciaEnviada().rechazados)
        elif x["tipo"] == "TRANSFERENCIA_RECIBIDA":
            RazonTransferenciaRecibida().resolver(transaccion=x, cliente=cliente)
            # lista += (RazonTransferenciaRecibida().aprobados + RazonTransferenciaRecibida().rechazados)
    lista = (RazonAltaChequera().aprobados + RazonAltaChequera().rechazados + RazonAltaTarjetaCredito().aprobados + RazonAltaTarjetaCredito().rechazados + RazonRetiroEfectivo().aprobados + RazonRetiroEfectivo().rechazados + RazonCompraDolar().aprobados + RazonCompraDolar().rechazados + RazonTransferenciaEnviada().aprobados + RazonTransferenciaEnviada().rechazados + RazonTransferenciaRecibida().aprobados + RazonTransferenciaRecibida().rechazados)
    print(len(lista))
    return lista
    