from JSONprueba import Json,eventos_black,eventos_classic,eventos_gold
from moduloCliente import Cliente_black,Cliente_clasico,Cliente_gold,iniciarPrograma
from razones import Razon,RazonAltaChequera,RazonAltaTarjetaCredito,RazonCompraDolar,RazonRetiroEectivo,RazonTransferenciaEnviada,RazonTransferenciaRecibida

#-------------------------Ingrese el archivo que se desea escanear(eventos_classic,eventos_gold,eventos_black)---------------------------------------------------------#
archivo = eventos_classic
x = iniciarPrograma(archivo)
RazonAltaChequera().resolver(x)
# print(RazonAltaChequera().resolver(x,"ALTA_CHEQUERA"))
# print(RazonAltaTarjetaCredito().resolver(x,"ALTA_TARJETA_CREDITO"))
# print(RazonCompraDolar().resolver(x,"COMPRA_DOLAR"))
# print(RazonRetiroEectivo().resolver(x,"RETIRO_EFECTIVO_CAJERO_AUTOMATICO"))
# print(RazonTransferenciaEnviada().resolver(x,"TRANSFERENCIA_ENVIADA"))
# print(RazonTransferenciaRecibida().resolver(x,"TRANSFERENCIA_RECIBIDA"))


#--------------------------El archivo HTML se llama: -------------------------------------------------------------------------------------------------------#