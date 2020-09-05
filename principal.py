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
__version__ = "0.1"


def menu():

    while True:
        consulta = int(input('Ingrese 1, para "VALIDACIÓN DE LA EMPRESA": \nIngrese 2, para "VALIDAR DATOS": \nIngese 3, para "SALIR"'))
        
        if consulta == 1:
            pass
            
        elif consulta == 2:
            pass

        elif consulta == 3:
            print('Ha salido del programa')
            break 

        else:
            print('El valor ingresado no corresponde con los indicados, intente nuevamente')

if __name__ == '__main__':
    
     print('Bienvenido al programa de verificación de permiso provincial')

