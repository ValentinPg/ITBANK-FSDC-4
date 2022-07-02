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

from calendar import c
import csv
from logging.config import dictConfig
from operator import index
import os

print("Bienvenido a ITBANK, este es el sistema de busqueda de cheques")
print('los datos se encuentran almacenados en el archivo "info cheques.csv"')

dni = input("ingrese el DNI del cliente (sin puntos): ")
estado = input("Ingrese el estado de cheque que desea conocer (ACEPTADO, RECHAZADO o PENDIENTE.): ")
# salida = (input("ingrese si quiere que la salida sea en formato pantalla o CSV: ")).lower()

# while salida != "pantalla" and salida != "csv":
#     print("fromato invallido, por favor ingrese otra vez")
#     salida = (input("ingrese si quiere que la salida sea en formato pantalla o CSV: ")).lower()




def obtenerInfo():   
    with open("python\info-cheques.csv") as abrirArchivo:
        archivo = csv.DictReader(abrirArchivo)
        for linea in archivo:
            if dni == linea["DNI"]:
                documento = linea["NroCheque"]
                tipoCheque = linea["Tipo"]
                estadoCheque = linea["Estado"]
                print(f"el numero de cheque es: {documento}")
                print(f"el cheque fue {tipoCheque}")
                print(f"el estado del cheque es: {estadoCheque}")
                


def estadoCheque():   
    with open("python\info-cheques.csv") as abrirArchivo:
        archivo = csv.DictReader(abrirArchivo)
        for linea in archivo:
            if dni == linea["DNI"] and estado != linea["Estado"]:
                print('No se encontraron coincidencias con el estado de cheque solicitado para el DNI correspondiente.')
            if dni == linea["DNI"] and estado == linea["Estado"]:
                estadoCheque = linea["Estado"]
                nCheque = linea["NroCheque"]
                cBanco = linea["CodigoBanco"]
                cSucursal = linea["CodigoScurusal"]
                nCO = linea["NumeroCuentaOrigen"]
                NCD = linea["NumeroCuentaDestino"]
                valor = linea["Valor"]
                fechaOrigen = linea["FechaOrigen"]
                FechaPago = linea["FechaPago"]
                Tipo = linea["Tipo"]

                
                print(f'El numero de cheque es: {nCheque} ')
                print(f'El código de banco es: {cBanco} ')
                print(f'El código de sucursal es: {cSucursal} ')
                print(f'El número de cuenta de origen es: {nCO} ')
                print(f'El número de cuenta de destino es: {NCD} ')
                print(f'El valor del cheque es: ${valor} ')
                print(f'La fecha de origen del cheque es: {fechaOrigen} ')
                print(f'La fecha de pago del cheque es: {FechaPago} ')
                print(f'El tipo de cheque es: {Tipo}')
                break

estadoCheque()
#obtenerInfo()