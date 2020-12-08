#!/usr/bin/env python
'''
Página principal [Proyecto Programador Python]
---------------------------
Autor: Johana Rangel
Version: 1.0

Descripcion:
Programa creado para validar los permisos de circulación provincial.
'''

__author__ = "Johana Rangel"
__email__ = "johanarang@hotmail.com"
__version__ = "1.0"

import traceback
import io
import sys
import os
import base64
import json
import sqlite3
from datetime import datetime, timedelta
import requests

import numpy as np
from flask import Flask, request, jsonify, render_template, Response, redirect
import matplotlib
matplotlib.use('Agg')   # Para multi-thread, non-interactive backend (avoid run in main loop)
import matplotlib.pyplot as plt
# Para convertir matplotlib a imagen y luego a datos binarios
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.image as mpimg

import empresa_valida
from config import config


# Crear el server Flask
app = Flask(__name__)

# Clave que utilizaremos para encriptar los datos
app.secret_key = "flask_session_key_inventada"

# Obtener la path de ejecución actual del script
script_path = os.path.dirname(os.path.realpath(__file__))

# Obtener los parámetros del archivo de configuración
config_path_name = os.path.join(script_path, 'config.ini')
db = config('db', config_path_name)
server = config('server', config_path_name)

# Enviar los datos de config de la DB
empresa_valida.db = db

@app.route("/")
def index():
    try:
        # Imprimir los distintos endopoints disponibles
        result = "<h1>Bienvenido!!</h1>"
        result += "<h2>Endpoints disponibles:</h2>"
        result += "<h3>[GET] /reset --> borrar y crear la base de datos</h3>"
        #result += "<h3>[GET] /pulsaciones?limit=[]&offset=[] --> mostrar últimas pulsaciones registradas (limite and offset are optional)</h3>"
        #result += "<h3>[GET] /pulsaciones/tabla?limit=[]&offset=[] --> mostrar últimas pulsaciones registradas (limite and offset are optional)</h3>"
        #result += "<h3>[GET] /pulsaciones/{name}/historico --> mostrar el histórico de pulsaciones de una persona</h3>"
        result += "<h3>[GET] /registro --> HTML con el formulario de registro de pulsaciones</h3>"
        result += "<h3>[POST] /registro --> ingresar nuevo registro de pulsaciones por JSON</h3>"
        result += "<h3>[GET] /entrada --> HTML de bienvenida con las acciones a realizar</h3>"
        #result += "<h3>[POST] /login --> ingresar el nombre de usuario por JSON</h3>"
        #result += "<h3>[GET] /logout --> Terminar la sesion</h3>"

        return(result)
    except:
        return jsonify({'trace': traceback.format_exc()})

@app.route("/reset")
def reset():
    try:
        # Borrar y crear la base de datos
        empresa_valida.create_schema()
        result = "<h3>Base de datos re-generada!</h3>"
        return (result)
    except:
        return jsonify({'trace': traceback.format_exc()})

@app.route("/entrada")
def entrada():
    try:
        # Imprimir los distintos endopoints disponibles
        return render_template('menu.html')
    except:
        return jsonify({'trace': traceback.format_exc()})

@app.route("/registro", methods=['GET', 'POST'])
def registro():

    if request.method == 'GET':
        try:
            # Imprimir los distintos endopoints disponibles
            return render_template('empresa.html')
        except:
            return jsonify({'trace': traceback.format_exc()})

    if request.method == 'POST':
        try:
            # Obtener del HTTP POST JSON de los datos registrados por la empresa
            codigo = str(request.form.get('codigo de circulación'))
            empresa= str(request.form.get('nombre empresa'))
            actividad = str(request.form.get('actividad'))
            nombre = str(request.form.get('nombre'))
            apellido = str(request.form.get(' apellido'))
            dni = str(request.form.get('dni')) 

            if(empresa is None or actividad is None or nombre is None or apellido is None
                or codigo is None or codigo.isdigit() is False or dni is None or dni.isdigit() is False):
                # Datos ingresados incorrectos
                    return Response(status=400)

            empresa_valida.insert(int(codigo), empresa, actividad, nombre, apellido, int(dni))

        except:
            return jsonify({'trace': traceback.format_exc()})

if __name__ == '__main__':
    print('Proyecto desarrollador python!')
    #Lanzar server
    app.run(host=server['host'],
            port=server['port'],
            debug=True)