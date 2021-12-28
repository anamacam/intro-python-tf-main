#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Ana
import datetime


class Cuenta(object):

    def __init__(self, monto_inicio=0, numero_de_cuenta=0):  # contructor, siempre de la misma forma
        self.cantidad = monto_inicio
        self.numero_de_cuenta = numero_de_cuenta
        self.movimientos = []
        self.activa = True

    def aplicar_gasto(self, monto):  # retirar
        if self.activa:
            return True
        self.cantidad = self.cantidad - monto
        self.crear_movimiento("Estamos aplicando un gasto", monto)
        return f"Se ha realizado un retiro {self.movimientos}, su saldo actual es de {self.cantidad}"

    def aplicar_deposito(self, monto):  # ingresar
        if self.activa:
            return True
        self.cantidad = self.cantidad + monto
        self.crear_movimiento("Estamos aplicando un deposito", monto)
        return f"Se ha realizado un deposito {self.movimientos}, su saldo actual es de {self.cantidad}"

    def desactivar(self):
        if self.cantidad == 0:
            self.activa = False
            return f"Su cuenta {self.numero_de_cuenta} ha sido {self.activa} " \
                   f" por fondos insuficiente {self.cantidad}:"

    def activar(self):
        if self.cantidad == 0:
            self.activa = True
            return f"Su cuenta ha sido ha sido activada satisfactoriamente con el {self.numero_de_cuenta} " \
                   f" y un saldo a favor de {self.cantidad}:"

    def crear_movimiento(self, descripcion, monto):
        movimiento = MovimientoCuenta(descripcion, monto)
        self.movimientos.append(movimiento)

    def __str__(self):
        print(f"CUENTA comun {self.cantidad},{self.numero_de_cuenta}")


class CuentaJoven(Cuenta):

    def __init__(self, bonificacion, monto_inicio=0, numero_de_cuenta=0):
        Cuenta.__init__(self, monto_inicio, numero_de_cuenta)
        self.bonificacion = bonificacion

    def __str__(self):
        print(f"CUENTA JOVEN {self.cantidad},{self.numero_de_cuenta,},{self.bonificacion}")


class MovimientoCuenta(object):

    def __init__(self, descripcion, monto_del_movimiento):
        self.fecha_y_hora = datetime.datetime.now()
        self.descripcion = descripcion
        self.monto = monto_del_movimiento

    def __str__(self):
        return f"{self.fecha_y_hora} {self.descripcion} {self.monto}"
