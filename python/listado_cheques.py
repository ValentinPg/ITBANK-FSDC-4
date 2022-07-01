# NroCheque: Número de cheque, este debe ser único por cuenta.
# CodigoBanco: Código numérico del banco, entre 1 y 100.
# CodigoSucursal: Código numérico de la sucursal del banco va entre 1 y 300.
# NumeroCuentaOrigen: Cuenta de origen del cheque.
# NumeroCuentaDestino: Cuenta donde se cobra el cheque.
# Valor: float con el valor del cheque.
# FechaOrigen: Fecha de emisión: (En timestamp)
# FechaPago: Fecha de pago o cobro del cheque (En timestamp)
# DNI: String con DNI del cliente donde se permite identificarlo
# Estado: Puede tener 3 valores pendiente, aprobado o rechazado.
# TIPO: "EMITIDO" O "DEPOSITADO"

import csv
from operator import index

# print("Bienvenido a ITBANK, este es el sistema de busqueda de cheques")
# print('los datos se encuentran almacenados en el archivo "info cheques.csv"')

dni = input("ingrese el DNI del cliente (sin puntos): ")

while len(dni) != 8:
    print("DNI invalido, el numero debe tener 8 digitos")
    dni = input("ingrese el DNI del cliente (sin puntos): ")

# salida = (input("ingrese si quiere que la salida sea en formato pantalla o CSV: ")).lower()

# while salida != "pantalla" and salida != "csv":
#     print("fromato invallido, por favor ingrese otra vez")
#     salida = (input("ingrese si quiere que la salida sea en formato pantalla o CSV: ")).lower()
usuarios = []
with open("python\info-cheques.csv") as abrirArchivo:
    archivo = csv.reader(abrirArchivo)
    for linea in archivo:
       usuarios.append((linea[0::]))
       
del usuarios[0]


for persona in usuarios:
    for deudor in persona:
        if dni == deudor:
            print(persona)
    
