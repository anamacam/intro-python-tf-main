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
    archivo = open("archivo.csv", "r")
    archivo_csv = csv.reader(archivo)
    for gastos, dni, in archivo_csv:
        if gastos in gastos:
            cuentas.aplicar_gastos()
            gastos[dni] = gastos
    archivo.close()
    return gastos


def procesar_depositos(cuentas, archivo):
    depositos = {}
    archivo = open("archivo.csv", "r")
    archivo_csv = csv.reader(archivo)
    for depositos, dni in archivo_csv:
        if depositos in depositos:
            cuentas.aplicar_depositos()
            depositos[dni] = depositos
    archivo.close()
    return depositos


def procesar_transferencias(cuentas, archivo):
    tranferencias = {}
    archivo = open("archivo.csv", "r")
    archivo_csv = csv.reader(archivo)
    for tranferencias, dni, in archivo_csv:
        if tranferencias in tranferencias:
            cuentas.aplicar_transferencia()
            tranferencias[dni] = tranferencias
    archivo.close()
    return tranferencias
