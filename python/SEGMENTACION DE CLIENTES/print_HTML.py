from razones import razones
#variable que va a almacenar todas las transacciones
transeferencias = None

#funcion que junta todas las transacciones con sus razones de rechazo ya especificadas
# def obtenerRazones(cliente):
#     #invocamos las clases
#     RazonAltaChequera().resolver(cliente)
#     RazonTransferenciaRecibida().resolver(cliente)
#     RazonTransferenciaEnviada().resolver(cliente)
#     RazonRetiroEfectivo().resolver(cliente)
#     RazonCompraDolar().resolver(cliente)
#     RazonAltaTarjetaCredito().resolver(cliente)
#     #juntamos los valores de las listas
#     transeferencias = (RazonAltaChequera().rechazados + RazonAltaChequera().aprobados)
#     transeferencias +=(RazonAltaTarjetaCredito().rechazados + RazonAltaTarjetaCredito().aprobados)
#     transeferencias += (RazonCompraDolar().aprobados + RazonCompraDolar().rechazados)
#     transeferencias += (RazonRetiroEfectivo().aprobados + RazonRetiroEfectivo().rechazados)
#     transeferencias +=(RazonTransferenciaEnviada().rechazados + RazonTransferenciaEnviada().aprobados)
#     transeferencias +=(RazonTransferenciaRecibida().aprobados+ RazonTransferenciaRecibida().rechazados)
#     return transeferencias


def conversion(lista):
    
    for x in enumerate(lista):
        with open("python\SEGMENTACION DE CLIENTES\indexpy.html", "a+") as e:
            if x[1]['estado'] == 'RECHAZADA':
                if x[1]['tipo'] == 'ALTA_CHEQUERA':
                    e.write (f"""<p>{x[0]} | {x[1]['fecha']} | {x[1]['tipo']} | CUENTA NUMERO {x[1]['cuentaNumero']} | {x[1]['estado']} | motivo: {x[1]['razon']} chequeras actuales: {x[1]['totalChequerasActualmente']}</p>\n""")
                elif x[1]['tipo'] == 'ALTA_TARJETA_CREDITO':
                    e.write (f"""<p>{x[0]} | {x[1]['fecha']} | {x[1]['tipo']} | CUENTA NUMERO {x[1]['cuentaNumero']} | {x[1]['estado']} | motivo: {x[1]['razon']} tarjetas actuales: {x[1]['totalTarjetasDeCreditoActualmente']}</p>\n""")
                elif x[1]['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                    e.write (f"""<p>{x[0]} | {x[1]['fecha']} | {x[1]['tipo']} | CUENTA NUMERO {x[1]['cuentaNumero']} | {x[1]['estado']} | motivo: {x[1]['razon']}: Cupo diario restante: {x[1]['cupoDiarioRestante']} | monto solicitado: {x[1]['monto']} </p>\n""")
                elif x[1]['tipo'] == 'COMPRA_DOLAR':
                    e.write (f"""<p>{x[0]} | {x[1]['fecha']} | {x[1]['tipo']} | CUENTA NUMERO {x[1]['cuentaNumero']} | {x[1]['estado']} | motivo: {x[1]['razon']}</p>""")
                elif x[1]["tipo"] == "TRANSFERENCIA_ENVIADA":
                    e.write (f"""<p>{x[0]} | {x[1]['fecha']} | {x[1]['tipo']} | CUENTA NUMERO {x[1]['cuentaNumero']} | {x[1]['estado']} | motivo: {x[1]['razon']} | saldo restante: {x[1]['monto'] - x[1]['saldoEnCuenta']}</p>\n""")
                elif x[1]["tipo"] == "TRANSFERENCIA_RECIBIDA":
                    e.write (f"""<p>{x[0]} | {x[1]['fecha']} | {x[1]['tipo']} | CUENTA NUMERO {x[1]['cuentaNumero']} | {x[1]['estado']} | motivo: {x[1]['razon']} | monto de transferencia: {x[1]['monto']}</p>\n""")

            elif x[1]['estado'] == 'ACEPTADA':
                if x[1]['tipo'] == 'ALTA_CHEQUERA':
                    e.write (f"""<p>{x[0]} | {x[1]['fecha']} | {x[1]['tipo']} | CUENTA NUMERO {x[1]['cuentaNumero']} | {x[1]['estado']} | chequeras actuales: {x[1]['totalChequerasActualmente']}</p>\n""")
                elif x[1]['tipo'] == 'ALTA_TARJETA_CREDITO':
                    e.write (f"""<p>{x[0]} | {x[1]['fecha']} | {x[1]['tipo']} | CUENTA NUMERO {x[1]['cuentaNumero']} | {x[1]['estado']} | tarjetas actuales: {x[1]['totalTarjetasDeCreditoActualmente']}</p>\n""")
                elif x[1]['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                    e.write (f"""<p>{x[0]} | {x[1]['fecha']} | {x[1]['tipo']} | CUENTA NUMERO {x[1]['cuentaNumero']} | {x[1]['estado']} | Cupo diario restante: {x[1]['cupoDiarioRestante']} | monto solicitado: {x[1]['monto']} </p>\n""")
                elif x[1]['tipo'] == 'COMPRA_DOLAR':
                    e.write (f"""<p>{x[0]} | {x[1]['fecha']} | {x[1]['tipo']} | CUENTA NUMERO {x[1]['cuentaNumero']} | {x[1]['estado']} | </p>""")
                elif x[1]["tipo"] == "TRANSFERENCIA_ENVIADA":
                    e.write (f"""<p>{x[0]} | {x[1]['fecha']} | {x[1]['tipo']} | CUENTA NUMERO {x[1]['cuentaNumero']} | {x[1]['estado']} | saldo restante: {x[1]['monto'] - x[1]['saldoEnCuenta']}</p>\n""")
                elif x[1]["tipo"] == "TRANSFERENCIA_RECIBIDA":
                    e.write (f"""<p>{x[0]} | {x[1]['fecha']} | {x[1]['tipo']} | CUENTA NUMERO {x[1]['cuentaNumero']} | {x[1]['estado']} | monto de transferencia: {x[1]['monto']}</p>\n""")
                    

def plantillaHTML(cliente,transacciones):
    archivoHTML = open("python\SEGMENTACION DE CLIENTES\indexpy.html", "w")
    htmlBase = f"""<html>
    <head>
    <title>INFORME CLIENTE</title>
    <h1>CLIENTE NR: {cliente.numero} </h1>    <h1>NOMBRE:{cliente.nombre}</h1>   <h1>APELLIDO:{cliente.apellido}</h1>      <h1> DNI:{cliente.dni} </h1>
    <h1>DIRECCION:</h1><p>PAIS: {cliente.direccion.cp}</p>
    <p>PROVINCIA: {cliente.direccion.estado}</p>
    <p>CIUDAD: {cliente.direccion.ciudad}</p>
    <p>CALLE: {cliente.direccion.calle}</p>
    <p>NUMERO: {cliente.direccion.numero}</p>
    </head>
    <body>
    <p>Se realizaron las siguientes operaciones:</p>

    """
    archivoHTML.write(htmlBase)
    archivoHTML.close()
    conversion(razones(cliente = cliente,archivo = transacciones))

