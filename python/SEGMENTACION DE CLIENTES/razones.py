
class Razon(object):
    def __init__(self,type = None) -> None:
        self.type = str(type)
        
    def resolver(self, cliente):
        self.cliente = cliente

class RazonAltaChequera(Razon):
    def __init__(self, type=None) -> None:
        super().__init__(type)
    
    aprobados, rechazados = [],[]
    
    def resolver(self, cliente):
        self.cliente = cliente
        for key in self.cliente.transacciones:
            if key["tipo"] == "ALTA_CHEQUERA":
                try:
                    if key["totalChequerasActualmente"] >= self.cliente.maxChequera:
                        key["razon"] = f"limite de chequeras alcanzado, limite: {self.cliente.maxChequera}"
                        RazonAltaChequera.rechazados.append(key)
                    else:
                        RazonAltaChequera.aprobados.append(key)
                except Exception:
                        key["razon"] = 'este usuario no tiene permitido crear chequeras'
                        RazonAltaChequera.rechazados.append(key)

 



class RazonAltaTarjetaCredito(Razon):
    def __init__(self, type=None) -> None:
        super().__init__(type)
    
    aprobados, rechazados = [],[]
    
    def resolver(self, cliente):
        super().resolver(cliente)
        for key in self.cliente.transacciones:
            if key["tipo"] == "ALTA_TARJETA_CREDITO":
                try:
                    if key["totalTarjetasDeCreditoActualmente"] >= self.cliente.maxCredito:
                        key["razon"] = f"limte de tarjetas de credito alcanzado, limite: {self.cliente.maxCredito}"
                        RazonAltaTarjetaCredito.rechazados.append(key)
                    else:
                        RazonAltaTarjetaCredito.aprobados.append(key)
                except Exception:
                        key["razon"] = 'este usuario no tiene permitido crear tarjetas de credito'
                        RazonAltaTarjetaCredito.rechazados.append(key)

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
                    key["razon"] = f"El monto solicitado excede el cupo diario"
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
                        key["razon"] = f" El saldo restante en cuenta es insuficiente para cubrir el coste de transeferencia: coste de transferencia: {self.cliente.caja_ahorro.costo_transferencias*key['monto']}"
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