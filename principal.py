#!/usr/bin/env python
'''
Página principal [Proyecto Inicial Python]
---------------------------
Autor: Johana Rangel
Version: 0.1

Descripcion:
Programa creado para validar permisos de circulación provincial.
'''

__author__ = "Johana Rangel"
__email__ = "johanarang@hotmail.com"
__version__ = "0.3"

import csv
import os
import re
import funcion_validacion
import validar_ingreso


consulta = int(input('Ingrese 1, para "VALIDACIÓN DE LA EMPRESA": \nIngrese 2, para "VALIDAR DATOS": \nIngrese 3, para "SALIR"\n'))

def menu(consulta):
        
    if consulta == 1:

        print('Bienvenido a la validación de trabajadores por empresa para ingreso provincial.')

        funcion_validacion.validacion()
        
    elif consulta == 2:

        print('Bienvenido a la validación de datos en puntos de control para ingreso provincial.')
        
        validar_ingreso.ingresa()

    elif consulta == 3:
        print('Ha salido del programa')
        
    else:
        print('El valor ingresado no corresponde con los indicados, intente nuevamente')

if __name__ == '__main__':
    
    print('Bienvenido al programa de verificación de permiso provincial')
    menu(consulta)
    

