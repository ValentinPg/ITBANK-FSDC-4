# NroCheque: Número de cheque, este debe ser único por cuenta.
# CodigoBanco: Código numérico del banco, entre 1 y 100.
# CodigoSucursal: Código numérico de la sucursal del banco va entre 1 y 300.
# NumeroCuentaOrigen: Cuenta de origen del cheque.
# NumeroCuentaDestino: Cuenta donde se cobra el cheque.
# Valor: float con el valor del cheque.
# FechaOrigen: Fecha de emisión: (En timestamp)
# FechaPago: Fecha de pago o cobro del cheque (En timestamp)

# Estado: Puede tener 3 valores pendiente, aprobado o rechazado.
# TIPO: "EMITIDO" O "DEPOSITADO"

import csv
from logging.config import dictConfig
from operator import index
from optparse import Values
import os
import datetime
import time
print("Bienvenido a ITBANK, este es el sistema de busqueda de cheques")
print('los datos se encuentran almacenados en el archivo "info cheques.csv"')

dni = input("ingrese el DNI del cliente (sin puntos): ")


# salida = (input("ingrese si quiere que la salida sea en formato pantalla o CSV: ")).lower()

# while salida != "pantalla" and salida != "csv":
#     print("fromato invallido, por favor ingrese otra vez")
#     salida = (input("ingrese si quiere que la salida sea en formato pantalla o CSV: ")).lower()





def obtenerInfo():   
    with open("python\info-cheques.csv") as abrirArchivo:
        archivo = csv.DictReader(abrirArchivo)
        for linea in archivo:
            if dni == linea["DNI"]:
                numeroCheque = linea["NroCheque"]
                CodigoBanco = linea["CodigoBanco"]
                tipoCheque = linea["Tipo"]
                estadoCheque = linea["Estado"]
                CodigoSucursal = linea["CodigoScurusal"]
                NumeroCuentaOrigen = linea["NumeroCuentaOrigen"]
                NumeroCuentaDestino = linea["NumeroCuentaDestino"]
                Valor = linea["Valor"]
                #convierto a int para tener la fecha
                linea["FechaOrigen"] = int(linea["FechaOrigen"])
                FechaOrigen = datetime.date.fromtimestamp(linea["FechaOrigen"])
                #convierto a int para tener la fecha
                linea["FechaPago"] = int(linea["FechaPago"])
                FechaPago = datetime.date.fromtimestamp(linea["FechaPago"])

                print(f"El numero del cheque es {numeroCheque}")
                print(f"El codigo del banco es {CodigoBanco}")
                print(f"El tipo de cheque es {tipoCheque}")
                print(f"El código de la sucursal es {CodigoSucursal}")
                print(f"El número de la cuenta de origen es {NumeroCuentaOrigen}")
                print(f"El número de la cuenta de destino es {NumeroCuentaDestino}")
                print(f"El cheque tiene un monto de {Valor} pesos")
                print(f"El cheque fue emitido: {FechaOrigen}")
                print(f"El cheque fue pagado {FechaPago}")
                print(f"El estado del cheque es: {estadoCheque}\n")
    abrirArchivo.close()      
           
obtenerInfo()

    
