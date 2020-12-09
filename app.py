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
        result += "<h3>[GET] /menu.html --> HTML de bienvenida con las acciones a realizar</h3>"
        result += "<h3>[GET] /empresa.html --> muestra el HTML con el formulario de registro</h3>"
        result += "<h3>[POST] /procesar --> ingreso del registro en la base de datos</h3>"
        result += "<h3>[GET] /validar_datos.html --> muestra el HTML de consulta de código en la base de datos</h3>"
        result += "<h3>[GET] /resultado_consulta --> muetra el resultado de la búsqueda por código</h3>"
        #result += "<h3>[GET] /pulsaciones/tabla?limit=[]&offset=[] --> mostrar últimas pulsaciones registradas (limite and offset are optional)</h3>"
        #result += "<h3>[GET] /pulsaciones/{name}/historico --> mostrar el histórico de pulsaciones de una persona</h3>"
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
        return render_template('reset.html')
    except:
        return jsonify({'trace': traceback.format_exc()})

@app.route("/menu.html")
def menu():
    try:
        # Imprimir los distintos endopoints disponibles
        return render_template('menu.html')
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route("/empresa.html", methods= ['GET'])  #Debo colocar el nombre del archivo html para que funcionen los botones.
def registro_empresa():
    if request.method == 'GET':
        try:
            # Imprimir los distintos endopoints disponibles
            return render_template('empresa.html')
        except:
            return jsonify({'trace': traceback.format_exc()})


@app.route('/procesar', methods=['POST'])
def procesar():
    
    if request.method == 'POST':
        try:
            # Obtener del HTTP POST JSON de los datos registrados por la empresa
            codigo = str(request.form.get('codigo'))
            empresa= str(request.form.get('empresa'))
            actividad = str(request.form.get('actividad'))
            nombre = str(request.form.get('nombre'))
            apellido = str(request.form.get(' apellido'))
            dni = str(request.form.get('dni')) 

            if(empresa is None or actividad is None or nombre is None or apellido is None
                or codigo is None or codigo.isdigit() is False or dni is None or dni.isdigit() is False):
                # Datos ingresados incorrectos
                    return Response(status=400)

            empresa_valida.insert(int(codigo), empresa, actividad, nombre, apellido, int(dni))
            return render_template('procesado.html')

        except:
            return jsonify({'trace': traceback.format_exc()})

@app.route("/validar_datos.html", methods= ['GET'])
def validar_datos():
    try:
        # Imprimir los distintos endopoints disponibles
        return render_template('validar_datos.html')
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route("/consulta", methods= ['POST'])
def consulta():

    if request.method == 'POST':
        try:
            # Imprimir los distintos endopoints disponibles
            codigo = str(request.form.get('codigo'))
            codigo, empresa, actividad, nombre, apellido, dni = empresa_valida.consulta(int(codigo))

            return render_template('consulta.html', codigo=codigo, empresa=empresa, actividad=actividad, nombre=nombre, apellido=apellido, dni=dni)

        except:
            return jsonify({'trace': traceback.format_exc()})


if __name__ == '__main__':
    print('Proyecto desarrollador python!')
    #Lanzar server
    app.run(host=server['host'],
            port=server['port'],
            debug=True)