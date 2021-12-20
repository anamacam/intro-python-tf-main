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
    # TODO: procesar linea a linea del archivo, y aplicar a cada cuenta de las personas
    # Return: debe devolver las cuentas actualizadas
    pass


def procesar_depositos(cuentas, archivo):
    # TODO: procesar linea a linea del archivo, y aplicar a cada cuenta de las personas
    # Return: debe devolver las cuentas actualizadas
    pass


def procesar_transferencias(cuentas, archivo):
    # TODO: procesar linea a linea del archivo, y aplicar a cada cuenta de las personas
    # Return: debe devolver las cuentas actualizadas
    pass
