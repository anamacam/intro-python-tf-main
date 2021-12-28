#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Ana
from sqlalchemy import DateTime, Integer, String, Column
from app import db

import datetime

from cuenta import Cuenta


def convertir_fecha(string_fecha):
    try:
        anio = string_fecha[0:4]
        mes = string_fecha[5:7]
        dia = string_fecha[8:10]
        return datetime.date(int(anio), int(mes), int(dia))
    except Exception as error:
        print(error)
        return f"¡Oops! fecha no valida. Intente nuevamente"


class Persona(db.Model):

    __tablename__ = 'personas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    fecha_nacimiento = Column(DateTime, nullable=False)
    dni = Column(String(8), nullable=False)

    def __init__(self, dni, nombre, str_fecha_nacimiento,):
        self.nombre = nombre
        self.fecha_nacimiento = convertir_fecha(str_fecha_nacimiento)
        self.dni = dni
        self.cuentas = []

    def __str__(self):
        return f'Nombre: {self.nombre}'

    @property
    def edad(self):
        hoy = datetime.date.today()
        delta = hoy - self.fecha_nacimiento
        return int(delta.days/365)

    def es_mayor_de_edad(self):
        return self.edad <= 18

    def crear_cuenta(self):
        edad = int(input("¿Cuántos años tiene? "))
        if edad > 18:
            print("Cuenta comun")
        else:
            print("Cuenta joven")

        cuenta = Cuenta()
        self.cuentas.append(cuenta)

    def obtener_todos_los_movimientos(self):
        todos_los_movimientos = []
        for cuenta in self.cuentas:
            todos_los_movimientos += cuenta.movimientos
        return todos_los_movimientos

    def saludo(self):
        return f"¡Hola! {self.nombre}, en este momento la temperatura es de:{clima_fecha.traer_fecha()} , " \
                   f"en la ciudad de {self.ciudad}:"
