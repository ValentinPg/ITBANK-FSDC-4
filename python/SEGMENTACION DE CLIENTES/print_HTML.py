from razones import RazonAltaChequera,RazonAltaTarjetaCredito,RazonCompraDolar,RazonRetiroEfectivo,RazonTransferenciaEnviada,RazonTransferenciaRecibida
#variable que va a almacenar todas las transacciones
transeferencias = None

#funcion que junta todas las transacciones con sus razones de rechazo ya especificadas
def obtenerRazones(cliente):
    #invocamos las clases
    RazonAltaChequera().resolver(cliente)
    RazonTransferenciaRecibida().resolver(cliente)
    RazonTransferenciaEnviada().resolver(cliente)
    RazonRetiroEfectivo().resolver(cliente)
    RazonCompraDolar().resolver(cliente)
    RazonAltaTarjetaCredito().resolver(cliente)
    #juntamos los valores de las listas
    transeferencias = (RazonAltaChequera().rechazados + RazonAltaChequera().aprobados)
    transeferencias +=(RazonAltaTarjetaCredito().rechazados + RazonAltaTarjetaCredito().aprobados)
    transeferencias += (RazonCompraDolar().aprobados + RazonCompraDolar().rechazados)
    transeferencias += (RazonRetiroEfectivo().aprobados + RazonRetiroEfectivo().rechazados)
    transeferencias +=(RazonTransferenciaEnviada().rechazados + RazonTransferenciaEnviada().aprobados)
    transeferencias +=(RazonTransferenciaRecibida().aprobados+ RazonTransferenciaRecibida().rechazados)
    return transeferencias


def conversion(lista):
    for x in enumerate(lista):
        with open("python\SEGMENTACION DE CLIENTES\indexpy.html", "a+") as e:
            e.write (f"""<p>{x}</p>\n""")

def plantillaHTML(cliente):
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
    conversion(obtenerRazones(cliente))

