from JSONprueba import Json,eventos_black,eventos_classic,eventos_gold
from moduloCliente import Cliente_black,Cliente_clasico,Cliente_gold,iniciarPrograma
from razones import Razon,RazonAltaChequera,RazonAltaTarjetaCredito,RazonCompraDolar,RazonRetiroEfectivo,RazonTransferenciaEnviada,RazonTransferenciaRecibida

#-------------------------Ingrese el archivo que se desea escanear(eventos_classic,eventos_gold,eventos_black)---------------------------------------------------------#
archivo = eventos_gold
x = iniciarPrograma(archivo)
# RazonAltaChequera().resolver(x)
# print(RazonAltaChequera().rechazados)
# RazonAltaTarjetaCredito().resolver(x)
# print(RazonAltaTarjetaCredito().rechazados)
# RazonCompraDolar().resolver(x)
# print(RazonCompraDolar().aprobados)
# RazonRetiroEfectivo().resolver(x)
# print(RazonRetiroEfectivo().aprobados)
# RazonTransferenciaEnviada().resolver(x)
# print(RazonTransferenciaEnviada().rechazados)
RazonTransferenciaRecibida().resolver(x)
print(RazonTransferenciaRecibida().aprobados)
#--------------------------El archivo HTML se llama: -------------------------------------------------------------------------------------------------------#