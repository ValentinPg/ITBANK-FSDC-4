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

# # print("Bienvenido a ITBANK, este es el sistema de busqueda de cheques")
# # print('los datos se encuentran almacenados en el archivo "info cheques.csv"')

# #funcion para evaluar el dni ingresado por el cliente
# def evaluar():
#     # Pedimos dni
#     dni = input("Ingrese número de DNI del cliente ")
#     # Evaluamos que el dni ingresado corresponde
#     numbers = []
#     while (len(dni) >= 8) and (len(dni) <= 10):
#         for i in range(0, 10):
#             numbers.append(str(i))
#         for char in dni:
#             if char not in numbers:
#                 print("El dni es invalido, debe contener solo caracteres númericos")
#         break
#     return dni #Deberia retoranar el dni
# evaluar()

# #funcion para elegir formato de impresion
# def formatoImpreso():
#     # Damos a elegir dos opciones de formato de impresion "Pantalla" o "CSV"
#     formato = input("¿Desea imprimir los datos en Pantalla o formato CSV? ").lower()
#     if formato == "pantalla":
#         formato_Pantalla = True
#     else:
#         formato_csv = True
# formatoImpreso()

# def pedirEstado():
#     # Preguntamos si quiere visualizar el estado en que se encuentra el cheque
#     estado = input("¿Desea visualizar el estado en que se encuentra los datos? ").lower()
#     if estado == "si":
#         visualizar_estado = True
#     else:
#         visualizar_estado = False    
# pedirEstado()

# def obtenerInfo():   
#     with open("python\info-cheques.csv") as abrirArchivo:
#         archivo = csv.DictReader(abrirArchivo)
#         for linea in archivo:
#             if dni in linea.values():
#                 print(linea)
# obtenerInfo()


# Pedimos dni

dni = input("Ingrese número de DNI del cliente ")
def evaluar(numeroDni):
    # Pedimos dni
    # Evaluamos que el dni ingresado corresponde
    numbers = []
    while (len(numeroDni) >= 8) and (len(numeroDni) <= 10): # Evalua la longitud entre 8 y 10 caracteres
        for i in range(0, 10):
            numbers.append(str(i))
        for char in numeroDni:
            if char not in numbers:
                print("El dni es invalido, debe contener solo caracteres númericos")
                dni = input("Ingrese número de DNI del cliente ")
                evaluar(dni)
        break
evaluar(dni)

def obtenerInfo():

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