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
from logging.config import dictConfig
from operator import index
import os

# print("Bienvenido a ITBANK, este es el sistema de busqueda de cheques")
# print('los datos se encuentran almacenados en el archivo "info cheques.csv"')

dni = int(input("ingrese el DNI del cliente (sin puntos ni espacios): "))

# while len(dni) != 8:
#     print("DNI invalido, el numero debe tener 8 digitos")
#     dni = input("ingrese el DNI del cliente (sin puntos): ")

# salida = (input("ingrese si quiere que la salida sea en formato pantalla o CSV: ")).lower()

# while salida != "pantalla" and salida != "csv":
#     print("fromato invallido, por favor ingrese otra vez")
#     salida = (input("ingrese si quiere que la salida sea en formato pantalla o CSV: ")).lower()



def obtenerInfo():   
    with open("python\info-cheques.csv") as abrirArchivo:
        archivo = csv.DictReader(abrirArchivo)
        for linea in archivo:
            if dni in linea.values():
                print(linea)
obtenerInfo()