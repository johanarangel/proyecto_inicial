#!/usr/bin/env python
'''
Permiso de circulación provincial
---------------------------
Autor: Johana Rangel
Version: 1.0

Descripcion:
Programa creado para administrar la base de datos de registro
de empleados validados por la empresa
'''

__author__ = "Johana Rangel"
__email__ = "johanarang@hotmail.com"
__version__ = "1.0"

import os
import sqlite3
import requests
import json

db = {}


def create_schema():

    # Conectarnos a la base de datos
    # En caso de que no exista el archivo se genera
    # como una base de datos vacia
    conn = sqlite3.connect(db['database'])

    # Crear el cursor para poder ejecutar las querys
    c = conn.cursor()

    # Obtener el path real del archivo de schema
    script_path = os.path.dirname(os.path.realpath(__file__))
    schema_path_name = os.path.join(script_path, db['schema'])

    # Crar esquema desde archivo
    c.executescript(open(schema_path_name, "r").read())

    # Para salvar los cambios realizados en la DB debemos
    # ejecutar el commit, NO olvidarse de este paso!
    conn.commit()

    # Cerrar la conexión con la base de datos
    conn.close()

def insert(codigo, empresa, actividad, nombre, apellido, dni):
    conn = sqlite3.connect(db['database'])
    c = conn.cursor()

    values = [codigo, empresa, actividad, nombre, apellido, dni]

    c.execute("""
        INSERT INTO heartrate (codigo, empresa, actividad, nombre, apellido, dni)
        VALUES (?,?,?);""", values)

    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()
