#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Ana
from cuenta import Cuenta
from persona import Persona


def test_cuenta():
    cuenta = Cuenta()
    assert type(cuenta) == Cuenta
    assert type(cuenta) != Persona


def test_suma():
    result = 2 + 2
    assert result == 4
