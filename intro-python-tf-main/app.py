#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Ana

import flask
from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy
import config

# create the application object
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

# definimos configuraciones
app.config['UPLOAD_FOLDER'] = './'
app.config['MAX_CONTENT_PATH'] = 2048

# definimos nuestros datos en memoria (base de datos)
lista_de_datos = {}


@app.route('/procesar_depositos', methods=['POST'])
def procesar_depositos():
    if request.method == 'POST':
        f = request.files['depositos']
        f.save(f.depositos)

        lista_de_datos = proceso_cuentas.procesar_depositos(lista_de_datos, f.depositos)
        return flask.redirect(flask.url_for('home'), code=302)


@app.route('/procesar_gastos', methods=['POST'])
def procesar_gastos():
    if request.method == 'POST':
        f = request.files['gastos']
        f.save(f.gastos)
        # No reconoce la lista de datos
        lista_de_datos = proceso_cuentas.procesar_gastos(lista_de_datos, f.gastos)
        return flask.redirect(flask.url_for('home'), code=302)
    pass


@app.route('/procesar_transferencias', methods=['POST'])
def procesar_transferencias():
    if request.method == 'POST':
        f = request.files['transferencias']
        f.save(f.transferencias)
        # No reconoce la lista de datos
        lista_de_datos = proceso_cuentas.procesar_transferencias(lista_de_datos, f.transferencias)
        return flask.redirect(flask.url_for('home'), code=302)
    pass


@app.route('/proceso')
def proceso():
    return render_template('proceso.html')


@app.route('/<int:dni>')
def home(dni):
    # dni = request.args.get('dni')
    try:
        persona_titular = lista_de_datos[str(dni)]
        return render_template('home-banking.html',
                               saludo=persona_titular.saludo(),
                               movements=persona_titular.obtener_todos_los_movimientos())
    except Exception as error:
        print(error)
        return render_template('error.html')


# El dato que arroja en la terminal es la preguta ¿cuantos años tiene? y no rentediza el template
if __name__ == '__main__':
    import proceso_cuentas
    lista_de_datos = proceso_cuentas.crear_cuentas()
    app.run(debug=True)