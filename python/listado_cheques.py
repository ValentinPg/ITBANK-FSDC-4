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

from calendar import c
import csv
from logging.config import dictConfig
from operator import index
from optparse import Values
import os
import datetime
from queue import Empty
import time
from numpy import empty

#da la bienvenida al programa
print("Bienvenido a ITBANK, este es el sistema de busqueda de cheques")
print('los datos se encuentran almacenados en el archivo "info cheques.csv"')

#extrae la informacion del archivo .csv
def obtenerInfo():
    #se establece el filtro por DNI
    dni = input("ingrese el DNI del cliente (sin puntos): ")
    elemento = {}
    listado = []
    #Accede al archivo
    with open("python\info-cheques.csv") as abrirArchivo:
        #Abre el archivo como lector
        archivo = csv.DictReader(abrirArchivo)
        for linea in archivo:
            #Busca coincidencias con el filtro por DNI
            if dni == linea["DNI"]:
            
            #Extrae los datos Filtrados
                elemento["DNI"],                elemento["NroCheque"]           = linea["DNI"],                linea["NroCheque"]
                elemento["CodigoBanco"],        elemento["Tipo"]                = linea["CodigoBanco"],        linea["Tipo"]
                elemento["Estado"],             elemento["CodigoSucursal"]      = linea["Estado"],             linea["CodigoSucursal"]
                elemento["NumeroCuentaOrigen"], elemento["FechaOrigen"]         = linea["NumeroCuentaOrigen"], linea["FechaOrigen"]
                elemento["Valor"],              elemento["NumeroCuentaDestino"] = linea["Valor"],              linea["NumeroCuentaDestino"]
                elemento["FechaPago"]                                           = linea["FechaPago"]
                listado.append(elemento)

    #Cierra el archivo
    abrirArchivo.close()
    #Si no se estrajo datos se vuelve a realizar la funcion
    if len(listado) == 0:
        print("El numero ingresado es invalido o No se han encontrado Coincidencias\n Por Favor")
        return obtenerInfo()
    
    #Mensaje de salida para 1 dato
    elif len(listado) == 1:
        print(f"Se han encontrado {len(listado)} coincidencia")
        return listado

    #Mensaje de salida para más de 1 dato
    else:
        print(f"Se han encontrado {len(listado)} coincidencias")
        return listado  
           
#Establece filtro por estado del cheque
def estadoCheque(lista):
    estado = input("Ingrese el estado de cheque que desea conocer (APROBADO, RECHAZADO o PENDIENTE.), Deje vacio para obtener todos los cheques: ")
    elemento = {}
    listado = []   
    for linea in lista:
        #si la variable estado es igual al estado de algun cheque o si la variable esta vacia
        if estado == linea["Estado"] or not estado:
            #si la variable esta vacia devuelve todos los elementos de la lista
            #si la variable es igual al estado solo devuelve los elementos en ese estado

            #extrae los datos filtrados

            elemento["DNI"],                elemento["NroCheque"]           = linea["DNI"],                linea["NroCheque"]
            elemento["CodigoBanco"],        elemento["Tipo"]                = linea["CodigoBanco"],        linea["Tipo"]
            elemento["Estado"],             elemento["CodigoSucursal"]      = linea["Estado"],             linea["CodigoSucursal"]
            elemento["NumeroCuentaOrigen"], elemento["FechaOrigen"]         = linea["NumeroCuentaOrigen"], linea["FechaOrigen"]
            elemento["Valor"],              elemento["NumeroCuentaDestino"] = linea["Valor"],              linea["NumeroCuentaDestino"]
            elemento["FechaPago"]                                           = linea["FechaPago"]
            listado.append(elemento)

    if len(listado) == 0:
        print("El Parametro ingresado es invalido o No se han encontrado Coincidencias\n Por Favor")
        return estadoCheque(lista)
    elif len(listado) == 1:
        print(f"Se han encontrado {len(listado)} coincidencia")
        return listado
    else:
        print(f"Se han encontrado {len(listado)} coincidencias")
        return listado  
            

def salida(lista):
    elemento = {}
    listado = []   
    for linea in lista:

        elemento["DNI"],                elemento["NroCheque"]           = linea["DNI"],                linea["NroCheque"]
        elemento["CodigoBanco"],        elemento["Tipo"]                = linea["CodigoBanco"],        linea["Tipo"]
        elemento["Estado"],             elemento["CodigoSucursal"]      = linea["Estado"],             linea["CodigoSucursal"]
        elemento["NumeroCuentaOrigen"], elemento["Valor"]               = linea["NumeroCuentaOrigen"], linea["Valor"]
        elemento["NumeroCuentaDestino"]                                 = linea["NumeroCuentaDestino"]

        elemento["FechaOrigen"] = datetime.date.fromtimestamp(int(linea["FechaOrigen"]))
        elemento["FechaPago"]   = datetime.date.fromtimestamp(int(linea["FechaPago"]))

        listado.append(elemento)

    salida = input("Ingrese una salida: VER (Para ver en pantalla), EXPORTAR (Para crear un archivo .CSV)")
    if salida == "VER":
        for i in listado:
            print(f''' -------------------------------------------------------------------------------------------------

 Cheque N°{elemento["NroCheque"]}
 
 Fecha de Emision: {elemento["FechaOrigen"]}         Fecha de Pago: {elemento["FechaPago"]}

 DNI: {elemento["DNI"]}           Sucursal: {elemento["CodigoSucursal"]}            Codigo: {elemento["CodigoBanco"]}

 Cuenta de Origen: {elemento["NumeroCuentaOrigen"]}               Cuenta de Destino: {elemento["NumeroCuentaDestino"]}

 Tipo de Cheque: {elemento["Tipo"]}         Estado del Cheque: {elemento["Estado"]}

 Monto: {elemento["Valor"]} $
 -------------------------------------------------------------------------------------------------''')
    elif salida == "EXPORTAR":
        print("exportar")
    else:
        print("parametro incorrecto")
        

salida(estadoCheque(obtenerInfo()))