# import html as html
# from intentoJson import Json,eventos_black,eventos_classic,eventos_gold


# # import intentoJson
# # from intentoJson import Json,eventos_black,eventos_classic,eventos_gold



# file = Json(eventos_black)

# class HTML(object):
#     def __init__(self,imprimirTexto) -> None:
#         self.imprimirTexto = imprimirTexto
    
#     def imprimirHTML(self):
#         archivo = open("python\SEGMENTACION DE CLIENTES\indexpy.html", "w")
#         htmlBase = f"""<html>
#         <head>
#         <title>INFORME CLIENTE</title>
#         <h1>CLIENTE NR: {file.obtenerDatos("numero")} </h1>    <h1>NOMBRE:{file.obtenerDatos("nombre")}</h1>   <h1>APELLIDO:{file.obtenerDatos("apellido")}</h1>      <h1> DNI:{file.obtenerDatos("dni")} </h1>
#         </head>
#         <body>
#         <h2>Se realizaron las siguientes operaciones:{file.obtenerTransacciones()}</h2>
  
#         <p></p>
  
#         </body>
#         </html>
#         """
#         archivo.write(htmlBase)
#         archivo.close()
        
# HTML("hola").imprimirHTML()

#--------------------------------
import html
from JSONprueba import Json ,eventos_black,eventos_classic,eventos_gold
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


def conversion():
    convertido = json.loads(eventos_black)
    convertido.replace(",","")
    convertido.replace(":","")
    return convertido

def ImprimirHTML():
    with open("python\SEGMENTACION\indexpy.html", "a+"):
        for x in convertido:
            x.split(",")


