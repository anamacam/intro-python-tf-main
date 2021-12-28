#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Ana
import csv

from persona import Persona


def crear_cuentas():
    """
    param: None
    :return: Lista de diccionarios
    """
    personas = {}
    archivo = open("personas.csv", "r")
    archivo_csv = csv.reader(archivo)
    titulos = next(archivo_csv)
    for nombre, dni, fecha_nacimiento in archivo_csv:
        persona = Persona(dni, nombre, fecha_nacimiento)
        persona.crear_cuenta()
        # La parte mas importante donde agrego al diccionario
        # con clave = dni el objecto persona
        personas[dni] = persona
    archivo.close()
    return personas


def procesar_gastos(cuentas, archivo):
    archivo = open("gastos.csv")
    primer_linea = True
    for linea in archivo:
        if not primer_linea:
            nro_cuenta, importe_gasto = linea.replace('\n', '').split(',')
            importe_gasto_int = float(importe_gasto)
            cuentas_actualizadas = aplicar_gastos(cuentas, nro_cuenta, importe_gasto_int)
        else:
            primer_linea = False
        archivo.close()
        return f"cuentas actualizada"


def procesar_depositos(cuentas, archivo,importe_deposito_int):
    archivo = open("depositos.csv")
    primer_linea = True
    for linea in archivo:
        if not primer_linea:
            nro_cuenta, monto_deposito = linea.replace('\n', '').split(',')
            importe_deposito_int = float(monto_deposito)
            cuentas_actualizadas = aplicar_depositos(cuentas, nro_cuenta, importe_deposito_int)
        else:
            primer_linea = False
        archivo.close()
    return f"cuenta actualizada"


def procesar_transferencias(cuentas, archivo):
    archivo = open("transferencias.csv")
    primer_linea = True
    for linea in archivo:
        if not primer_linea:
            nro_cuenta, monto_deposito = linea.replace('\n', '').split(',')
            importe_deposito_int = float(monto_deposito)
            cuentas_actualizadas = aplicar_depositos(cuentas, nro_cuenta, importe_deposito_int)
        else :
            primer_linea:
            nro_cuenta, monto_gasto = linea.replace('\n', '').split(',')
            importe_gasto_int = float(monto_gasto)
            cuentas_actualizadas = aplicar_depositos(cuentas, nro_cuenta, importe_gasto_int)
        archivo.close()
    return f"cuenta actualizada"
