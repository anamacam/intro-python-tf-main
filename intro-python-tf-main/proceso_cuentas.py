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
    archivo = open("personas.csv", "r")
    archivo_csv = csv.reader(archivo)
    for nombre, dni, fecha_nacimiento in archivo_csv:
        gastos= Gastos(cantidad, gastos)
        if gastos in gastos:
         gastos.aplicar_gastos()
         persona[dni] = gastos
    archivo.close()
    return gastos

def procesar_depositos(cuentas, archivo):
    depositos = {}
    archivo = open("archivo.csv", "r")
    archivo_csv = csv.reader(archivo)
    for nombre, dni, fecha_nacimiento in archivo_csv:
        depositos = Depositos(cantidad, monto)
        if depositos in depositos:
         depositos.aplicar_depositos()
         persona[dni] = depositos
    archivo.close()
    return depositos


def procesar_transferencias(cuentas, archivo):
    tranferencias = {}
    archivo = open("archivo.csv", "r")
    archivo_csv = csv.reader(archivo)
    for nombre, dni, fecha_nacimiento in archivo_csv:
        tranferencias = Tranferencias(cantidad, monto)
        if tranferencias in tranferencias:
            tranferencias.aplicar_transferencia()
            persona[dni] = tranferencias
    archivo.close()
    return tranferencias
