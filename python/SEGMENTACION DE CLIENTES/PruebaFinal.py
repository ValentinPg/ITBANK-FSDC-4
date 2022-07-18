from JSONprueba import Json,eventos_black,eventos_classic,eventos_gold
from moduloCliente import Cliente_black,Cliente_clasico,Cliente_gold,iniciarPrograma
from razones import Razon

#-------------------------Ingrese el archivo que se desea escanear(eventos_classic,eventos_gold,eventos_black)---------------------------------------------------------#
x = iniciarPrograma(eventos_gold)
print(x)
Razon(x)


#--------------------------El archivo HTML se llama: -------------------------------------------------------------------------------------------------------#