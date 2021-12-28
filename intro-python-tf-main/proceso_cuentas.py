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
    gastos = {}
    personas = {}
    archivo = open("gastos.csv", "r")
    archivo_csv = csv.reader(archivo)
    for dni, monto in archivo_csv:
        gasto = Gasto(dni, monto)
        gasto.aplicar_gasto()
        personas[dni] = gastos
    archivo.close()
    return f"cuenta actualizada"


def procesar_depositos(cuentas, archivo,importe_deposito_int):
    depositos = {}
    personas = {}
    archivo = open("depositos.csv", "r")
    archivo_csv = csv.reader(archivo)
    for dni, monto in archivo_csv:
        deposito = Deposito(dni, monto)
        deposito.aplicar_deposito()
        personas[dni] = depositos
    archivo.close()
    return f"cuenta actualizada"


def procesar_transferencias(cuentas, archivo):
    transferencias = {}
    personas = {}
    archivo = open("transferencias.csv", "r")
    archivo_csv = csv.reader(archivo)
    for dni, monto in archivo_csv:
        transferencia = Transferencia(dni, monto)
        transferencia.aplicar_deposito()
        personas[dni] = transferencias
    archivo.close()
    return f"cuenta actualizada"
