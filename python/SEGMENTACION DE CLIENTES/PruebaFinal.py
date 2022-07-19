from JSONprueba import Json,eventos_black,eventos_classic,eventos_gold
from moduloCliente import Cliente_black,Cliente_clasico,Cliente_gold,iniciarPrograma
from razones import Razon,RazonAltaChequera,RazonAltaTarjetaCredito,RazonCompraDolar,RazonRetiroEectivo,RazonTransferenciaEnviada,RazonTransferenciaRecibida

#-------------------------Ingrese el archivo que se desea escanear(eventos_classic,eventos_gold,eventos_black)---------------------------------------------------------#
archivo = eventos_black
x = iniciarPrograma(archivo)
# RazonAltaChequera().resolver(x)
# print(RazonAltaChequera().rechazados)
# RazonAltaTarjetaCredito().resolver(x)
# print(RazonAltaTarjetaCredito().rechazados)
# RazonCompraDolar().resolver(x)
# print(RazonCompraDolar().aprobados)
RazonRetiroEectivo().resolver(x)
print(RazonRetiroEectivo.rechazados)


#--------------------------El archivo HTML se llama: -------------------------------------------------------------------------------------------------------#