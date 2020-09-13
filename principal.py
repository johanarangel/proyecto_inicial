#!/usr/bin/env python
'''
Página principal [Proyecto Inicial Python]
---------------------------
Autor: Johana Rangel
Version: 0.4

Descripcion:
Programa creado para validar los permisos de circulación provincial.
'''

__author__ = "Johana Rangel"
__email__ = "johanarang@hotmail.com"
__version__ = "0.4"

import csv
import os
import re
import funcion_validacion
import validar_ingreso

'''
El programa cuenta inicialmente con un menu con las acciones a realizar (para validacion de 
la empresa, validar datos en los puntos de control y para salir del programa), cada opción
del menu es entera, quedando almacenada la opcion en la variable consulta, variable que se pasa 
por parámetro en la función menu.
''' 
#Atrapando excepción para validación de formato de entrada de datos para la variable consulta.

try:
    consulta = int(input('Ingrese 1, para "VALIDACIÓN DE LA EMPRESA": \nIngrese 2, para "VALIDAR DATOS": \nIngrese 3, para "SALIR"\n'))

except:
    print('El valor indicado no corresponde con lo indicado. Intente nuevamente.')
    consulta = int(input('Ingrese 1, para "VALIDACIÓN DE LA EMPRESA": \nIngrese 2, para "VALIDAR DATOS": \nIngrese 3, para "SALIR"\n'))

def menu(consulta):
    
    if consulta == 1:
        
        '''
        En este punto, al ser la variable consulta es igual a uno, se imprime en pantalla el 
        mensaje de bienvenida a la "Validación de trabajadores por empresa para ingreso provincial".
        Se importa el módulo llamado funcion_validacion que contiene la funcion "validación", cuya 
        acción es agregar por parte de la empresa los datos solicitados.
        '''
         
        print('Bienvenido a la validación de trabajadores por empresa para ingreso provincial.')

        funcion_validacion.validacion()
        
    elif consulta == 2:

        '''
        Esta opción, funciona cuando la variable consulta es igual a dos, se imprime en pantalla el 
        mensaje de bienvenida a la "Validación de datos en puntos de control para ingreso provincial".
        Se importa el módulo llamado "validar_ingreso" que contiene la funcion "ingresa", cuya 
        acción es buscar en la base de datos "validacionempresas.csv" si está registrado por la 
        empresa que requiere sus servicios. Imprimiendo por pantalla si está registrado los datos
        y si tiene acceso provincial o no. En caso, tenga permiso queda almacenado en un segundo archivo csv
        "ingresoprovincial" el ingrese a la provincia.
        '''
        print('Bienvenido a la validación de datos en puntos de control para ingreso provincial.')
        
        validar_ingreso.ingresa()

    elif consulta == 3:
        print('Ha salido del programa') #Opción para salir del programa.
        
    else:

        #Opción que informa que los valores ingresados no corresponden 
        #y tiene la opción de volver a intentarlo y capturando posibles
        #errores de excepción.

        print('El valor ingresado no corresponde con los indicados, intente nuevamente')
        
        try:
            consulta = int(input('Ingrese 1, para "VALIDACIÓN DE LA EMPRESA": \nIngrese 2, para "VALIDAR DATOS": \nIngrese 3, para "SALIR"\n'))

        except:
            print('El valor indicado no corresponde con lo indicado. Intente nuevamente.')
            consulta = int(input('Ingrese 1, para "VALIDACIÓN DE LA EMPRESA": \nIngrese 2, para "VALIDAR DATOS": \nIngrese 3, para "SALIR"\n'))

if __name__ == '__main__':
    
    print('Bienvenido al programa de verificación de permiso provincial')
    menu(consulta)
    

