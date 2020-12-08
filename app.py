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


#from config import config


# Crear el server Flask
app = Flask(__name__)

# # Clave que utilizaremos para encriptar los datos
# app.secret_key = "flask_session_key_inventada"

# # Obtener la path de ejecución actual del script
# script_path = os.path.dirname(os.path.realpath(__file__))

# # Obtener los parámetros del archivo de configuración
# config_path_name = os.path.join(script_path, 'config.ini')
# db = config('db', config_path_name)
# server = config('server', config_path_name)

# # Enviar los datos de config de la DB
# title.db = db

@app.route("/")
def index():
    try:
        # Imprimir los distintos endopoints disponibles
        return render_template('menu.html')
    except:
        return jsonify({'trace': traceback.format_exc()})



if __name__ == '__main__':
    print('Proyecto desarrollador python!')
    #Lanzar server
    app.run()